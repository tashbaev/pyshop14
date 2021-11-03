from django.urls import path

from product.views import home_page, product_list, product_detail, product_create, product_update, product_delete
from .class_views import *
urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', product_create, name='product-create'),
    path('product/update/<int:product_id>/', product_update, name='product-update'),
    path('product/delete/<int:product_id>/', product_delete, name='product-delete')

]
