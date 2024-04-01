def test_create_ad(client, user_info, user_token):
    ad_info = {
        "title": "test ad",
        "description": "ad for testing"
    }
    response = client.post("/api/ad", json=ad_info, headers={"authorization": user_token})
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == ad_info["title"]
    assert response_json["description"] == ad_info["description"]
    assert response_json["creator"]["email"] == user_info["email"]


def test_list_ad(client):
    response = client.get("/api/ad")
    assert response.status_code == 200


def test_retrieve_ad(client):
    response = client.get("/api/ad/1")
    assert response.status_code == 200
