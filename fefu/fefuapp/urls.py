from django.urls import path
from . import views
from .views import text_Post

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('post/', text_Post, name='text_post'),
]