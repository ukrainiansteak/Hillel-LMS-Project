
def test_all_groups_list_get(admin_client):
    response = admin_client.get('/groups/')
    assert response.status_code == 200


def test_group_list_get(admin_client):
    response = admin_client.get('/groups/43')
    assert response.status_code == 200


def test_group_edit_form_get(admin_client):
    response = admin_client.get('/groups/update/43')
    assert response.status_code == 200


def test_group_edit_form_post_invalid(admin_client):
    response = admin_client.post('/groups/update/43')
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'date_start': ['This field is required.'],
        'location': ['This field is required.'],
        'specialty': ['This field is required.'],
    }


def test_group_edit_form_post(admin_client):
    payload = {
        'date_start': '2022-5-6',
        'location': 'O',
        'specialty': 'Cool specialty',
        'headman': ''
    }
    response = admin_client.post('/groups/update/43', data=payload)
    assert response.status_code == 302
    assert response.url == '/groups/43'
