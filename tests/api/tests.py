from groups.models import Group
from students.models import Student
from teachers.models import Teacher


def test_get_students_list(client_api):
    response = client_api.get('/api/v1/students/')
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_get_teachers_list(client_api):
    response = client_api.get('/api/v1/teachers/')
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_get_groups_list(client_api):
    response = client_api.get('/api/v1/groups/')
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_post_students_list(client_api):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
    }
    response = client_api.post('/api/v1/students/', data=payload)
    assert response.status_code == 201  # created


def test_put_student(client_api):
    student = Student.objects.last()
    payload = {
        'first_name': 'First',
        'last_name': 'Last',
    }
    response = client_api.put(f'/api/v1/students/{student.id}/', data=payload)
    assert response.status_code == 200


def test_delete_student(client_api):
    student = Student.objects.last()
    response = client_api.delete(f'/api/v1/students/{student.id}/')
    assert response.status_code == 204
    assert not response.content


def test_post_teachers_list(client_api):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
    }
    response = client_api.post('/api/v1/teachers/', data=payload)
    assert response.status_code == 201  # created


def test_put_teacher(client_api):
    teacher = Teacher.objects.last()
    payload = {
        'first_name': 'First',
        'last_name': 'Last',
    }
    response = client_api.put(f'/api/v1/teachers/{teacher.id}/', data=payload)
    assert response.status_code == 200


def test_delete_teacher(client_api):
    teacher = Teacher.objects.last()
    response = client_api.delete(f'/api/v1/teachers/{teacher.id}/')
    assert response.status_code == 204
    assert not response.content


def test_post_group(client_api):
    payload = {
        'specialty': 'Cool specialty'
    }
    response = client_api.post('/api/v1/groups/', data=payload)
    assert response.status_code == 201  # created


def test_put_group(client_api):
    group = Group.objects.last()
    payload = {
        'specialty': 'specialty'
    }
    response = client_api.put(f'/api/v1/groups/{group.id}/', data=payload)
    assert response.status_code == 200


def test_delete_group(client_api):
    group = Group.objects.last()
    response = client_api.delete(f'/api/v1/groups/{group.id}/')
    assert response.status_code == 204
    assert not response.content
