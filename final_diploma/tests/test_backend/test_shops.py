import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from backend.models import Shop



# shops list - unauthorized client
@pytest.mark.django_db
def test_list_shops_unauthorized_client(unauthorized_client, shop_factory):
    url = reverse("shops-list")
    shop1 = shop_factory()
    shop2 = shop_factory()
    shop3 = shop_factory()
    resp = unauthorized_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 3
    resp_ids = {elem['id'] for elem in resp_json}
    assert resp_ids == {shop1.id, shop2.id, shop3.id}



# shops list - authorized client
@pytest.mark.django_db
def test_list_shops_authorized_client(api_client, shop_factory):
    url = reverse("shops-list")
    shop1 = shop_factory()
    shop2 = shop_factory()
    shop3 = shop_factory()
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 3
    resp_ids = {elem['id'] for elem in resp_json}
    assert resp_ids == {shop1.id, shop2.id, shop3.id}



# create shop - authorized client
@pytest.mark.django_db
def test_create_shop_user(api_client):
    url = reverse("shops-list")
    shop = {
        'name': 'Svyaznoy',
        'url': 'Svyaznoy.ru',
    }
    resp = api_client.post(url, shop)
    assert resp.status_code == HTTP_403_FORBIDDEN
    assert Shop.objects.count() == 0



# create shop - admin
@pytest.mark.django_db
def test_create_shop_admin(admin_client):
    url = reverse("shops-list")
    shop = {
        'name': 'Svyaznoy',
        'url': 'Svyaznoy.ru',
    }
    resp = admin_client.post(url, shop)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert Shop.objects.count() == 1
    assert resp_json['name'] == 'Svyaznoy'



# shop update by an authorized user
@pytest.mark.django_db
def test_shop_update_user(api_client, shop_factory):
    shop = shop_factory()
    url = reverse("shops-detail", args=[shop.id])
    shop = {
        'name': 'Svyaznoy',
        'url': 'Svyaznoy.ru',
    }
    resp = api_client.patch(url, shop)
    assert resp.status_code == HTTP_403_FORBIDDEN
    


# shop update by admin
@pytest.mark.django_db
def test_update_admin(admin_client, shop_factory):
    shop = shop_factory()
    url = reverse("shops-detail", args=[shop.id])
    shop = {
        'name': 'Svyaznoy',
        'url': 'Svyaznoy.ru',
    }
    resp = admin_client.patch(url, shop)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json['name'] == 'Svyaznoy'