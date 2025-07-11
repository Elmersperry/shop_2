from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('product/<slug:slug>/', views.product, name='product'),
]