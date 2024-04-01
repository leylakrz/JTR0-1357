import pytest
from starlette.testclient import TestClient

from logics.truncate import truncate_test_db
from main import app
from resources.postgres.session import get_postgres_async_session
from resources.postgres.test_session import get_postgres_test_async_session


@pytest.fixture(scope="session", autouse=True)
def setup_tear_down():
    yield
    truncate_test_db()


@pytest.fixture(scope="session")
def client():
    app.dependency_overrides[get_postgres_async_session] = get_postgres_test_async_session
    client = TestClient(app)
    return client


@pytest.fixture(scope="session")
def user_info():
    return {
        "email": "test@test.com",
        "password": "test_password"
    }


@pytest.fixture(scope="session")
def user_token(client, user_info):
    response = client.post("/api/login", json=user_info)
    return response.json()["access_token"]
