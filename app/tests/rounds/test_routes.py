def test_index_success(client):
    # Page loads
    response = client.get("/rounds")
    assert response.status_code == 200


def test_index_content(client):
    # Page contains greeting
    response = client.get("/rounds")
    assert b"Rounds listed here" in response.data
