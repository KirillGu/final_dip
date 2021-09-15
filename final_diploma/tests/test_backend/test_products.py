import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK



# products info list - unauthorized client
@pytest.mark.django_db
def test_products_info_list_unauthorized_client(unauthorized_client, product_factory, 
    category_factory, shop_factory, product_info_factory):
    category = category_factory()
    product_1 = product_factory(category_id=category.id)
    product_2 = product_factory(category_id=category.id)
    shop = shop_factory()
    product_info_1 = product_info_factory(product_id=product_1.id, shop_id=shop.id)
    product_info_2 = product_info_factory(product_id=product_2.id, shop_id=shop.id)
    url = reverse("products")
    resp = unauthorized_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 2
    resp_ids = {elem['id'] for elem in resp_json}
    assert resp_ids == {product_info_1.id, product_info_2.id}
    


# products info - authorized client
@pytest.mark.django_db
def test_products_info_list_api_client(api_client, product_factory, 
    category_factory, shop_factory, product_info_factory):
    category = category_factory()
    product_1 = product_factory(category_id=category.id)
    product_2 = product_factory(category_id=category.id)
    shop = shop_factory()
    product_info_1 = product_info_factory(product_id=product_1.id, shop_id=shop.id)
    product_info_2 = product_info_factory(product_id=product_2.id, shop_id=shop.id)
    url = reverse("products")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 2
    resp_ids = {elem['id'] for elem in resp_json}
    assert resp_ids == {product_info_1.id, product_info_2.id}


# products info - admin
@pytest.mark.django_db
def test_products_info_list_admin(admin_client, product_factory, 
    category_factory, shop_factory, product_info_factory):
    category = category_factory()
    product_1 = product_factory(category_id=category.id)
    product_2 = product_factory(category_id=category.id)
    shop = shop_factory()
    product_info_1 = product_info_factory(product_id=product_1.id, shop_id=shop.id)
    product_info_2 = product_info_factory(product_id=product_2.id, shop_id=shop.id)
    url = reverse("products")
    resp = admin_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 2
    resp_ids = {elem['id'] for elem in resp_json}
    assert resp_ids == {product_info_1.id, product_info_2.id}