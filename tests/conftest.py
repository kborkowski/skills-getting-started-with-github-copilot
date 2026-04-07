from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def restore_activities_state():
    original_state = deepcopy(app_module.activities)

    # Arrange
    yield

    # Cleanup shared in-memory state between tests
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original_state))


@pytest.fixture
def client():
    return TestClient(app_module.app)
