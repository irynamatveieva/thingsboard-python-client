"""
Test configuration and fixtures for thingsboard-python-client tests.

Inserts the ce/ edition into sys.path so that generated tb_ce_client package
(and our overlaid common/ files copied into it) can be imported directly in tests.
"""
import sys
import os

# Make tb_ce_client importable from the ce/ edition directory
_CE_DIR = os.path.join(os.path.dirname(__file__), "..", "ce")
if _CE_DIR not in sys.path:
    sys.path.insert(0, _CE_DIR)
