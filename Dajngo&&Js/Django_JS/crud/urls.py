from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>', views.update, name='update'),
    path('example', views.example_view, name='example'),
    path('<int:id>', views.example_view2, name='example2'),

    path('', views.example_view, name='example'),
    path('<int:id>/', views.example_view2, name='example2'),
]