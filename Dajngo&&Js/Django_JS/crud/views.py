from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.http import JsonResponse
from .serializers import MemeberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.views.decorators.http import require_http_methods

# Create your views here.

# def index(request):
#     if request.method =='GET':
#         Members = Member.objects.all().values('username')
#         Members_list = list(Members)
#         return JsonResponse(Members_list, safe=False)

# Use serializer 

# @require_http_methods(["DELETE"])

@api_view(['GET', 'POST', 'PUT', 'DELETE'])


def example_view(request):
    if request.method == 'GET':
        # Handle GET request
        return Response({'message': 'This is a GET response'})

    elif request.method == 'POST':
        # Handle POST request
        data = request.data
        return Response({'message': f'This is a POST response with data: {data}'})
    
    elif request.method == 'PUT':
        # Handle PUT request
        data = request.data
        return Response({'message': f'This is a PUT response with data: {data}'})
    
    elif request.method == 'DELETE':
        # Handle DELETE request
        return Response({'message': 'This is a DELETE response'})

    # Handle other HTTP methods if needed
    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def index(request):
    # Start with the request line
    request_line = f"{request.method} {request.get_full_path()} {request.META.get('SERVER_PROTOCOL', 'HTTP/1.1')}\n"

    # Collect headers
    headers = ""
    for header, value in request.headers.items():
        headers += f"{header}: {value}\n"

    # Collect the body
    if request.method == "POST":
        body = request.body.decode('utf-8')
    else:
        body = ""

    # Combine everything into the final output
    full_request = request_line + headers + "\n" + body

    # Print the full request
    print("==== FULL REQUEST ====")
    print(full_request)
    print("======================")
    if request.method == 'GET':
        Members = Member.objects.all()
        serializer = MemeberSerializer(Members, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return Response(serializer.data)
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        age = data.get('age')
        member = Member.objects.create(username=username, age=age)
        return JsonResponse({'id': member.id, 'username': member.username, 'age': member.age}, safe=False)

def update(request, id):
    # Start with the request line
    request_line = f"{request.method} {request.get_full_path()} {request.META.get('SERVER_PROTOCOL', 'HTTP/1.1')}\n"
    # Collect headers
    headers = ""
    for header, value in request.headers.items():
        headers += f"{header}: {value}\n"
    # Collect the body
    if request.method == "POST":
        body = request.body.decode('utf-8')
    else:
        body = ""
    # Combine everything into the final output
    full_request = request_line + headers + "\n" + body
    # Print the full request
    print("==== FULL REQUEST ====")
    print(full_request)
    print("======================")
    # if request.method =='PUT' or request.method == 'GET':
    #     member_id = id
    #     print("\nheeere\n")
    #     print(member_id)
    #     print("\n")
        # return JsonResponse("not error", safe=False)
    if request.method =='DELETE' or request.method == 'GET':
        member = Member.objects.get(id=id)
        # serializer = MemeberSerializer(member)
        member.delete()
        # return JsonResponse(serializer.data, safe=False)
        return(HttpResponse("not error"))
    # try:
    #     data = json.loads(request.body)
    #     member_id = data.get('id')
    #     print("\nyeeees\n")
    #     print(member_id)
    #     print("\nyeeees\n")
    #     new_username = data.get('username')
    #     # member = Member.objects.get(id=id)
    #     serializer = MemeberSerializer(member_id)
    #     return JsonResponse(serializer.data)
    # except Member.DoesNotExist:
    #     return JsonResponse({'error': 'Member not found'}, status=404)



    if request.method == 'PUT' or 'POST':
        data = json.loads(request.body)
        member_id = data.get('id')
        new_username = data.get('username')
        
        try:
            member = Member.objects.get(id=member_id)
            member.username = new_username
            member.save()
            return JsonResponse({'id': member.id, 'username': member.username, 'age': member.age})
        except Member.DoesNotExist:
            return JsonResponse({'error': 'Member not found'}, status=404)
