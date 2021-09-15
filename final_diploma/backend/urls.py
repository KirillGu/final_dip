from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, PartnerOrders, PartnerStateViewSet, PartnerUpdate, ShopViewSet, \
ProductInfoView, BasketView, ContactView, OrderView

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('partner/state', PartnerStateViewSet, basename='partner-state')
router.register('categories', CategoryViewSet, basename='categories')
router.register('shops', ShopViewSet, basename='shops')

urlpatterns = [
    path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/orders/', PartnerOrders.as_view(), name='partner-orders'),
    path('users/contact/', ContactView.as_view(), name='user-contact'),
    path('products/', ProductInfoView.as_view(), name='products'),
    path('order/', OrderView.as_view(), name='order'),
    path('basket/', BasketView.as_view(), name='basket'),
]

urlpatterns += router.urls
