import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.fixture
def unauthorized_client():
    return APIClient()


@pytest.fixture
def api_client(django_user_model):
    user = django_user_model.objects.create_user(email='testuser@email.com', password='testpass123')
    user_token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {user_token.key}')
    return client


@pytest.fixture
def admin_token(admin_user):
    token, _ = Token.objects.get_or_create(user=admin_user)
    return token.key


@pytest.fixture
def admin_client(admin_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {admin_token}')
    return client



