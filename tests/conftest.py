from datetime import date

import pytest
from django.contrib.auth.models import User

from django.core.management import call_command
from rest_framework.test import APIClient

from groups.models import Group


@pytest.fixture(autouse=True, scope='function')
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture()
def group():
    group_object = Group.objects.create(location='O', specialty='specialty', date_start=date(2022, 5, 14))
    yield group_object
    group_object.delete()


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'tests/fixtures/groups.json')
        call_command('loaddata', 'tests/fixtures/students.json')
        call_command('loaddata', 'tests/fixtures/teachers.json')
        call_command('loaddata', 'tests/fixtures/users.json')


@pytest.fixture(scope='function')
def client_api():
    client = APIClient()
    user = User.objects.get(username='admin')
    client.force_authenticate(user=user)
    return client
