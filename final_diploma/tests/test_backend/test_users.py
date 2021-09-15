from django.urls.base import reverse
import pytest
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK


# create user
@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(email='testuser@email.com', password='testpass123')
    assert User.objects.count() == 1
    assert user.email == 'testuser@email.com'
    assert user.is_active == True
    assert user.is_staff == False
    assert user.is_superuser == False


# create superuser
@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    admin_user = User.objects.create_superuser(email='superuser@email.com', password='testpass123')
    assert User.objects.count() == 1
    assert admin_user.email == 'superuser@email.com'
    assert admin_user.is_active == True
    assert admin_user.is_staff == True
    assert admin_user.is_superuser == True


# add contacts
@pytest.mark.django_db
def test_contact_create(api_client):
    url = reverse('user-contact')
    User = get_user_model()
    user = User.objects.create_user(email='testuser2@email.com', password='testpass123')
    contact = {
        "city": "Moscow",
        "street": "Dmitrovka",
        "house": "7",
        "structure": "-",
        "building": "1",
        "apartment": "11",
        "phone": "+7(903)1234567",
        "user": user
    }
    resp = api_client.post(url, contact)
    assert resp.status_code == HTTP_200_OK

    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp_json[0]["phone"] == "+7(903)1234567"
    assert resp_json[0]["street"] == "Dmitrovka"

    