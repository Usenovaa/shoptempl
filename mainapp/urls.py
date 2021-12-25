from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('create/category/', CategoryCreate.as_view(), name='category_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
    path('product_detail/<int:pk>/', ProductDetailView, name='detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),

]