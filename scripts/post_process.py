#!/usr/bin/env python3
"""Post-process generated OpenAPI client code.

Usage: python3 scripts/post_process.py <package_dir> <package_name>

Example: python3 scripts/post_process.py ce/tb_ce_client tb_ce_client

Steps performed:
  1. Strip generated OpenAPI comment blocks (# coding: utf-8 + docstring)
  2. Fix JsonNode/object references (broken imports, from_dict calls, to_dict calls)
  2a. Convert alias= to serialization_alias= for PEP 8 __init__ signatures
  2b. Add __str__/__repr__ to models and get_id() to EntityId
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
# Step 2a: Convert alias= to serialization_alias= (PEP 8 __init__ params)
# ---------------------------------------------------------------------------

# Match alias="..." in Field() definitions, but NOT by_alias=
_FIELD_ALIAS_RE = re.compile(r'(?<![a-z_])alias="([^"]+)"')

# Fix to_json(): replace json.dumps(self.to_dict()) with model_dump_json()
_TO_JSON_OLD = '        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead\n        return json.dumps(self.to_dict())'
_TO_JSON_NEW = '        return self.model_dump_json(by_alias=True, exclude_unset=True)'


def _camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def _build_alias_map(content: str) -> Dict[str, str]:
    """Build a mapping from serialization_alias value to Python field name.

    Scans field declarations like:
        var_from: ... = Field(..., serialization_alias="from")
    and returns {"from": "var_from"}.
    """
    alias_map: Dict[str, str] = {}
    for m in re.finditer(
        r'^\s+(\w+)\s*:.*serialization_alias="([^"]+)"', content, re.MULTILINE
    ):
        field_name, alias = m.group(1), m.group(2)
        if field_name != alias:
            alias_map[alias] = field_name
    return alias_map


def _convert_model_validate_keys(content: str) -> Tuple[str, int]:
    """Convert camelCase dict keys to snake_case inside model_validate({...}) blocks.

    Also handles reserved-word renames (e.g. "from" → "var_from") by reading
    serialization_alias= declarations from the same file.

    Only converts the dict-key position (first quoted string before ':' on each line
    inside the block). Preserves camelCase in obj["key"] and obj.get("key") on the
    right-hand side.
    """
    alias_map = _build_alias_map(content)
    count = 0

    def _process_block(block_match: re.Match) -> str:
        nonlocal count
        block = block_match.group(0)

        def _convert_key(key_match: re.Match) -> str:
            nonlocal count
            prefix = key_match.group(1)
            key = key_match.group(2)
            suffix = key_match.group(3)
            # Reserved-word rename takes priority, then camelCase→snake_case
            if key in alias_map:
                new_key = alias_map[key]
            else:
                new_key = _camel_to_snake(key)
            if new_key != key:
                count += 1
            return f'{prefix}"{new_key}"{suffix}'

        # Match dict keys: leading whitespace + "key" + colon
        return re.sub(r'(\n\s+)"(\w+)"(\s*:)', _convert_key, block)

    new_content = re.sub(
        r'cls\.model_validate\(\{.*?\}\)',
        _process_block,
        content,
        flags=re.DOTALL,
    )
    return new_content, count


def convert_field_aliases(models_dir: Path) -> Tuple[int, int]:
    """Convert alias= to serialization_alias= and fix from_dict() keys.

    This makes model __init__ signatures use snake_case parameter names
    (PEP 8 compliant) while keeping camelCase for JSON serialization.

    Returns (alias_conversions, from_dict_key_fixes).
    """
    if not models_dir.exists():
        return 0, 0

    alias_conversions = 0
    key_fixes = 0

    for f in sorted(models_dir.glob("*.py")):
        if f.name == "__init__.py":
            continue

        content = f.read_text(encoding="utf-8")
        original = content

        # Fix to_json(): use model_dump_json() instead of json.dumps(to_dict())
        content = content.replace(_TO_JSON_OLD, _TO_JSON_NEW)

        # Convert alias= to serialization_alias= (skip if already done)
        if 'serialization_alias=' not in content:
            new_content, n = _FIELD_ALIAS_RE.subn(r'serialization_alias="\1"', content)
            alias_conversions += n
            content = new_content

            # Convert model_validate dict keys from camelCase to snake_case
            content, n = _convert_model_validate_keys(content)
            key_fixes += n

        if content != original:
            f.write_text(content, encoding="utf-8")

    return alias_conversions, key_fixes


# ---------------------------------------------------------------------------
# Step 2b: Add __str__/__repr__ to models and get_id() to EntityId
# ---------------------------------------------------------------------------

_TO_STR_RETURN_OLD = "        return pprint.pformat(self.model_dump(by_alias=True))"
_TO_STR_RETURN_NEW = "        return pprint.pformat(self.model_dump(by_alias=False, mode='json'))"
_TO_STR_DOC_OLD = '"""Returns the string representation of the model using alias"""'
_TO_STR_DOC_NEW = '"""Returns the string representation of the model"""'
# oneOf union models use a different to_str() pattern (no by_alias arg)
_TO_STR_ONEOF_OLD = "        return pprint.pformat(self.model_dump())"
_TO_STR_ONEOF_NEW = "        return pprint.pformat(self.model_dump(mode='json'))"

_MODEL_STR_METHODS = '''
    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()
'''

_ENTITY_ID_METHODS = '''
    def get_id(self) -> str:
        """Returns the entity ID as a string."""
        return str(self.id)

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(entity_type={self.entity_type.value!r}, id={str(self.id)!r})"
'''

# For ID classes that extend BaseModel directly (EventId, AuditLogId, etc.)
# — they have id: UUID but no entity_type field.
_BASEMODEL_ID_METHODS = '''
    def get_id(self) -> str:
        """Returns the entity ID as a string."""
        return str(self.id)

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(id={str(self.id)!r})"
'''


def _is_entity_id_subclass(content: str) -> bool:
    """Check if a model file defines a class that extends EntityId."""
    return bool(re.search(r'^class \w+\(EntityId\):', content, re.MULTILINE))


def _is_basemodel_id_class(content: str) -> bool:
    """Check if a model file defines an Id class that extends BaseModel directly."""
    return bool(re.search(r'^class \w+Id\(BaseModel\):', content, re.MULTILINE))


def add_model_str_methods(models_dir: Path) -> Tuple[int, int, int]:
    """Add __str__/__repr__ to models and get_id() to EntityId.

    - Changes to_str() output from camelCase to snake_case with JSON-safe
      serialization (by_alias=False, mode='json')
    - Adds __str__/__repr__ to regular models (delegating to to_str())
    - Adds get_id(), __str__, __repr__ to EntityId base class
    - EntityId subclasses inherit from EntityId, so no injection needed
    - BaseModel ID classes (EventId, AuditLogId, etc.) get their own
      get_id(), __str__, __repr__ since they can't inherit from EntityId

    Returns (to_str_fixes, str_injections, entity_id_patched).
    """
    if not models_dir.exists():
        return 0, 0, 0

    to_str_fixes = 0
    str_injections = 0
    entity_id_patched = 0

    for f in sorted(models_dir.glob("*.py")):
        if f.name == "__init__.py":
            continue

        content = f.read_text(encoding="utf-8")
        original = content

        # Skip if already patched
        if 'def __str__(self)' in content:
            continue

        # Fix to_str(): by_alias=True -> by_alias=False, mode='json'
        if _TO_STR_RETURN_OLD in content:
            content = content.replace(_TO_STR_RETURN_OLD, _TO_STR_RETURN_NEW, 1)
            content = content.replace(_TO_STR_DOC_OLD, _TO_STR_DOC_NEW, 1)
            to_str_fixes += 1
        elif _TO_STR_ONEOF_OLD in content:
            # oneOf union models use model_dump() without by_alias
            content = content.replace(_TO_STR_ONEOF_OLD, _TO_STR_ONEOF_NEW, 1)
            to_str_fixes += 1

        is_entity_id_file = f.name == 'entity_id.py'
        is_entity_id_sub = _is_entity_id_subclass(content)
        is_basemodel_id = _is_basemodel_id_class(content)

        if is_entity_id_file:
            # Inject get_id(), __str__, __repr__ for EntityId base class
            content = content.replace(
                _TO_STR_RETURN_NEW + '\n',
                _TO_STR_RETURN_NEW + '\n' + _ENTITY_ID_METHODS,
                1,
            )
            entity_id_patched = 1
            str_injections += 1
        elif is_entity_id_sub:
            # EntityId subclasses inherit __str__/__repr__ from base — skip
            pass
        elif is_basemodel_id:
            # BaseModel ID classes (EventId, AuditLogId, etc.)
            content = content.replace(
                _TO_STR_RETURN_NEW + '\n',
                _TO_STR_RETURN_NEW + '\n' + _BASEMODEL_ID_METHODS,
                1,
            )
            str_injections += 1
        else:
            # Regular models (including oneOf unions): inject __str__ and __repr__
            for anchor in (_TO_STR_RETURN_NEW, _TO_STR_ONEOF_NEW):
                if anchor in content:
                    content = content.replace(
                        anchor + '\n',
                        anchor + '\n' + _MODEL_STR_METHODS,
                        1,
                    )
                    str_injections += 1
                    break

        if content != original:
            f.write_text(content, encoding="utf-8")

    return to_str_fixes, str_injections, entity_id_patched


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


# ---------------------------------------------------------------------------
# Step 6: Generate _controller_map.py
# ---------------------------------------------------------------------------

def _generate_controller_map(api_dir: Path, package_name: str) -> "Tuple[str, int, int]":
    """Scan api/*.py files and generate _controller_map.py content.

    Builds two dicts:
      _CONTROLLER_MAP:      {method_name: (module_path, cls_name)} for every public method
      _CONTROLLER_ATTR_MAP: {short_name: (module_path, cls_name)} for each controller class

    Short-name derivation: camelCase -> snake_case, strip trailing "_api" suffix.
    e.g. DeviceControllerApi -> device_controller_api -> device_controller

    Returns (file_content, method_count, controller_count).
    """
    method_map: "Dict[str, Tuple[str, str]]" = {}
    attr_map: "Dict[str, Tuple[str, str]]" = {}

    for py_file in sorted(api_dir.glob("*.py")):
        if py_file.name == "__init__.py":
            continue

        content = py_file.read_text(encoding="utf-8")
        cls_match = re.search(r"^class (\w+)[:(]", content, re.MULTILINE)
        if not cls_match:
            continue

        cls_name = cls_match.group(1)
        module_path = f"{package_name}.api.{py_file.stem}"

        # Short name: camelCase -> snake_case, strip trailing _api (4 chars)
        short_name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", cls_name).lower()
        if short_name.endswith("_api"):
            short_name = short_name[:-4]

        attr_map[short_name] = (module_path, cls_name)

        # Collect all public methods (exclude __init__)
        methods = re.findall(r"^    def ([a-zA-Z][a-zA-Z0-9_]*)\(", content, re.MULTILINE)
        for method_name in methods:
            if method_name == "__init__":
                continue
            method_map[method_name] = (module_path, cls_name)

    # Generate file content
    lines = [
        "# Generated by post_process.py -- do not edit manually.",
        "",
        "_CONTROLLER_MAP = {",
    ]
    for method_name, (module_path, cls_name) in sorted(method_map.items()):
        lines.append(f'    "{method_name}": ("{module_path}", "{cls_name}"),')
    lines.append("}")
    lines.append("")
    lines.append("_CONTROLLER_ATTR_MAP = {")
    for short_name, (module_path, cls_name) in sorted(attr_map.items()):
        lines.append(f'    "{short_name}": ("{module_path}", "{cls_name}"),')
    lines.append("}")
    lines.append("")

    file_content = "\n".join(lines)
    return file_content, len(method_map), len(attr_map)


# ---------------------------------------------------------------------------
# Step 7: Generate client.pyi type stub
# ---------------------------------------------------------------------------

def _extract_method_signatures(content: str) -> "List[Tuple[str, str, str]]":
    """Extract all public instance method signatures from a Python source file.

    Returns a list of (method_name, params_str, return_type_str) tuples.
    Skips __init__.

    For multi-line signatures (with nested brackets in Tuple[...], Dict[...]),
    we use a paren-depth scanner to find the complete parameter block.
    """
    results = []

    # Find all method definitions at 4-space indent (instance methods)
    # We scan for "    def method_name(" positions
    method_start_re = re.compile(r"^    def ([a-zA-Z_][a-zA-Z0-9_]*)\(", re.MULTILINE)

    for m in method_start_re.finditer(content):
        method_name = m.group(1)
        if method_name == "__init__":
            continue

        # Start scanning from the opening paren
        paren_start = m.start() + m.group(0).index("(")
        pos = paren_start + 1
        depth = 1
        length = len(content)

        # Walk forward until we close the parameter paren (handling nesting)
        while pos < length and depth > 0:
            ch = content[pos]
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            pos += 1

        # pos is now just past the closing ")"
        params_inner = content[paren_start + 1:pos - 1]

        # Now look for return type annotation "-> RetType" up to ":"
        rest = content[pos:]
        ret_match = re.match(r"\s*->\s*([^:\n]+?)\s*:", rest, re.DOTALL)
        return_type = ret_match.group(1).strip() if ret_match else "Any"

        # Strip whitespace/newlines from params to build a clean stub
        # Replace default values with ... (Ellipsis notation for .pyi)
        params_clean = _clean_params_for_stub(params_inner)

        results.append((method_name, params_clean, return_type))

    return results


def _clean_params_for_stub(params: str) -> str:
    """Clean up a parameter string for use in a .pyi stub.

    - Collapse whitespace/newlines to single spaces
    - Replace default values (= something) with = ...
    - Preserve type annotations
    """
    # Collapse all whitespace sequences to single space
    cleaned = re.sub(r"\s+", " ", params).strip()

    # Replace default values: "= <value>" -> "= ..."
    # We handle this by finding "= " not followed by "..." and replacing the value
    # This is tricky because default values can be complex (e.g. = None, = 0, = True)
    # Strategy: use a simple state-machine approach - split by comma at depth 0,
    # then process each param
    result_params = []
    # Split parameters by comma at depth 0
    parts = _split_at_depth_zero(cleaned)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Find "= value" at the end of the param (at depth 0)
        # If param has a default, replace with "= ..."
        param_with_ellipsis = _replace_default_value(part)
        result_params.append(param_with_ellipsis)

    return ", ".join(result_params)


def _split_at_depth_zero(s: str) -> "List[str]":
    """Split string by commas at bracket depth 0."""
    parts = []
    depth = 0
    current = []
    for ch in s:
        if ch in "([{":
            depth += 1
            current.append(ch)
        elif ch in ")]}":
            depth -= 1
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current))
    return parts


def _replace_default_value(param: str) -> str:
    """Replace a parameter's default value with '...' for .pyi stubs.

    E.g. 'x: int = 0' -> 'x: int = ...'
         'y = None'    -> 'y = ...'
    Leaves params with no default unchanged.
    """
    # Find the position of "=" at depth 0
    depth = 0
    for i, ch in enumerate(param):
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        elif ch == "=" and depth == 0:
            # Make sure it's not "=="
            if i + 1 < len(param) and param[i + 1] == "=":
                continue
            # Check it's not preceded by !, <, > (comparison operators)
            if i > 0 and param[i - 1] in "!<>":
                continue
            # Replace everything from "= " to end with "= ..."
            return param[:i].rstrip() + " = ..."
    return param


def _generate_client_pyi(
    api_dir: Path, package_name: str, client_py_path: Path
) -> "Tuple[str, int]":
    """Generate client.pyi type stub content.

    Extracts method signatures from all controller files and builds a .pyi
    stub declaring every delegated method so IDEs can provide autocompletion.

    Returns (pyi_content, stub_count).
    """
    # Collect all controller classes and their methods
    controller_classes: "List[Tuple[str, str, str, List[Tuple[str, str, str]]]]" = []
    # (short_name, cls_name, module_path, [(method_name, params, return_type), ...])

    for py_file in sorted(api_dir.glob("*.py")):
        if py_file.name == "__init__.py":
            continue

        content = py_file.read_text(encoding="utf-8")
        cls_match = re.search(r"^class (\w+)[:(]", content, re.MULTILINE)
        if not cls_match:
            continue

        cls_name = cls_match.group(1)
        module_path = f"{package_name}.api.{py_file.stem}"

        # Derive short name (same as _generate_controller_map)
        short_name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", cls_name).lower()
        if short_name.endswith("_api"):
            short_name = short_name[:-4]

        methods = _extract_method_signatures(content)
        controller_classes.append((short_name, cls_name, module_path, methods))

    # Build the .pyi content
    lines = [
        f"# {package_name}/client.pyi  (GENERATED -- do not edit manually)",
        "from typing import Optional, Union, Tuple, Dict, Any, List",
        "from typing_extensions import Annotated",
        "from pydantic import Field, StrictStr, StrictInt, StrictFloat, StrictBool",
        "",
        f"from {package_name}.api_client import ApiClient",
        "",
        "# Controller class imports",
    ]
    for short_name, cls_name, module_path, _methods in controller_classes:
        lines.append(f"from {module_path} import {cls_name}")

    lines.extend([
        "",
        f"from {package_name}.models import *  # noqa: F401, F403",
        "",
        "class ThingsboardClient:",
        "    api_client: ApiClient",
        "    _controllers: dict",
        "    _auth_manager: Any",
        "",
        "    def __init__(",
        "        self,",
        "        url: str,",
        "        username: Optional[str] = ...,",
        "        password: Optional[str] = ...,",
        "        api_key: Optional[str] = ...,",
        "        token: Optional[str] = ...,",
        "        refresh_token: Optional[str] = ...,",
        "        max_retries: int = ...,",
        "        initial_retry_delay_ms: int = ...,",
        "        max_retry_delay_ms: int = ...,",
        "        retry_on_rate_limit: bool = ...,",
        "    ) -> None: ...",
        "    def _get_or_create_controller(self, cls_name: str, module_path: str) -> Any: ...",
        "    def get_token(self) -> Optional[str]: ...",
        "    def get_refresh_token(self) -> Optional[str]: ...",
        "    def close(self) -> None: ...",
        "    def __enter__(self) -> ThingsboardClient: ...",
        "    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool: ...",
    ])

    # Add controller property stubs and method stubs grouped by controller
    stub_count = 0
    for short_name, cls_name, module_path, methods in controller_classes:
        lines.append("")
        lines.append(f"    # --- {cls_name} ---")
        lines.append("    @property")
        lines.append(f"    def {short_name}(self) -> {cls_name}: ...")
        for method_name, params_clean, return_type in methods:
            # Strip leading 'self' from params_clean (it's always the first param
            # from the source but we emit it explicitly as the method receiver)
            params_no_self = params_clean
            if params_no_self.startswith("self, "):
                params_no_self = params_no_self[len("self, "):]
            elif params_no_self == "self":
                params_no_self = ""
            # Build stub line
            if params_no_self:
                stub_line = f"    def {method_name}(self, {params_no_self}) -> {return_type}: ..."
            else:
                stub_line = f"    def {method_name}(self) -> {return_type}: ..."
            lines.append(stub_line)
            stub_count += 1

    lines.append("")

    return "\n".join(lines), stub_count


def rewrite_init_files(package_dir: Path, package_name: str) -> "Tuple[int, int, int]":
    """Rewrite __init__.py files for lazy loading.

    Returns (model_count, api_count, method_count) tuple.
    """
    models_dir = package_dir / "models"
    api_dir = package_dir / "api"

    if not models_dir.exists():
        print(f"  Warning: models/ directory not found in {package_dir}, skipping lazy import rewrite")
        return 0, 0, 0

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

    # Step 6: Generate _controller_map.py
    method_count = 0
    if api_dir.exists():
        map_content, method_count, _ctrl_count = _generate_controller_map(api_dir, package_name)
        controller_map_path = package_dir / "_controller_map.py"
        controller_map_path.write_text(LICENSE_HEADER + map_content, encoding="utf-8")

    # Step 7: Generate client.pyi type stub
    if api_dir.exists():
        client_py_path = package_dir / "client.py"
        pyi_content, _stub_count = _generate_client_pyi(api_dir, package_name, client_py_path)
        pyi_path = package_dir / "client.pyi"
        pyi_path.write_text(LICENSE_HEADER + pyi_content, encoding="utf-8")

    return len(model_map), len(api_map), method_count


# ---------------------------------------------------------------------------
# Step 4: Apply Apache 2.0 license headers
# ---------------------------------------------------------------------------

def apply_license_headers(py_files: List[Path]) -> int:
    """Prepend LICENSE_HEADER to each .py file that doesn't already have it.

    Returns the number of files modified.
    """
    modified = 0

    for f in py_files:
        content = f.read_text(encoding="utf-8")
        # Skip if already has a license header (either format)
        if "# Copyright" in content[:200] and "ThingsBoard" in content[:200]:
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
    # Step 2a: Convert alias= to serialization_alias= (PEP 8 __init__)
    # -------------------------------------------------------------------
    if models_dir.exists():
        alias_conv, key_fixes = convert_field_aliases(models_dir)
        print(
            f"  Step 2a — PEP 8 aliases: "
            f"{alias_conv} alias= converted to serialization_alias=, "
            f"{key_fixes} from_dict() keys converted to snake_case"
        )
    else:
        print("  Step 2a — Skipped (no models/ directory)")

    # -------------------------------------------------------------------
    # Step 2b: Add __str__/__repr__ and EntityId convenience methods
    # -------------------------------------------------------------------
    if models_dir.exists():
        to_str_fixes, str_injections, eid_patched = add_model_str_methods(models_dir)
        print(
            f"  Step 2b — Model str methods: "
            f"{to_str_fixes} to_str() fixed to snake_case, "
            f"{str_injections} __str__/__repr__ added"
            + (", EntityId patched with get_id()" if eid_patched else "")
        )
    else:
        print("  Step 2b — Skipped (no models/ directory)")

    # -------------------------------------------------------------------
    # Step 3: Rewrite __init__.py files for lazy imports
    # -------------------------------------------------------------------
    model_count, api_count, method_count = rewrite_init_files(package_dir, package_name)
    print(
        f"  Step 3 — Lazy import rewrite: "
        f"{model_count} models, {api_count} controllers, {method_count} methods mapped"
    )

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
    print(f"  Controller map methods:  {method_count}")
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
