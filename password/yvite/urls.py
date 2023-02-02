from django.urls import path, include   
from . import views

urlpatterns = [
    path('', views.password_generator, name='index'),
    path('password_generator/', views.password_generator, name='password_generator'),
]
