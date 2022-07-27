from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from django.contrib.auth.models import User
from client.models import ClientModel
from userManager.utils import request_login, user_logout
from .utils import create_client, delete_client
from .serializers import ClientLoginSerializer, NewClientSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from client import serializers

"""_views summary for client module_

from the views defined here the tansaction of data from the database will start from the serializer class then
returned as json response to the server

Expected data to return from API requests

GET and POST REQUESTS
    1. User data
        will be returned in bulk
        
    2. CRUDS
        creating client account, deleting client account.
         
"""


@api_view(['GET'])
def get_client_profile(request, username):
    try:
        # look for requested client profile
        user_account = User.objects.get(username = username)
        user_profile = ClientModel.objects.get(user = user_account, previlage = "client")
        
        data = {
            'username': user_account.username,
            'first_name': user_account.first_name,
            'last_name': user_account.last_name,
            'email':user_account.email,
            'phone_number':user_profile.phone_number,
            'NIDA_id_number':user_profile.NIDA_id_number,
            'previlage':user_profile.previlage,
            'state':user_profile.state,  
        }
        return Response(data)
    except:
        # user account not found
        return Response({"status": 404})
    
    
@api_view(['POST'])
def login_request_view(request):
    data_response = ClientLoginSerializer(data = request.data)
    if data_response.is_valid():
        username = data_response['username'].value
        password = data_response['password'].value
        login_response = request_login(request, username, password)
        return Response(login_response)
    
    return Response({"status": 500, "description":"Failed to process the request"})

def logout_request_view(request):
    user_logout(request)
    return Response({"status": 200, "details": "user logged in"}) 
    


@api_view(['POST'])
def create_client_view(request):
    data_response = NewClientSerializer(data = request.data)
    if data_response.is_valid() or 1==1:
        username = data_response['username'].value
        first_name = data_response['first_name'].value
        last_name = data_response['last_name'].value
        email = data_response['email'].value
        phone_number = data_response['phone_number'].value
        NIDA_id_number = data_response['NIDA_id_number'].value
        password = data_response['password'].value
        
        create_client(username, first_name, last_name, email, password, phone_number, NIDA_id_number)
        
        return Response({"status": 200, "details": "client created"})
    return Response({"status": 400, "details": "Failed to create account"})

@api_view(['GET'])
def delete_client_view(request, username):
    action_status = delete_client(username)
    return Response(action_status)