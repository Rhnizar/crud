from django.urls import path
from . import views

urlpatterns = [
    path('check_relationship/', views.check_relationship, name='check'),
    path('create/', views.create, name='create')
]