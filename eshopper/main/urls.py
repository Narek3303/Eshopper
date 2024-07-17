from django.urls import path
from .views import HomeListView, product_detail
from django.contrib.auth import views as auth_views
from . import views


app_name = 'shop'


urlpatterns = [
    path('', HomeListView.as_view(), name='products'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('<slug:slug>/', HomeListView.as_view(), name='product_slug'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('review/<slug>/', views.add_review, name='add_review'),
    # path('search/', views.shop_search, name='search'),


]

