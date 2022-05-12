
def test_student_form_get(admin_client):
    response = admin_client.get('/students/create')
    assert response.status_code == 200


def test_student_form_post_empty(admin_client):
    response = admin_client.post('/students/create')
    assert response.status_code == 200  # error
    assert response.context_data['form'].errors == {
        'first_name': ['This field is required.'],
        'last_name': ['This field is required.'],
        'email': ['This field is required.'],
        'phone_number': ['This field is required.'],
        'age': ['This field is required.'],
        'enroll_date': ['This field is required.'],
        'graduate_date': ['This field is required.'],
        'inn': ['This field is required.'],
        'group': ['This field is required.'],
    }


def test_student_form_post_valid(admin_client, group):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 22,
        'email': 'example@mail.com',
        'phone_number': '+1(111)222-33-43',
        'enroll_date': '2021-1-1',
        'graduate_date': '2021-2-1',
        'inn': '909090909',
        'group': group.id,
    }
    response = admin_client.post('/students/create', data=payload)
    assert response.status_code == 302  # success
    assert response.url == '/students/'


def test_student_form_post_invalid_email(admin_client, group):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 22,
        'email': 'INVALID-EMAIL',
        'phone_number': '+1(111)222-33-44',
        'enroll_date': '2021-1-1',
        'graduate_date': '2021-2-1',
        'inn': '909090909',
        'group': group.id,
    }
    response = admin_client.post('/students/create', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Enter a valid email address.'],
    }


def test_student_form_post_enroll_date_greater_graduate_date(admin_client, group):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 22,
        'email': 'example1@emai.com',
        'phone_number': '+1(111)222-33-44',
        'enroll_date': '2021-2-1',
        'graduate_date': '2021-1-1',
        'inn': '909090909',
        'group': group.id,
    }
    response = admin_client.post('/students/create', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        '__all__': ['Enroll date cannot be later than graduate date.'],
    }


def test_student_form_post_email_not_unique(admin_client, group):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 22,
        'email': 'email1@email.com',
        'phone_number': '+1(111)222-33-44',
        'enroll_date': '2021-1-1',
        'graduate_date': '2021-2-1',
        'inn': '909090909',
        'group': group.id,
    }
    response = admin_client.post('/students/create', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Email is not unique.']
    }


def test_student_form_post_phone_not_unique(admin_client, group):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 22,
        'email': 'email134@email.com',
        'phone_number': '+38(050)0363769',
        'enroll_date': '2021-1-1',
        'graduate_date': '2021-2-1',
        'inn': '909090909',
        'group': group.id,
    }
    response = admin_client.post('/students/create', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'phone_number': ['Phone number is not unique.']
    }
