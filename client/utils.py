from django.contrib.auth.models import User
from userManager.utils import create_user
from .models import ClientModel

#create client
def create_client(username, first_name, last_name, email, password, phone_number, NIDA_id_number):
    client_user_account = create_user(username, first_name, last_name, email, password)
    newClient = ClientModel(user = client_user_account, phone_number = phone_number, NIDA_id_number = NIDA_id_number, previlage = "client")
    newClient.save()
   
# delete client accout 
def delete_client(username):
    try:
        # delete the parent user model instance
        client = User.objects.get(username = username)
        client.delete()
        return {"status": 200, "details": "Success"}
    except:
        return {"status":404, "details": "Failed"}
# change phone number  
def change_phone_number(username, phone_number):
    client_instance = User.objects.get(username = username)
    client = ClientModel.objects.get(user = client_instance)
    client.phone_number = phone_number
    client.save()
    
# change client state  
def change_client_state(username, state):
    client_instance = User.objects.get(username = username)
    client = ClientModel.objects.get(user = client_instance)
    client.state = state
    client.save()
    
# change first_name 
def change_first_name(username, first_name):
    client = User.objects.get(username = username)
    client.first_name = first_name
    client.save()
    
# change last_name 
def change_last_name(username, last_name):
    client = User.objects.get(username = username)
    client.last_name = last_name
    client.save()
    
# change email_name 
def change_email(username, email):
    client = User.objects.get(username = username)
    client.first_name = email
    client.save()