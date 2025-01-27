from django.urls import path
from .views import post_list_and_create

urlpatterns = [
    path('', post_list_and_create, name='home'),
]