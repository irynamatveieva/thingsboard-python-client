"""
Structural tests for per-controller split (SPLIT-01, SPLIT-02, SPLIT-04, SPLIT-05, SPLIT-06).

These tests verify the per-controller split output. They import from tb_ce_client
(via conftest.py sys.path to ce/). They will FAIL (RED) until Plan 03 regenerates
the editions with per-controller files.
"""

import importlib
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

CE_API_DIR = PROJECT_ROOT / "ce" / "tb_ce_client" / "api"
PE_API_DIR = PROJECT_ROOT / "pe" / "tb_pe_client" / "api"
PAAS_API_DIR = PROJECT_ROOT / "paas" / "tb_paas_client" / "api"


# ---------------------------------------------------------------------------
# SPLIT-01 / SPLIT-05: File count tests
# ---------------------------------------------------------------------------


def test_ce_controller_file_count():
    """CE edition must have at least 55 per-controller API files (not __init__.py)."""
    files = [f for f in CE_API_DIR.glob("*.py") if f.name != "__init__.py"]
    assert len(files) >= 55, (
        f"Expected >=55 controller files in CE api/, got {len(files)}. "
        f"Run Plan 03 to regenerate with per-controller split."
    )


def test_pe_controller_file_count():
    """PE edition must have at least 78 per-controller API files."""
    files = [f for f in PE_API_DIR.glob("*.py") if f.name != "__init__.py"]
    assert len(files) >= 78, (
        f"Expected >=78 controller files in PE api/, got {len(files)}. "
        f"Run Plan 03 to regenerate with per-controller split."
    )


def test_paas_controller_file_count():
    """PaaS edition must have at least 83 per-controller API files."""
    files = [f for f in PAAS_API_DIR.glob("*.py") if f.name != "__init__.py"]
    assert len(files) >= 83, (
        f"Expected >=83 controller files in PaaS api/, got {len(files)}. "
        f"Run Plan 03 to regenerate with per-controller split."
    )


def test_no_monolith_file():
    """thingsboard_api.py must NOT exist in CE api/ after per-controller split."""
    monolith = CE_API_DIR / "thingsboard_api.py"
    assert not monolith.exists(), (
        "thingsboard_api.py still exists in CE api/. "
        "Run Plan 03 to regenerate with per-controller split."
    )


# ---------------------------------------------------------------------------
# SPLIT-04: Lazy import tests
# ---------------------------------------------------------------------------


def test_lazy_api_init_does_not_load_controllers():
    """Importing tb_ce_client.api should not eagerly load any controller modules."""
    # Evict the api package and all api submodules for a clean import.
    # We intentionally do NOT evict tb_ce_client.client or tb_ce_client.models
    # so that test_client.py mocks (which patch module-level class references)
    # remain valid when both test files run together in one session.
    # After the Task 1 fix, client.py has no top-level LoginEndpointApi import,
    # so evicting only the api tree is sufficient to guarantee lazy-load behaviour.
    mods_to_remove = [
        k for k in sys.modules if k == "tb_ce_client.api" or k.startswith("tb_ce_client.api.")
    ]
    for m in mods_to_remove:
        del sys.modules[m]

    # Import only the api package
    import tb_ce_client.api  # noqa: F401

    loaded = [k for k in sys.modules if k.startswith("tb_ce_client.api.")]
    assert loaded == [], (
        f"Unexpected controller modules loaded on 'import tb_ce_client.api': {loaded}"
    )


def test_lazy_api_loads_on_access():
    """Accessing DeviceControllerApi from tb_ce_client.api loads exactly that module."""
    # Clear cache first
    mods_to_remove = [k for k in sys.modules if k.startswith("tb_ce_client.api.")]
    for m in mods_to_remove:
        del sys.modules[m]
    sys.modules.pop("tb_ce_client.api", None)

    from tb_ce_client.api import DeviceControllerApi

    assert DeviceControllerApi.__module__ == "tb_ce_client.api.device_controller_api", (
        f"DeviceControllerApi.__module__ = {DeviceControllerApi.__module__!r}, "
        f"expected 'tb_ce_client.api.device_controller_api'"
    )


# ---------------------------------------------------------------------------
# SPLIT-06: Root __init__.py tests
# ---------------------------------------------------------------------------


def test_root_import_does_not_load_controllers():
    """Importing tb_ce_client should not load any api.* controller submodules."""
    # Evict the api package and all api submodules for a clean import.
    # We intentionally do NOT evict tb_ce_client.client or tb_ce_client.models
    # so that test_client.py mocks remain valid in a combined test session.
    # After the Task 1 fix, importing tb_ce_client root no longer pulls in
    # login_endpoint_api, so this targeted eviction is sufficient.
    mods_to_remove = [
        k for k in sys.modules if k == "tb_ce_client.api" or k.startswith("tb_ce_client.api.")
    ]
    for m in mods_to_remove:
        del sys.modules[m]

    # Re-import root
    importlib.import_module("tb_ce_client")

    api_submodules = [k for k in sys.modules if k.startswith("tb_ce_client.api.")]
    assert api_submodules == [], (
        f"Unexpected api submodules loaded after 'import tb_ce_client': {api_submodules}"
    )


def test_no_thingsboard_api_in_lazy_classes():
    """Root __init__.py _LAZY_CLASSES must not contain 'ThingsboardApi' after split."""
    root_init = PROJECT_ROOT / "ce" / "tb_ce_client" / "__init__.py"
    assert root_init.exists(), f"CE root __init__.py not found at {root_init}"
    content = root_init.read_text(encoding="utf-8")

    # Find _LAZY_CLASSES dict content (between { and the closing })
    # Check that ThingsboardApi is not a key in it
    assert '"ThingsboardApi"' not in content or "thingsboard_api" not in content, (
        "root __init__.py still references ThingsboardApi in _LAZY_CLASSES. "
        "Run Plan 03 to regenerate with per-controller split."
    )


# ---------------------------------------------------------------------------
# SPLIT-02: Dynamic discovery (structural — requires generated files)
# ---------------------------------------------------------------------------


def test_collect_api_classes_dynamic():
    """_collect_api_classes discovers classes without hard-coding names."""
    # This tests that the function is callable and returns sensible results
    # on the actual CE api/ directory (after regeneration).
    import sys as _sys

    scripts_dir = str(PROJECT_ROOT / "scripts")
    if scripts_dir not in _sys.path:
        _sys.path.insert(0, scripts_dir)
    import post_process

    result = post_process._collect_api_classes(CE_API_DIR, "tb_ce_client")
    assert len(result) >= 55, (
        f"_collect_api_classes found only {len(result)} classes from CE api/ "
        f"(expected >= 55). Run Plan 03 to regenerate."
    )
    # Verify dynamic discovery: no hard-coded names used
    assert all(cls.endswith("Api") for cls in result), (
        "All discovered classes should end with 'Api'"
    )
