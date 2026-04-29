#!/usr/bin/env python3
#
# Copyright © 2026-2026 ThingsBoard, Inc.
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
"""Apply Apache 2.0 license headers to hand-written source files.

The post_process.py pipeline already handles generated client packages
(tb_*_client/). This script covers the gap: hand-written Python under
common/ and scripts/ that ships in the published wheels (via the
generate-client.sh overlay) or sits alongside generated code.

Idempotent: re-running is a no-op for files that already carry a header.

Usage:
    python3 scripts/apply-license-headers.py [--check]

    --check: exit non-zero if any file would be modified (no writes).
             Suitable as a CI gate.
"""

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from post_process import LICENSE_HEADER  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parent

# Directories whose .py files must carry the header.
# common/ ships in the wheels via overlay; scripts/ sits next to the shell
# scripts that already carry the header — keep them consistent.
TARGET_DIRS = [
    REPO_ROOT / "common",
    REPO_ROOT / "scripts",
]

# Files inside the target dirs to skip (this script itself is fine to header,
# but tests/ and __pycache__ are excluded by directory choice).
EXCLUDE_NAMES = {"__pycache__"}


def has_header(content: str) -> bool:
    head = content[:200]
    return "# Copyright" in head and "ThingsBoard" in head


def insert_header(content: str) -> str:
    """Prepend LICENSE_HEADER, preserving a shebang line if present."""
    if content.startswith("#!"):
        newline = content.find("\n")
        if newline != -1:
            shebang = content[: newline + 1]
            rest = content[newline + 1 :]
            return shebang + LICENSE_HEADER + rest
    return LICENSE_HEADER + content


def iter_targets() -> list[Path]:
    files: list[Path] = []
    for d in TARGET_DIRS:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.py")):
            if any(part in EXCLUDE_NAMES for part in path.parts):
                continue
            files.append(path)
    return files


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    files = iter_targets()
    needs_update: list[Path] = []
    updated = 0

    for f in files:
        content = f.read_text(encoding="utf-8")
        if has_header(content):
            continue
        needs_update.append(f)
        if check_only:
            continue
        f.write_text(insert_header(content), encoding="utf-8")
        updated += 1

    if check_only:
        if needs_update:
            print("Missing license header in:")
            for f in needs_update:
                print(f"  {f.relative_to(REPO_ROOT)}")
            return 1
        print(f"License headers OK ({len(files)} files checked).")
        return 0

    print(f"License headers applied to {updated} files (checked {len(files)}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
