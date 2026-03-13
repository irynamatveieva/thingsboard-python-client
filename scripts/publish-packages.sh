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
# Uploads all three ThingsBoard client packages to TestPyPI or PyPI via twine.
#
# NOTE: Credentials are read from ~/.pypirc. Configure it with:
#
#   [distutils]
#   index-servers =
#       pypi
#       testpypi
#
#   [pypi]
#   username = __token__
#   password = pypi-<your-api-token>
#
#   [testpypi]
#   repository = https://test.pypi.org/legacy/
#   username = __token__
#   password = pypi-<your-testpypi-api-token>
#
# IMPORTANT: Use twine (not poetry publish) — Poetry does not read ~/.pypirc.
#
# Usage:
#   ./scripts/publish-packages.sh [testpypi|pypi]
#
# Arguments:
#   testpypi   Upload to TestPyPI (default — safe to run anytime)
#   pypi       Upload to PyPI (production — permanent)
#
# Examples:
#   ./scripts/publish-packages.sh             # Upload to TestPyPI
#   ./scripts/publish-packages.sh testpypi    # Upload to TestPyPI (explicit)
#   ./scripts/publish-packages.sh pypi        # Upload to PyPI (production)
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$SCRIPT_DIR/.."
DIST_DIR="$ROOT_DIR/dist"

# Parse argument — default to testpypi for safety
REPO="${1:-testpypi}"

# Validate argument
if [ "$REPO" != "testpypi" ] && [ "$REPO" != "pypi" ]; then
    echo "Usage: $0 [testpypi|pypi]"
    echo ""
    echo "  testpypi  Upload to https://test.pypi.org/ (default)"
    echo "  pypi      Upload to https://pypi.org/ (production)"
    exit 1
fi

# Check dist/ has wheels
if ! ls "${DIST_DIR}"/*.whl > /dev/null 2>&1; then
    echo "ERROR: No wheels found in dist/. Run scripts/build-packages.sh first."
    exit 1
fi

# Check twine is available
if ! command -v twine > /dev/null 2>&1; then
    echo "ERROR: twine not found. Install with: pip install twine"
    exit 1
fi

# List what will be uploaded
echo "=== Publishing to ${REPO} ==="
echo ""
echo "Artifacts to upload:"
ls -lh "${DIST_DIR}"/*.whl "${DIST_DIR}"/*.tar.gz 2>/dev/null
echo ""

# Upload via twine (reads credentials from ~/.pypirc)
twine upload --repository "${REPO}" "${DIST_DIR}"/*.whl "${DIST_DIR}"/*.tar.gz

echo ""
echo "=== Upload complete ==="
echo ""
if [ "$REPO" = "testpypi" ]; then
    echo "Install from TestPyPI:"
    echo "  pip install --index-url https://test.pypi.org/simple/ tb-ce-client"
    echo "  pip install --index-url https://test.pypi.org/simple/ tb-pe-client"
    echo "  pip install --index-url https://test.pypi.org/simple/ tb-paas-client"
else
    echo "Install from PyPI:"
    echo "  pip install tb-ce-client"
    echo "  pip install tb-pe-client"
    echo "  pip install tb-paas-client"
fi
