from django.urls import path
from .import views

urlpatterns = [
    path('',views.Get_User_Data, name='Get_User_Data'),
    path('prData/',views.Get_UserProfile_Data, name='Get_UserProfile_Data')
]
