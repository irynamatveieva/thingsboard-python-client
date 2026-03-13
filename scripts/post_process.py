#!/usr/bin/env python3
"""Post-process generated OpenAPI client code.

Usage: python3 scripts/post_process.py <package_dir> <package_name>

Example: python3 scripts/post_process.py ce/tb_ce_client tb_ce_client

Steps performed:
  1. Strip generated OpenAPI comment blocks (# coding: utf-8 + docstring)
  2. Fix JsonNode/object references (broken imports, from_dict calls, to_dict calls)
  3. Rewrite __init__.py files for lazy imports (models/ and root)
  4. Apply Apache 2.0 license headers to all .py files
  5. Clean up unwanted generated files (README, setup.py, etc.)
"""

import importlib
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------
# License header template
# ---------------------------------------------------------------------------
LICENSE_HEADER = """\
#
# Copyright 2026 ThingsBoard, Inc.
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
"""

# ---------------------------------------------------------------------------
# Step 1: Strip generated OpenAPI comment blocks
# ---------------------------------------------------------------------------

# Pattern to match the generated header:
#   # coding: utf-8
#   <blank line(s)>
#   """
#       ThingsBoard REST API
#       ...
#   """
_CODING_HEADER_RE = re.compile(
    r'^# coding: utf-8\s*\n+"""[\s\S]*?"""\s*\n*',
    re.MULTILINE,
)


def strip_generated_comment_blocks(py_files: List[Path]) -> int:
    """Remove the '# coding: utf-8' + docstring header from generated files.

    Returns the number of files modified.
    """
    modified = 0
    for f in py_files:
        content = f.read_text(encoding="utf-8")
        new_content = _CODING_HEADER_RE.sub("", content, count=1)
        if new_content != content:
            f.write_text(new_content, encoding="utf-8")
            modified += 1
    return modified


# ---------------------------------------------------------------------------
# Step 2: Fix JsonNode/object references
# ---------------------------------------------------------------------------

# 2a: Remove broken import line
def _make_broken_import_pattern(package_name: str) -> re.Pattern:
    return re.compile(
        rf"^from {re.escape(package_name)}\.models\.object import object\n",
        re.MULTILINE,
    )


# 2b: Fix from_dict calls — two variants:
#   object.from_dict(obj["field"]) if obj.get("field") is not None else None
#   object.from_dict(obj['field']) if obj.get('field') is not None else None
_FROM_DICT_WITH_NONE_CHECK_RE = re.compile(
    r'object\.from_dict\(obj\[(["\'])(\w+)\1\]\)'
    r'\s*if\s+obj\.get\(\1\2\1\)\s+is\s+not\s+None\s+else\s+None',
    re.MULTILINE,
)

# Simpler form without None check
_FROM_DICT_SIMPLE_RE = re.compile(
    r'object\.from_dict\(obj\[(["\'])(\w+)\1\]\)',
    re.MULTILINE,
)


def _fix_from_dict(content: str) -> Tuple[str, int]:
    """Replace object.from_dict(...) patterns with obj.get(...)."""
    count = 0

    new_content, n = _FROM_DICT_WITH_NONE_CHECK_RE.subn(
        lambda m: f'obj.get({m.group(1)}{m.group(2)}{m.group(1)})',
        content,
    )
    count += n

    new_content, n = _FROM_DICT_SIMPLE_RE.subn(
        lambda m: f'obj.get({m.group(1)}{m.group(2)}{m.group(1)})',
        new_content,
    )
    count += n

    return new_content, count


# 2c: Fix to_dict calls on object-typed fields.
#
# When --schema-mappings JsonNode=object was used in older generator invocations,
# generated to_dict() methods would call self.field.to_dict() on Optional[object]
# fields (which have no .to_dict() method). Without that schema mapping, JsonNode
# fields become Optional[Any] and do NOT get .to_dict() overrides, so this step
# is a no-op for standard generation.
#
# We only fix to_dict calls where the field was ALSO fixed by from_dict() fix
# (same files, same fields), to avoid incorrectly stripping valid nested model
# .to_dict() calls (e.g. self.tenant_id.to_dict() where tenant_id is a Pydantic
# model — those are valid and should be preserved).
#
# Strategy: collect snake_case field names whose from_dict() was fixed, then
# only fix .to_dict() calls for those specific field names.
_TO_DICT_CALL_RE_TEMPLATE = r"(_dict\[['\"][^'\"]+['\"]\]\s*=\s*self\.{snake_field})\.to_dict\(\)"


def _fix_to_dict_for_fields(content: str, object_fields: list) -> Tuple[str, int]:
    """Remove .to_dict() suffix only for known object-typed fields."""
    count = 0
    for snake_field in object_fields:
        pattern = re.compile(
            _TO_DICT_CALL_RE_TEMPLATE.format(snake_field=re.escape(snake_field)),
            re.MULTILINE,
        )
        new_content, n = pattern.subn(r'\1', content)
        content = new_content
        count += n
    return content, count


def fix_jsonnode_references(
    models_dir: Path,
    package_name: str,
) -> Tuple[int, int, int]:
    """Apply all three JsonNode/object fixes to model files.

    Returns (import_removals, from_dict_fixes, to_dict_fixes).
    """
    if not models_dir.exists():
        return 0, 0, 0

    broken_import_re = _make_broken_import_pattern(package_name)
    import_removals = 0
    from_dict_fixes = 0
    to_dict_fixes = 0

    for f in sorted(models_dir.glob("*.py")):
        if f.name == "__init__.py":
            continue

        content = f.read_text(encoding="utf-8")
        original = content

        # 2a: remove broken import
        new_content, n = broken_import_re.subn("", content)
        import_removals += n

        # Clean up any resulting double blank lines
        if n:
            new_content = re.sub(r'\n{3,}', '\n\n', new_content)

        # 2b: fix from_dict calls — collect which field names were fixed
        #     so step 2c can target only those fields
        fixed_field_names: list = []
        _with_none = _FROM_DICT_WITH_NONE_CHECK_RE.findall(new_content)
        _simple = _FROM_DICT_SIMPLE_RE.findall(new_content)
        for _, field_name in _with_none:
            # Convert camelCase field name to snake_case for to_dict lookup
            snake = re.sub(r'(?<!^)(?=[A-Z])', '_', field_name).lower()
            fixed_field_names.append(snake)
        for _, field_name in _simple:
            snake = re.sub(r'(?<!^)(?=[A-Z])', '_', field_name).lower()
            if snake not in fixed_field_names:
                fixed_field_names.append(snake)

        new_content, n = _fix_from_dict(new_content)
        from_dict_fixes += n

        # 2c: fix to_dict calls ONLY for object-typed fields (identified above)
        if fixed_field_names:
            new_content, n = _fix_to_dict_for_fields(new_content, fixed_field_names)
            to_dict_fixes += n

        if new_content != original:
            f.write_text(new_content, encoding="utf-8")

    return import_removals, from_dict_fixes, to_dict_fixes


# ---------------------------------------------------------------------------
# Step 3: Rewrite __init__.py files for lazy imports
# ---------------------------------------------------------------------------

def _collect_model_classes(models_dir: Path, package_name: str) -> Dict[str, str]:
    """Scan model .py files and build {ClassName: "package.models.module"} mapping."""
    model_map: Dict[str, str] = {}

    for py_file in sorted(models_dir.glob("*.py")):
        if py_file.name == "__init__.py":
            continue

        module_name = py_file.stem

        # Skip the broken 'object' pseudo-module
        if module_name == "object":
            continue

        content = py_file.read_text(encoding="utf-8")
        for match in re.finditer(r"^class (\w+)\(", content, re.MULTILINE):
            class_name = match.group(1)
            model_map[class_name] = f"{package_name}.models.{module_name}"

    # Remove 'object' key if it somehow snuck in (JsonNode artifact)
    model_map.pop("object", None)

    return model_map


def _collect_api_classes(api_dir: Path, package_name: str) -> Dict[str, str]:
    """Scan api/*.py files and build {ClassName: "package.api.module"} mapping.

    Matches both ``class Foo(Bar):`` and ``class Foo:`` definitions because
    the OpenAPI generator emits API classes without a base class (no parentheses).
    """
    api_map: Dict[str, str] = {}

    for py_file in sorted(api_dir.glob("*.py")):
        if py_file.name == "__init__.py":
            continue

        module_name = py_file.stem
        content = py_file.read_text(encoding="utf-8")
        # Match "class Foo:" or "class Foo(Bar):" — API classes have no base class
        for match in re.finditer(r"^class (\w+)[:(]", content, re.MULTILINE):
            cls_name = match.group(1)
            api_map[cls_name] = f"{package_name}.api.{module_name}"

    return api_map


def _generate_models_init(package_name: str, model_map: Dict[str, str]) -> str:
    """Generate lazy-loading models/__init__.py content."""
    sorted_items = sorted(model_map.items())

    lines = [
        "import importlib",
        "from typing import TYPE_CHECKING",
        "",
        f"__all__ = [",
    ]
    for cls_name, _ in sorted_items:
        lines.append(f'    "{cls_name}",')
    lines.append("]")
    lines.append("")

    # TYPE_CHECKING block for IDE support
    lines.append("if TYPE_CHECKING:")
    for cls_name, mod_path in sorted_items:
        lines.append(f"    from {mod_path} import {cls_name}")
    lines.append("")

    # Lazy mapping dict
    lines.append("_MODEL_CLASSES = {")
    for cls_name, mod_path in sorted_items:
        lines.append(f'    "{cls_name}": "{mod_path}",')
    lines.append("}")
    lines.append("")

    # __getattr__ for lazy loading
    lines.extend([
        "def __getattr__(name: str):",
        "    if name in _MODEL_CLASSES:",
        "        module = importlib.import_module(_MODEL_CLASSES[name])",
        "        cls = getattr(module, name)",
        "        globals()[name] = cls  # Cache for subsequent access",
        "        return cls",
        '    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")',
        "",
        "def __dir__():",
        "    return list(_MODEL_CLASSES.keys())",
        "",
    ])

    return "\n".join(lines)


def _generate_api_init(package_name: str, api_map: Dict[str, str]) -> str:
    """Generate lazy-loading api/__init__.py content."""
    sorted_items = sorted(api_map.items())

    lines = [
        "import importlib",
        "from typing import TYPE_CHECKING",
        "",
        "__all__ = [",
    ]
    for cls_name, _ in sorted_items:
        lines.append(f'    "{cls_name}",')
    lines.append("]")
    lines.append("")

    # TYPE_CHECKING block for IDE support
    lines.append("if TYPE_CHECKING:")
    for cls_name, mod_path in sorted_items:
        lines.append(f"    from {mod_path} import {cls_name}")
    lines.append("")

    # Lazy mapping dict
    lines.append("_API_CLASSES = {")
    for cls_name, mod_path in sorted_items:
        lines.append(f'    "{cls_name}": "{mod_path}",')
    lines.append("}")
    lines.append("")

    # __getattr__ for lazy loading
    lines.extend([
        "def __getattr__(name: str):",
        "    if name in _API_CLASSES:",
        "        module = importlib.import_module(_API_CLASSES[name])",
        "        cls = getattr(module, name)",
        "        globals()[name] = cls  # Cache for subsequent access",
        "        return cls",
        '    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")',
        "",
        "def __dir__():",
        "    return list(_API_CLASSES.keys())",
        "",
    ])

    return "\n".join(lines)


def _generate_root_init(
    package_name: str,
    model_map: Dict[str, str],
    api_map: Dict[str, str],
) -> str:
    """Generate lazy-loading root __init__.py content.

    Keeps eager imports for small essential runtime classes:
      - ApiClient, Configuration, exceptions, ApiResponse, ThingsboardClient
    Uses __getattr__ lazy loading for all controller classes and models.
    """
    sorted_models = sorted(model_map.items())
    sorted_api = sorted(api_map.items())

    lines = [
        "import importlib",
        "from typing import TYPE_CHECKING",
        "",
        "# Eager imports — small, always needed at runtime",
        f"from {package_name}.api_client import ApiClient",
        f"from {package_name}.configuration import Configuration",
        f"from {package_name}.api_response import ApiResponse",
        f"from {package_name}.exceptions import (",
        "    OpenApiException,",
        "    ApiAttributeError,",
        "    ApiTypeError,",
        "    ApiValueError,",
        "    ApiKeyError,",
        "    ApiException,",
        ")",
        "# Common module — handwritten client wrapper",
        "try:",
        f"    from {package_name}.client import ThingsboardClient",
        "    __all__ = ['ThingsboardClient']",
        "except ImportError:",
        "    pass",
        "",
        "if TYPE_CHECKING:",
    ]

    # Controller class imports for IDE (sorted)
    for cls_name, mod_path in sorted_api:
        lines.append(f"    from {mod_path} import {cls_name}")

    # Model imports for IDE
    for cls_name, mod_path in sorted_models:
        lines.append(f"    from {mod_path} import {cls_name}")

    lines.append("")

    # Lazy mapping — all controllers first (sorted), then all models (sorted)
    lines.append("_LAZY_CLASSES = {")
    for cls_name, mod_path in sorted_api:
        lines.append(f'    "{cls_name}": "{mod_path}",')
    for cls_name, mod_path in sorted_models:
        lines.append(f'    "{cls_name}": "{mod_path}",')
    lines.append("}")
    lines.append("")

    lines.extend([
        "def __getattr__(name: str):",
        "    if name in _LAZY_CLASSES:",
        "        module = importlib.import_module(_LAZY_CLASSES[name])",
        "        obj = getattr(module, name)",
        "        globals()[name] = obj  # Cache for subsequent access",
        "        return obj",
        '    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")',
        "",
        "def __dir__():",
        "    return list(_LAZY_CLASSES.keys()) + [",
        '        "ApiClient", "Configuration", "ApiResponse",',
        '        "OpenApiException", "ApiAttributeError", "ApiTypeError",',
        '        "ApiValueError", "ApiKeyError", "ApiException",',
        '        "ThingsboardClient",',
        "    ]",
        "",
    ])

    return "\n".join(lines)


def rewrite_init_files(package_dir: Path, package_name: str) -> Tuple[int, int]:
    """Rewrite __init__.py files for lazy loading.

    Returns (model_count, api_count) tuple.
    """
    models_dir = package_dir / "models"
    api_dir = package_dir / "api"

    if not models_dir.exists():
        print(f"  Warning: models/ directory not found in {package_dir}, skipping lazy import rewrite")
        return 0, 0

    model_map = _collect_model_classes(models_dir, package_name)
    api_map = _collect_api_classes(api_dir, package_name) if api_dir.exists() else {}

    # Rewrite models/__init__.py
    models_init = models_dir / "__init__.py"
    models_init.write_text(_generate_models_init(package_name, model_map), encoding="utf-8")

    # Rewrite api/__init__.py with lazy loading (if api/ exists)
    if api_dir.exists():
        api_init = api_dir / "__init__.py"
        api_init.write_text(_generate_api_init(package_name, api_map), encoding="utf-8")

    # Rewrite root __init__.py (passes api_map, not hard-coded ThingsboardApi)
    root_init = package_dir / "__init__.py"
    root_init.write_text(_generate_root_init(package_name, model_map, api_map), encoding="utf-8")

    return len(model_map), len(api_map)


# ---------------------------------------------------------------------------
# Step 4: Apply Apache 2.0 license headers
# ---------------------------------------------------------------------------

def apply_license_headers(py_files: List[Path]) -> int:
    """Prepend LICENSE_HEADER to each .py file that doesn't already have it.

    Returns the number of files modified.
    """
    modified = 0
    # The first meaningful line of the header (after the blank line guard)
    header_check = "# Copyright 2026 ThingsBoard, Inc."

    for f in py_files:
        content = f.read_text(encoding="utf-8")
        # Skip if already has the license header
        if header_check in content[:200]:
            continue
        f.write_text(LICENSE_HEADER + content, encoding="utf-8")
        modified += 1
    return modified


# ---------------------------------------------------------------------------
# Step 5: Clean up unwanted generated files
# ---------------------------------------------------------------------------

def cleanup_generated_files(package_dir: Path) -> List[str]:
    """Remove files that the generator creates but we don't want.

    Returns list of removed file paths.
    """
    removed: List[str] = []
    parent = package_dir.parent

    # {package_dir}_README.md (e.g., tb_ce_client_README.md one level up)
    readme_candidate = parent / f"{package_dir.name}_README.md"
    if readme_candidate.exists():
        readme_candidate.unlink()
        removed.append(str(readme_candidate))

    # setup.py, setup.cfg, tox.ini in parent (shouldn't exist with
    # generateSourceCodeOnly, but be defensive).
    # NOTE: pyproject.toml is intentionally excluded — each edition directory
    # now contains a pyproject.toml for Poetry packaging (Phase 3).
    for artifact in ("setup.py", "setup.cfg", "tox.ini"):
        candidate = parent / artifact
        if candidate.exists():
            candidate.unlink()
            removed.append(str(candidate))

    # py.typed marker — Phase 3 will add this properly
    py_typed = package_dir / "py.typed"
    if py_typed.exists():
        py_typed.unlink()
        removed.append(str(py_typed))

    return removed


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main(package_dir: Path, package_name: str) -> None:
    """Run all post-processing steps on the generated package."""
    if not package_dir.exists():
        print(f"Error: package directory does not exist: {package_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Post-processing: {package_dir} (package: {package_name})")

    # Collect all .py files recursively
    all_py_files = sorted(package_dir.rglob("*.py"))
    models_dir = package_dir / "models"
    model_py_files = sorted(models_dir.glob("*.py")) if models_dir.exists() else []

    print(f"  Found {len(all_py_files)} .py files total")

    # -------------------------------------------------------------------
    # Step 1: Strip generated comment blocks
    # -------------------------------------------------------------------
    stripped = strip_generated_comment_blocks(all_py_files)
    print(f"  Step 1 — Stripped generated comment blocks: {stripped} files")

    # -------------------------------------------------------------------
    # Step 2: Fix JsonNode/object references
    # -------------------------------------------------------------------
    if models_dir.exists():
        import_removals, from_dict_fixes, to_dict_fixes = fix_jsonnode_references(
            models_dir, package_name
        )
        print(
            f"  Step 2 — JsonNode fixes: "
            f"{import_removals} broken imports removed, "
            f"{from_dict_fixes} from_dict() calls fixed, "
            f"{to_dict_fixes} to_dict() calls fixed"
        )
    else:
        print("  Step 2 — Skipped (no models/ directory)")
        import_removals, from_dict_fixes, to_dict_fixes = 0, 0, 0

    # -------------------------------------------------------------------
    # Step 3: Rewrite __init__.py files for lazy imports
    # -------------------------------------------------------------------
    model_count, api_count = rewrite_init_files(package_dir, package_name)
    print(f"  Step 3 — Lazy import rewrite: {model_count} models, {api_count} controllers mapped")

    # -------------------------------------------------------------------
    # Step 4: Apply license headers
    # -------------------------------------------------------------------
    # Re-collect files after rewrites (init files changed)
    all_py_files = sorted(package_dir.rglob("*.py"))
    headers_applied = apply_license_headers(all_py_files)
    print(f"  Step 4 — License headers applied: {headers_applied} files")

    # -------------------------------------------------------------------
    # Step 5: Clean up unwanted generated files
    # -------------------------------------------------------------------
    removed = cleanup_generated_files(package_dir)
    if removed:
        print(f"  Step 5 — Cleaned up {len(removed)} files:")
        for path in removed:
            print(f"    - {path}")
    else:
        print("  Step 5 — No unwanted files to clean up")

    # -------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------
    total_py = len(sorted(package_dir.rglob("*.py")))
    print()
    print(f"  === Post-processing summary for {package_name} ===")
    print(f"  Total .py files:       {total_py}")
    print(f"  Comment blocks stripped: {stripped}")
    print(f"  JsonNode fixes:")
    print(f"    Broken imports removed: {import_removals}")
    print(f"    from_dict() fixed:      {from_dict_fixes}")
    print(f"    to_dict() fixed:        {to_dict_fixes}")
    print(f"  Lazy import models:    {model_count}")
    print(f"  Lazy import controllers: {api_count}")
    print(f"  License headers added: {headers_applied}")
    print(f"  Files cleaned up:      {len(removed)}")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        print("Error: expected exactly 2 arguments: <package_dir> <package_name>", file=sys.stderr)
        sys.exit(1)

    package_dir_arg = Path(sys.argv[1])
    package_name_arg = sys.argv[2]
    main(package_dir_arg, package_name_arg)
