"""
Tests validating generated documentation for all three ThingsBoard client editions.

Validates:
- doc file counts (DGEN-01, DGEN-02)
- Python naming conventions in controller docs (DGEN-03)
- Pydantic conventions in model docs (DGEN-04)
- Docs are outside the installed package (DOC-02)
- CE wheel excludes docs/ (DOC-03)
"""
import subprocess
import zipfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
CE_DOCS = REPO_ROOT / "ce" / "docs"
PE_DOCS = REPO_ROOT / "pe" / "docs"
PAAS_DOCS = REPO_ROOT / "paas" / "docs"


# ---------------------------------------------------------------------------
# CE doc existence and count tests
# ---------------------------------------------------------------------------


def test_ce_docs_exist_outside_package():
    """ce/docs/ exists and contains >=700 .md files."""
    assert CE_DOCS.is_dir(), "ce/docs/ directory does not exist"
    md_files = list(CE_DOCS.glob("*.md"))
    assert len(md_files) >= 700, (
        f"ce/docs/ has {len(md_files)} .md files (expected >=700)"
    )


def test_ce_docs_not_in_package():
    """ce/tb_ce_client/docs/ must NOT exist — docs are outside the package."""
    package_docs = REPO_ROOT / "ce" / "tb_ce_client" / "docs"
    assert not package_docs.exists(), (
        f"ce/tb_ce_client/docs/ should not exist but was found at {package_docs}"
    )


def test_ce_controller_docs_exist():
    """ce/docs/ has >=50 *ControllerApi.md files including DeviceControllerApi.md."""
    assert CE_DOCS.is_dir(), "ce/docs/ directory does not exist"
    controller_files = list(CE_DOCS.glob("*Api.md"))
    assert len(controller_files) >= 50, (
        f"ce/docs/ has {len(controller_files)} *Api.md files (expected >=50)"
    )
    device_doc = CE_DOCS / "DeviceControllerApi.md"
    assert device_doc.exists(), "ce/docs/DeviceControllerApi.md does not exist"


def test_ce_model_docs_exist():
    """ce/docs/ has >=600 non-Api model .md files."""
    assert CE_DOCS.is_dir(), "ce/docs/ directory does not exist"
    all_md = list(CE_DOCS.glob("*.md"))
    api_md = list(CE_DOCS.glob("*Api.md"))
    model_count = len(all_md) - len(api_md)
    assert model_count >= 600, (
        f"ce/docs/ has {model_count} model .md files (expected >=600)"
    )


# ---------------------------------------------------------------------------
# CE controller doc content tests
# ---------------------------------------------------------------------------


def test_ce_device_doc_has_python_method_names():
    """DeviceControllerApi.md uses snake_case method names (assign_device_to_customer).

    The docs may contain camelCase names in description/summary text (e.g. "Assign device to
    customer (assignDeviceToCustomer)") that comes verbatim from the OpenAPI spec. What matters
    is that the Python callable form uses snake_case: ``client.assign_device_to_customer``.
    """
    doc = CE_DOCS / "DeviceControllerApi.md"
    assert doc.exists(), "ce/docs/DeviceControllerApi.md does not exist"
    content = doc.read_text(encoding="utf-8")
    # The snake_case method appears as both a section heading and in code blocks
    assert "assign_device_to_customer" in content, (
        "DeviceControllerApi.md missing snake_case method 'assign_device_to_customer'"
    )
    # The client. prefix before snake_case confirms the callable is rendered in Python style
    assert "client.assign_device_to_customer" in content, (
        "DeviceControllerApi.md missing 'client.assign_device_to_customer' callable form"
    )


def test_ce_device_doc_has_method_sections():
    """DeviceControllerApi.md has ## assign_device_to_customer heading and HTTP verb markers."""
    doc = CE_DOCS / "DeviceControllerApi.md"
    assert doc.exists(), "ce/docs/DeviceControllerApi.md does not exist"
    content = doc.read_text(encoding="utf-8")
    assert "## assign_device_to_customer" in content, (
        "DeviceControllerApi.md missing '## assign_device_to_customer' section heading"
    )
    assert "**POST**" in content or "**GET**" in content, (
        "DeviceControllerApi.md missing HTTP verb markers (**POST** or **GET**)"
    )


# ---------------------------------------------------------------------------
# CE model doc content tests
# ---------------------------------------------------------------------------


def test_ce_model_doc_has_python_conventions():
    """Device.md contains 'model_dump' and does NOT contain Java getter 'getId()'."""
    doc = CE_DOCS / "Device.md"
    assert doc.exists(), "ce/docs/Device.md does not exist"
    content = doc.read_text(encoding="utf-8")
    assert "model_dump" in content, (
        "Device.md missing Pydantic convention 'model_dump'"
    )
    assert "getId()" not in content, (
        "Device.md contains Java getter 'getId()' (should use Pydantic conventions)"
    )


def test_ce_model_doc_has_package_reference():
    """Device.md references 'tb_ce_client.models'."""
    doc = CE_DOCS / "Device.md"
    assert doc.exists(), "ce/docs/Device.md does not exist"
    content = doc.read_text(encoding="utf-8")
    assert "tb_ce_client.models" in content, (
        "Device.md missing package reference 'tb_ce_client.models'"
    )


# ---------------------------------------------------------------------------
# PE doc tests
# ---------------------------------------------------------------------------


def test_pe_docs_exist():
    """pe/docs/ exists with >=900 .md files and >=78 *Api.md controller docs."""
    assert PE_DOCS.is_dir(), "pe/docs/ directory does not exist"
    md_files = list(PE_DOCS.glob("*.md"))
    api_files = list(PE_DOCS.glob("*Api.md"))
    assert len(md_files) >= 900, (
        f"pe/docs/ has {len(md_files)} .md files (expected >=900)"
    )
    assert len(api_files) >= 78, (
        f"pe/docs/ has {len(api_files)} *Api.md files (expected >=78)"
    )


def test_pe_model_doc_has_correct_package():
    """A PE model doc references 'tb_pe_client.models' (not tb_ce_client)."""
    assert PE_DOCS.is_dir(), "pe/docs/ directory does not exist"
    # Look for any non-Api .md file (a model doc)
    model_docs = [f for f in PE_DOCS.glob("*.md") if not f.name.endswith("Api.md")]
    assert model_docs, "pe/docs/ has no model .md files"
    # Check several until we find one with the package reference
    found = False
    for doc in model_docs[:20]:
        content = doc.read_text(encoding="utf-8")
        if "tb_pe_client.models" in content:
            found = True
            break
    assert found, (
        "No PE model doc contains 'tb_pe_client.models' package reference"
    )
    # Also assert no PE doc references tb_ce_client
    ce_refs = [
        f for f in model_docs[:20]
        if "tb_ce_client" in f.read_text(encoding="utf-8")
    ]
    assert not ce_refs, (
        f"PE model docs contain 'tb_ce_client' reference: {ce_refs[0].name}"
    )


# ---------------------------------------------------------------------------
# PaaS doc tests
# ---------------------------------------------------------------------------


def test_paas_docs_exist():
    """paas/docs/ exists with >=900 .md files and >=83 *Api.md controller docs."""
    assert PAAS_DOCS.is_dir(), "paas/docs/ directory does not exist"
    md_files = list(PAAS_DOCS.glob("*.md"))
    api_files = list(PAAS_DOCS.glob("*Api.md"))
    assert len(md_files) >= 900, (
        f"paas/docs/ has {len(md_files)} .md files (expected >=900)"
    )
    assert len(api_files) >= 83, (
        f"paas/docs/ has {len(api_files)} *Api.md files (expected >=83)"
    )


def test_paas_model_doc_has_correct_package():
    """A PaaS model doc references 'tb_paas_client.models' (not tb_ce_client)."""
    assert PAAS_DOCS.is_dir(), "paas/docs/ directory does not exist"
    model_docs = [f for f in PAAS_DOCS.glob("*.md") if not f.name.endswith("Api.md")]
    assert model_docs, "paas/docs/ has no model .md files"
    found = False
    for doc in model_docs[:20]:
        content = doc.read_text(encoding="utf-8")
        if "tb_paas_client.models" in content:
            found = True
            break
    assert found, (
        "No PaaS model doc contains 'tb_paas_client.models' package reference"
    )
    ce_refs = [
        f for f in model_docs[:20]
        if "tb_ce_client" in f.read_text(encoding="utf-8")
    ]
    assert not ce_refs, (
        f"PaaS model docs contain 'tb_ce_client' reference: {ce_refs[0].name}"
    )


# ---------------------------------------------------------------------------
# CE wheel exclusion test
# ---------------------------------------------------------------------------


def test_ce_wheel_excludes_docs():
    """Build CE wheel and verify it contains no docs/ entries."""
    ce_dir = REPO_ROOT / "ce"
    dist_dir = ce_dir / "dist"

    # Clean any prior build artifacts
    if dist_dir.exists():
        for f in dist_dir.iterdir():
            f.unlink()

    result = subprocess.run(
        ["poetry", "build"],
        cwd=str(ce_dir),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"poetry build failed:\n{result.stdout}\n{result.stderr}"
    )

    whl_files = list(dist_dir.glob("*.whl"))
    assert whl_files, f"No .whl file found in {dist_dir}"
    whl = whl_files[0]

    with zipfile.ZipFile(whl) as zf:
        docs_entries = [name for name in zf.namelist() if "/docs/" in name]

    # Clean up build artifacts
    for f in dist_dir.iterdir():
        f.unlink()
    dist_dir.rmdir()

    assert not docs_entries, (
        f"CE wheel contains docs/ entries: {docs_entries[:5]}"
    )
