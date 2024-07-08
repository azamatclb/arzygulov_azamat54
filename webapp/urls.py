from django.urls import path
from . import views
from webapp.views import add_product, product_view, add_category, delete_product, update_product

urlpatterns = [
    path('', views.index, name='products'),
    path('categories/add/', add_category, name='add_category'),
    path('product/<int:pk>/', product_view, name='product_view'),
    path('products/add/', add_product, name='add_product'),
    path('product/<int:pk>/delete', delete_product, name='delete_product'),
    path('product/<int:pk>/update', update_product, name='update_product'),
]
