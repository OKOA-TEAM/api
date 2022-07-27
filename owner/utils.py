from .models import Vehicle, VehicleOwner, Driver
from django.contrib.auth.models import User
from userManager.utils import create_user

#create owner
def create_owner(username, first_name, last_name, email, password, phone_number, NIDA_id_number):
    owner_user_account = create_user(username, first_name, last_name, email, password)
    new_owner = VehicleOwner(user = owner_user_account, phone_number = phone_number, NIDA_id_number = NIDA_id_number, mode = "owner")
    new_owner.save()
  
# change phone number  
def change_phone_number(username, phone_number):
    owner_instance = User.objects.get(username = username)
    owner = VehicleOwner.objects.get(user = owner_instance)
    owner.phone_number = phone_number
    owner.save()
    
# change owner state  
def change_owner_state(username, state):
    owner_instance = User.objects.get(username = username)
    owner = VehicleOwner.objects.get(user = owner_instance)
    owner.state = state
    owner.save()
    
# change first_name 
def change_first_name(username, first_name):
    owner = User.objects.get(username = username)
    owner.first_name = first_name
    owner.save()
    
# change last_name 
def change_last_name(username, last_name):
    owner = User.objects.get(username = username)
    owner.last_name = last_name
    owner.save()
    
# change email_name 
def change_email(username, email):
    owner = User.objects.get(username = username)
    owner.first_name = email
    owner.save()
    
    
# Drive model manipulation
#create
def create_driver(employer_id_number, username, first_name, last_name, email, password, phone_number, NIDA_id_number):
    # get employer accout
    try:
        employer = VehicleOwner.objects.get(NIDA_id_number = employer_id_number)
        driver_user_account = create_user(username, first_name, last_name, email, password)
        new_driver = Driver(employer = employer, user = driver_user_account, phone_number = phone_number, NIDA_id_number = NIDA_id_number, mode = "driver")
        new_driver.save()
    except:
        return 404
    
   
#Vehicle model manipulation

def create_vehicle(owner_usrname, vehicle_name, vehicle_make, vehicle_model, plate_number):
    owner = VehicleOwner.objects.get(username = owner_usrname)
    newVehicle = Vehicle(vehicle_owner = owner)
    newVehicle.vehicle_id = "_randomId_"
    newVehicle.vehicle_name = vehicle_name
    newVehicle.vehicle_make = vehicle_make
    newVehicle.vehicle_model = vehicle_model
    newVehicle.plate_number = plate_number
    newVehicle.save()
    
def delete_vehicle(plate_number):
    vehicle_instance = Vehicle.objects.get(plate_number = plate_number)
    vehicle_instance.delete()