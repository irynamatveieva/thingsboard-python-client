#!/bin/bash
#
# Copyright © 2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# Generates Python REST clients from OpenAPI specs using openapi-generator-cli.
#
# Usage:
#   ./generate-client.sh [options] <edition> [base-url]
#
# Arguments:
#   edition    ce | pe | paas | all
#   base-url   Optional. Fetches spec from <base-url>/v3/api-docs/thingsboard
#              and updates the local spec file before generation.
#              Not supported with "all".
#
# Options:
#   --verbose  Show full generator output (per-file writes, operations, etc.)
#   --dry-run  Generate into target/generated/ only. Skip copying to package dir,
#              common module overlay, and post-processing.
#
# Examples:
#   ./generate-client.sh ce                           # Generate CE from local spec
#   ./generate-client.sh all                          # Generate all editions from local specs
#   ./generate-client.sh ce http://localhost:8080      # Fetch spec from local TB, then generate
#   ./generate-client.sh --dry-run ce                  # Generate to target/ only, don't touch package dir
#   ./generate-client.sh --verbose ce                  # Full output, no log filtering
#
# What it does:
#   1. Optionally fetches OpenAPI spec from a running ThingsBoard instance
#   2. Validates the spec (warns on duplicate operationIds)
#   3. Runs openapi-generator-cli with Python target (single-class via SET_TAGS_FOR_ALL_OPERATIONS)
#   4. Copies generated tb_{edition}_client/ into the edition's package directory
#   5. Overlays common/ contents into the package directory
#   6. Runs scripts/post_process.py (license headers, lazy imports, JsonNode fixes, cleanup)
#
# Preserved on regeneration:
#   - <edition>/spec/openapi.json  (only updated when base-url is provided)
#
# Replaced on regeneration:
#   - <edition>/tb_{edition}_client/  (fully replaced from generated output)
#
# Output log: generate-client.log (overwritten on each run)
#
# Prerequisites: Java (for openapi-generator-cli JAR), Python 3
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
EDITIONS=("ce" "pe" "paas")

VERBOSE=false
DRY_RUN=false
while [ $# -gt 0 ]; do
  case "$1" in
    --verbose) VERBOSE=true; shift ;;
    --dry-run) DRY_RUN=true; shift ;;
    -*) echo "Unknown option: $1"; exit 1 ;;
    *) break ;;
  esac
done

if [ $# -eq 0 ]; then
  echo "Usage: $0 [--verbose] [--dry-run] <edition> [base-url]"
  echo "  edition: ce | pe | paas | all"
  echo "  base-url: optional, fetches spec from <base-url>/v3/api-docs/thingsboard"
  exit 1
fi

EDITION="$1"
BASE_URL="${2:-}"
LOG_FILE="$SCRIPT_DIR/generate-client.log"

# Log everything to file and stdout
exec > >(tee "$LOG_FILE") 2>&1

# -------------------------------------------------------------------
# JAR management (version-locked to match Java client)
# -------------------------------------------------------------------
OPENAPI_GENERATOR_VERSION="7.20.0"
GENERATOR_CACHE_DIR="${OPENAPI_GENERATOR_CACHE_DIR:-${HOME}/.cache/openapi-generator}"
GENERATOR_JAR="$GENERATOR_CACHE_DIR/openapi-generator-cli-${OPENAPI_GENERATOR_VERSION}.jar"

if [ ! -f "$GENERATOR_JAR" ]; then
  echo "Downloading openapi-generator-cli ${OPENAPI_GENERATOR_VERSION}..."
  mkdir -p "$GENERATOR_CACHE_DIR"
  curl -fSL -o "$GENERATOR_JAR" \
    "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${OPENAPI_GENERATOR_VERSION}/openapi-generator-cli-${OPENAPI_GENERATOR_VERSION}.jar"
fi

# Wrapper function so call sites look identical to the npx-based CLI
openapi-generator-cli() { java -jar "$GENERATOR_JAR" "$@"; }

# -------------------------------------------------------------------
# generate() — process a single edition
# -------------------------------------------------------------------
generate() {
  local edition="$1"
  local spec_file="$SCRIPT_DIR/$edition/spec/openapi.json"
  local output_dir="$SCRIPT_DIR/$edition/target/generated"
  local module_dir="$SCRIPT_DIR/$edition"

  # --- Optional spec fetch ---
  if [ -n "$BASE_URL" ]; then
    local api_url="$BASE_URL/v3/api-docs/thingsboard"
    echo "Fetching spec for $edition from $api_url"
    mkdir -p "$(dirname "$spec_file")"
    curl -sf "$api_url" -o "$spec_file" || { echo "Error: failed to fetch spec from $api_url"; exit 1; }
  fi

  if [ ! -f "$spec_file" ]; then
    echo "Error: spec file not found: $spec_file"
    exit 1
  fi

  rm -rf "$output_dir"

  # --- Spec validation ---
  echo "Validating spec: $spec_file"
  local validate_output
  validate_output=$(openapi-generator-cli validate -i "$spec_file" 2>&1) || {
    echo "$validate_output" | grep -v "Unused model:"
    exit 1
  }

  # --- Duplicate operationId detection (GEN-09) ---
  # ThingsBoard's spec generator appends _1, _2, etc. for duplicates; warn (not fail).
  local duplicates
  duplicates=$(grep -o '"operationId" *: *"[^"]*"' "$spec_file" | sed 's/.*: *"//;s/"//' | grep -E '_[0-9]+$' || true)
  if [ -n "$duplicates" ]; then
    echo "Warning: spec contains duplicate operationIds (suffixed by ThingsBoard):"
    echo "$duplicates" | sed 's/^/  /'
    echo "These will generate methods with numeric suffixes. Consider fixing @ApiOperation annotations."
  fi

  # --- Python client generation (single class via SET_TAGS_FOR_ALL_OPERATIONS) ---
  echo "Generating Python client for edition: $edition from $spec_file"
  java -jar "$GENERATOR_JAR" generate \
    -i "$spec_file" \
    -g python \
    -o "$output_dir" \
    --package-name "tb_${edition}_client" \
    --additional-properties hideGenerationTimestamp=true,generateSourceCodeOnly=true \
    --global-property apiTests=false,modelTests=false,modelDocs=false,apiDocs=false \
    --openapi-normalizer SET_TAGS_FOR_ALL_OPERATIONS=Thingsboard \
    2>&1 | if [ "$VERBOSE" = true ]; then cat; else grep -v \
      -e "^\[main\] INFO  o.o.codegen.*writing file" \
      -e "^\[main\] INFO  o.o.c.languages.*Processing operation" \
      -e "Unknown scheme.*loginPassword" \
      -e "Skipped by.*options supplied by user" \
      -e "^\[main\] INFO  o.o.c.DefaultGenerator"; fi

  if [ "$DRY_RUN" = true ]; then
    echo "Dry run: generated client is in $output_dir"
    echo "Skipping copy to package directory, common overlay, and post-processing."
  else
    # --- Copy generated package to edition directory (GEN-01/02/03/04) ---
    # With generateSourceCodeOnly=true, the package is directly in output_dir/tb_${edition}_client
    rm -rf "$module_dir/tb_${edition}_client"
    cp -r "$output_dir/tb_${edition}_client" "$module_dir/tb_${edition}_client"
    echo "Copied generated package to $module_dir/tb_${edition}_client"

    # --- Common module overlay (GEN-10) ---
    local common_dir="$SCRIPT_DIR/common"
    if [ -d "$common_dir" ] && [ -n "$(ls -A "$common_dir" 2>/dev/null)" ]; then
      cp -r "$common_dir/"* "$module_dir/tb_${edition}_client/"
      echo "Copied common module overlay to $module_dir/tb_${edition}_client"
    fi

    # --- Post-processing (GEN-06, GEN-07, GEN-08) ---
    echo "Running post-processor for $edition..."
    python3 "$SCRIPT_DIR/scripts/post_process.py" "$module_dir/tb_${edition}_client" "tb_${edition}_client"
  fi

  # --- Metrics output ---
  local pkg_dir
  if [ "$DRY_RUN" = true ]; then
    pkg_dir="$output_dir/tb_${edition}_client"
  else
    pkg_dir="$module_dir/tb_${edition}_client"
  fi

  if [ -d "$pkg_dir" ]; then
    echo ""
    echo "=== Metrics: $edition ==="
    local total_files
    total_files=$(find "$pkg_dir" -name "*.py" | wc -l | tr -d ' ')
    echo "  Python files: $total_files"

    local total_lines
    total_lines=$(find "$pkg_dir" -name "*.py" -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $1}')
    echo "  Total lines:  $total_lines"

    # API class file size and line count (look in api/ subdirectory specifically)
    local api_file
    api_file=$(find "$pkg_dir/api" -name "thingsboard_api.py" 2>/dev/null | head -1)
    if [ -n "$api_file" ]; then
      local api_lines api_size
      api_lines=$(wc -l < "$api_file" | tr -d ' ')
      api_size=$(wc -c < "$api_file" | tr -d ' ')
      echo "  API class:    $(basename "$api_file") — ${api_lines} lines, ${api_size} bytes"
    fi

    local model_count
    model_count=$(find "$pkg_dir" -path "*/models/*.py" -not -name "__init__.py" 2>/dev/null | wc -l | tr -d ' ')
    echo "  Models:       $model_count"

    # GEN-05: Verify Pydantic v2 patterns (native from generator)
    # Find a model with ConfigDict (confirms Pydantic v2 model_config usage)
    # Note: not all models import BaseModel directly (enum models, subclasses) so
    # we check for model_config = ConfigDict which is the definitive Pydantic v2 marker
    local sample_model
    sample_model=$(grep -rl "model_config = ConfigDict" "$pkg_dir/models" 2>/dev/null || true)
    sample_model=$(echo "$sample_model" | head -1)
    if [ -n "$sample_model" ]; then
      echo "  Pydantic v2:  OK (model_config = ConfigDict confirmed in $(basename "$sample_model"))"
    else
      # Fallback: check if any model imports from pydantic
      local pydantic_model
      pydantic_model=$(grep -rl "from pydantic import" "$pkg_dir/models" 2>/dev/null || true)
      pydantic_model=$(echo "$pydantic_model" | head -1)
      if [ -n "$pydantic_model" ]; then
        echo "  Pydantic v2:  OK (pydantic imports found in $(basename "$pydantic_model"))"
      else
        echo "  Pydantic v2:  WARNING — no Pydantic patterns found in models/"
      fi
    fi

    echo "  Import time:  time python3 -c \"import tb_${edition}_client\""
    echo ""
  fi
}

# -------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------
if [ "$EDITION" = "all" ]; then
  if [ -n "$BASE_URL" ]; then
    echo "Error: base-url is not supported with 'all'. Run per edition instead."
    exit 1
  fi
  for e in "${EDITIONS[@]}"; do
    generate "$e"
  done
else
  if [[ ! " ${EDITIONS[*]} " =~ " ${EDITION} " ]]; then
    echo "Error: unknown edition '$EDITION'. Must be one of: ${EDITIONS[*]} all"
    exit 1
  fi
  generate "$EDITION"
fi
