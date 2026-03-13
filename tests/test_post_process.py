"""
Unit tests for _collect_api_classes and _generate_api_init in scripts/post_process.py.

These tests use temporary directories with mock *_api.py files and are runnable
immediately (no regeneration needed). They will PASS after Task 2 adds the functions.
"""
import sys
import tempfile
import os
from pathlib import Path
import pytest

# Add scripts/ to sys.path so we can import post_process directly
_SCRIPTS_DIR = str(Path(__file__).parent.parent / "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import post_process


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def mock_api_dir(tmp_path):
    """Create a temporary api/ directory with mock controller files."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()

    # Mock controller files
    (api_dir / "device_controller_api.py").write_text(
        "class DeviceControllerApi(ApiClient):\n    pass\n",
        encoding="utf-8",
    )
    (api_dir / "alarm_controller_api.py").write_text(
        "class AlarmControllerApi(ApiClient):\n    pass\n",
        encoding="utf-8",
    )
    (api_dir / "admin_controller_api.py").write_text(
        "class AdminControllerApi(ApiClient):\n    pass\n",
        encoding="utf-8",
    )
    # __init__.py should be skipped
    (api_dir / "__init__.py").write_text("# auto-generated\n", encoding="utf-8")

    return api_dir


# ---------------------------------------------------------------------------
# Tests for _collect_api_classes
# ---------------------------------------------------------------------------

def test_collect_api_classes_dynamic(mock_api_dir):
    """_collect_api_classes discovers classes from files without hard-coding."""
    result = post_process._collect_api_classes(mock_api_dir, "tb_ce_client")

    assert "DeviceControllerApi" in result
    assert "AlarmControllerApi" in result
    assert "AdminControllerApi" in result
    # __init__.py must be skipped
    assert len(result) == 3


def test_collect_api_classes_module_paths(mock_api_dir):
    """_collect_api_classes maps class names to correct module paths."""
    result = post_process._collect_api_classes(mock_api_dir, "tb_ce_client")

    assert result["DeviceControllerApi"] == "tb_ce_client.api.device_controller_api"
    assert result["AlarmControllerApi"] == "tb_ce_client.api.alarm_controller_api"
    assert result["AdminControllerApi"] == "tb_ce_client.api.admin_controller_api"


def test_collect_api_classes_empty_dir(tmp_path):
    """_collect_api_classes returns empty dict when api/ has only __init__.py."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    (api_dir / "__init__.py").write_text("", encoding="utf-8")

    result = post_process._collect_api_classes(api_dir, "tb_ce_client")
    assert result == {}


def test_collect_api_classes_multiple_classes_per_file(tmp_path):
    """_collect_api_classes picks up multiple classes from a single file."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    (api_dir / "multi_api.py").write_text(
        "class FooApi(Base):\n    pass\n\nclass BarApi(Base):\n    pass\n",
        encoding="utf-8",
    )

    result = post_process._collect_api_classes(api_dir, "mypkg")
    assert "FooApi" in result
    assert "BarApi" in result
    assert result["FooApi"] == "mypkg.api.multi_api"
    assert result["BarApi"] == "mypkg.api.multi_api"


# ---------------------------------------------------------------------------
# Tests for _generate_api_init
# ---------------------------------------------------------------------------

def test_generate_api_init_lazy_pattern():
    """_generate_api_init output contains __getattr__, _API_CLASSES, TYPE_CHECKING."""
    api_map = {
        "DeviceControllerApi": "tb_ce_client.api.device_controller_api",
        "AlarmControllerApi": "tb_ce_client.api.alarm_controller_api",
    }
    content = post_process._generate_api_init("tb_ce_client", api_map)

    assert "__getattr__" in content
    assert "_API_CLASSES" in content
    assert "TYPE_CHECKING" in content
    assert "importlib" in content
    assert "__dir__" in content


def test_generate_api_init_all_classes(mock_api_dir):
    """All discovered classes appear in __all__ and _API_CLASSES."""
    api_map = post_process._collect_api_classes(mock_api_dir, "tb_ce_client")
    content = post_process._generate_api_init("tb_ce_client", api_map)

    for cls_name in api_map:
        assert f'"{cls_name}"' in content, (
            f"{cls_name!r} not found in generated api/__init__.py content"
        )


def test_generate_api_init_sorted_output():
    """_generate_api_init emits classes in sorted order."""
    api_map = {
        "ZebraControllerApi": "pkg.api.zebra_controller_api",
        "AlphaControllerApi": "pkg.api.alpha_controller_api",
        "MidControllerApi": "pkg.api.mid_controller_api",
    }
    content = post_process._generate_api_init("pkg", api_map)

    alpha_pos = content.index("AlphaControllerApi")
    mid_pos = content.index("MidControllerApi")
    zebra_pos = content.index("ZebraControllerApi")
    assert alpha_pos < mid_pos < zebra_pos, (
        "Classes should appear in sorted (alphabetical) order"
    )


# ---------------------------------------------------------------------------
# Tests for updated _generate_root_init (api_map parameter)
# ---------------------------------------------------------------------------

def test_generate_root_init_no_thingsboard_api():
    """Updated _generate_root_init with empty api_map must not emit ThingsboardApi."""
    content = post_process._generate_root_init("tb_ce_client", {}, {})
    assert "ThingsboardApi" not in content, (
        "_generate_root_init should not hard-code ThingsboardApi when api_map is empty"
    )


def test_generate_root_init_with_api_map():
    """_generate_root_init with api_map lists controllers in _LAZY_CLASSES."""
    api_map = {
        "DeviceControllerApi": "tb_ce_client.api.device_controller_api",
    }
    content = post_process._generate_root_init("tb_ce_client", {}, api_map)
    assert '"DeviceControllerApi"' in content
    assert "device_controller_api" in content


# ---------------------------------------------------------------------------
# Tests for updated rewrite_init_files (Tuple[int, int] return)
# ---------------------------------------------------------------------------

def test_rewrite_init_files_returns_tuple(tmp_path):
    """rewrite_init_files returns (model_count, api_count) tuple."""
    pkg_dir = tmp_path / "tb_test_client"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").write_text("", encoding="utf-8")

    models_dir = pkg_dir / "models"
    models_dir.mkdir()
    (models_dir / "__init__.py").write_text("", encoding="utf-8")
    (models_dir / "device.py").write_text("class Device(BaseModel):\n    pass\n", encoding="utf-8")

    api_dir = pkg_dir / "api"
    api_dir.mkdir()
    (api_dir / "__init__.py").write_text("", encoding="utf-8")
    (api_dir / "device_controller_api.py").write_text(
        "class DeviceControllerApi(ApiClient):\n    pass\n", encoding="utf-8"
    )

    result = post_process.rewrite_init_files(pkg_dir, "tb_test_client")
    assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
    assert len(result) == 2, f"Expected 2-tuple, got {len(result)}-tuple"
    model_count, api_count = result
    assert model_count == 1, f"Expected 1 model, got {model_count}"
    assert api_count == 1, f"Expected 1 api class, got {api_count}"
