def test_index_success(client):
    # Page loads
    response = client.get("/")
    assert response.status_code == 200


def test_index_content(client):
    # Page contains greeting
    response = client.get("/")
    assert b"Let's play a game!" in response.data
