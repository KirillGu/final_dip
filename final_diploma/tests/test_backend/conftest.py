import pytest
from model_bakery import baker


@pytest.fixture
def product_factory():
    def factory(**kwargs):
        return baker.make("Product", **kwargs)
    return factory


@pytest.fixture
def category_factory():
    def factory(**kwargs):
        return baker.make("Category", **kwargs)
    return factory


@pytest.fixture
def product_info_factory():
    def factory(**kwargs):
        return baker.make("ProductInfo", **kwargs)
    return factory


@pytest.fixture
def shop_factory():
    def factory(**kwargs):
        return baker.make("Shop", **kwargs)
    return factory