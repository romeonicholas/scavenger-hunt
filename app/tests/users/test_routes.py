def test_users_show_success(client):
    # Page loads
    response = client.get("/users")
    assert response.status_code == 200


def test_users_show_content(client):
    # Page contains explanation
    response = client.get("/users")
    assert b"Find your account here!" in response.data


def test_users_new_success(client):
    # Page loads
    response = client.get("/users/new")
    assert response.status_code == 200


def test_users_new_content(client):
    # Page contains form
    response = client.get("/users/new")
    assert b"Create your account here!" in response.data


def test_users_new_post_success(client):
    # Page loads
    response = client.post("/users/new")
    assert response.status_code == 200
