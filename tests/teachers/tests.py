def test_teacher_form_get(admin_client):
    response = admin_client.get('/teachers/create')
    assert response.status_code == 200


def test_teachers_list_view_get(admin_client):
    response = admin_client.get('/teachers/')
    assert response.status_code == 200


def test_teacher_form_empty_post(admin_client):
    response = admin_client.post('/teachers/create')
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'first_name': ['This field is required.'],
        'last_name': ['This field is required.'],
        'email': ['This field is required.'],
        'phone_number': ['This field is required.'],
        'profile_description': ['This field is required.'],
        'birth_date': ['This field is required.'],
        'group': ['This field is required.'],
        'role': ['This field is required.']
    }


def test_teacher_form_post(admin_client, group):
    payload = {
        'first_name': 'Jake',
        'last_name': 'Brown',
        'email': 'jake.brown@gmail.com',
        'phone_number': '+1(435)345-35-76',
        'profile_description': 'Hello',
        'birth_date': '2002-3-2',
        'group': group.id,
        'role': 'M'
    }
    response = admin_client.post('/teachers/create', data=payload)
    assert response.status_code == 302
    assert response.url == '/teachers/'


def test_teacher_prohibited_email(admin_client, group):
    payload = {
        'first_name': 'Jake',
        'last_name': 'Brown',
        'email': 'jake.brown@mail.ru',
        'phone_number': '+1(435)345-35-76',
        'profile_description': 'Hello',
        'birth_date': '2002-3-2',
        'group': group.id,
        'role': 'M'
    }
    response = admin_client.post('/teachers/create', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['You cannot register a mail.ru email.']
    }


def test_teacher_form_email_not_unique(admin_client, group):
    payload = {
        'first_name': 'Jake',
        'last_name': 'Brown',
        'email': 'ann.ber73@gmail.com',
        'phone_number': '+1(435)345-35-76',
        'profile_description': 'Hello',
        'birth_date': '2002-3-2',
        'group': group.id,
        'role': 'M'
    }
    response = admin_client.post('/teachers/create', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Email is not unique.']
    }
