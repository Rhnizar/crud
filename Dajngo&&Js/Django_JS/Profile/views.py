from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, User_Profile
from .serializers import UserSerializer, UserProfileSerializer

# Create your views here.

def index(request):
    return (HttpResponse("Teeeeest"))

def Get_User_Data(request):
    if request.method == 'GET':
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return JsonResponse(serializer.data, safe=False)

def Get_UserProfile_Data(request):
    if request.method == 'GET':
        UserProfiles = User_Profile.objects.all()
        serializer = UserProfileSerializer(UserProfiles, many=True)
        return JsonResponse(serializer.data, safe=False)