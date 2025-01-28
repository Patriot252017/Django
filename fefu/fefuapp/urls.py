from django.urls import path
from .views import post_list_and_create
from .views import login
from . import views

urlpatterns = [
    path('', post_list_and_create, name='home'),
    path('register/', views.register, name='register'),
    path('login/', login, name='login'),
]