def test_register(client, user_info):
    response = client.post("/api/register", json=user_info)
    assert response.status_code == 200


def test_register_again(client, user_info):
    response = client.post("/api/register", json=user_info)
    assert response.status_code == 400


def test_login(client, user_info):
    response = client.post("/api/login", json=user_info)
    assert response.status_code == 200
    assert "access_token" in response.json()
