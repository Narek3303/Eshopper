from django.urls import path
from . import views


app_name = 'shop_list'

urlpatterns = [
    path('shop/', views.shop_listview, name='shoplist'),
]