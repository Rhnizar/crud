from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_view, name='example'),
    path('<int:id>/', views.example_view2, name='example2'),
]