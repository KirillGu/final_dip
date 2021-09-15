import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from backend.models import Category



# categories list - unauthorized client
@pytest.mark.django_db
def test_list_categories_unauthorized_client(unauthorized_client, category_factory):
    url = reverse("categories-list")
    category1 = category_factory()
    category2 = category_factory()
    resp = unauthorized_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert len(resp_json) == 2
    resp_ids = {elem['id'] for elem in resp_json}
    assert resp_ids == {category1.id, category2.id}


# categories list - authorized client
@pytest.mark.django_db
def test_list_categories_authorized_client(api_client):
    url = reverse("categories-list")
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json == []


# create category - authorized client
@pytest.mark.django_db
def test_create_category_user(api_client):
    url = reverse("categories-list")
    category = {
        'name': 'Smartphones',
        'shops': 'Svyaznoy',
    }
    resp = api_client.post(url, category)
    assert resp.status_code == HTTP_403_FORBIDDEN
    assert Category.objects.count() == 0


# create category - admin
@pytest.mark.django_db
def test_create_category_admin(admin_client):
    url = reverse("categories-list")
    category = {
        'name': 'Smartphones',
        'shops': 'Svyaznoy',
    }
    resp = admin_client.post(url, category)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert Category.objects.count() == 1
    assert resp_json['name'] == 'Smartphones'
    return resp_json


# category update by an authorized user
@pytest.mark.django_db
def test_category_update_user(api_client, admin_client):
    resp_json = test_create_category_admin(admin_client)
    url = reverse("categories-detail", args=[resp_json["id"]])
    category = {
        'name': 'Notebooks',
        'shops': 'Svyaznoy',
    }
    resp = api_client.patch(url, category)
    resp_json = resp.json()
    assert resp.status_code == HTTP_403_FORBIDDEN


# category update by admin
@pytest.mark.django_db
def test_category_update_admin(admin_client):
    resp_json = test_create_category_admin(admin_client)
    url = reverse("categories-detail", args=[resp_json["id"]])
    category = {
        'name': 'Notebooks',
        'shops': 'Svyaznoy',
    }
    resp = admin_client.patch(url, category)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json["name"] == 'Notebooks'
