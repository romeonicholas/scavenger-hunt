def test_greetings_show_success(client):
    # Page loads
    response = client.get("/greetings")
    assert response.status_code == 200


def test_greetings_show_content(client):
    # Page contains greeting header
    response = client.get("/greetings")
    assert b"Greetings listed here" in response.data


def test_greetings_random_success(client):
    # Page loads
    response = client.get("/greetings/random")
    assert response.status_code == 200


def test_greetings_random_content(client):
    # Page contains greeting header
    response = client.get("/greetings/random")
    assert b"Random Greeting" in response.data
