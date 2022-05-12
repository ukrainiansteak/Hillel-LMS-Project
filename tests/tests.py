def test_index_get_auth(admin_client):
    response = admin_client.get('/')
    assert response.status_code == 200


def test_index_get_anon(client):
    response = client.get('/')
    assert response.status_code == 302
