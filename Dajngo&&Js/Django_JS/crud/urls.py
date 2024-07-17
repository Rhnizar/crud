from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:id>/', views.update, name='update'),
    path('/example', views.example_view, name='index'),
]