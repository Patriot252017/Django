from django.urls import path
from .views import post_list_and_create
from . import views

urlpatterns = [
    path('', post_list_and_create, name='home'),
    path('users/', views.create, name='create'),
    path('get_users/', views.get_users, name='get_users'),
    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('users/<int:user_id>/update/', views.update, name='update'),
    path('users/<int:user_id>/delete/', views.delete, name='delete'),
]