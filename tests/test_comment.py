def test_create_comment(client, user_info, user_token):
    ad_info = {
        "text": "test comment",
        "ad_id": 1
    }
    response = client.post("/api/comment", json=ad_info, headers={"authorization": user_token})
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["text"] == ad_info["text"]
    assert response_json["description"] == ad_info["description"]
    assert response_json["creator"]["email"] == user_info["email"]


def test_create_comment_again(client, user_info, user_token):
    ad_info = {
        "text": "test comment",
        "ad_id": 1
    }
    response = client.post("/api/comment", json=ad_info, headers={"authorization": user_token})
    assert response.status_code == 400
