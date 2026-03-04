import sys
from pathlib import Path

# Add project root to PYTHONPATH so "config" and "src" can be imported reliably
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from config.settings import load_settings
from src.client.api_client import APIClient

@pytest.fixture(scope="session")
def settings():
    return load_settings()

@pytest.fixture(scope="session")
def api(settings):
    return APIClient(
        base_url=settings["base_url"],
        timeout=settings["timeout"],
        api_key=settings["api_key"],
    )
