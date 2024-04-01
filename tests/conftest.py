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
def client() -> TestClient:
    app.dependency_overrides[get_postgres_async_session] = get_postgres_test_async_session
    client = TestClient(app)
    return client


@pytest.fixture(scope="session")
def user_info() -> dict:
    return {
        "email": "test@test.com",
        "password": "test_password"
    }


@pytest.fixture(scope="session")
def user_token(client, user_info) -> str:
    response = client.post("/api/login", json=user_info)
    return response.json()["access_token"]


@pytest.fixture(scope="session")
def ad_info(client, user_token) -> dict:
    ad = {
        "email": "test ad",
        "password": "ad for testing"
    }
    response = client.post("/api/ad", json=ad, headers={"authorization": user_token})
    return response.json()


@pytest.fixture(scope="session")
def ad_info_2(client, user_token) -> dict:
    ad = {
        "email": "test ad 2",
        "password": "ad for testing"
    }
    response = client.post("/api/ad", json=ad, headers={"authorization": user_token})
    return response.json()
