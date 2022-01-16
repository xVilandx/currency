from django.core.management import call_command

import pytest

from rest_framework.test import APIClient


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = (
            'sources.json',
            'rates.json',
        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')


@pytest.fixture()
def api_client():
    client = APIClient()
    yield client


@pytest.fixture(scope='function')
def api_client_auth(django_user_model):
    api_client = APIClient()

    password = 'superSecretPassword'
    user = django_user_model(
        email='example@admin.com',
    )
    user.set_password(password)
    user.save()

    token_response = api_client.post(
        '/api/v1/token/',
        data={'email': user.email, 'password': password},
    )
    assert token_response.status_code == 200
    access = token_response.json()['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'JWT {access}')

    yield api_client

    user.delete()
