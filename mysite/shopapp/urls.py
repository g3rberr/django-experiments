from django.urls import path
from .views import (ShopIndexView, GroupsListView, ProductDetailView,
                    ProductsListView, OrderListView, OrderDetailView,
                    ProductCreateView, ProductUpdateView, ProductDeleteView)

app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/', OrderListView.as_view(), name="orders_list"),
    path('orders/<int:pk>', OrderDetailView.as_view(), name="order_detail"),

]