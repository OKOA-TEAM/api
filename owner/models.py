from django.db import models
from userManager.models import BaseUserModel

class VehicleOwner(BaseUserModel):
    def __str__(self) -> str:
        return self.user.username
    
class Vehicle(models.Model):
    # create a random ID generator for vehicle, request and users
    # pictures of the vehicles, chassis no, TIN NO and government certifications
    vehicle_owner = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE)
    vehicle_id = models.CharField(max_length=10, blank=True)
    vehicle_name = models.CharField(max_length = 50)
    vehicle_make = models.CharField(max_length = 20)
    vehicle_model = models.CharField(max_length = 20)
    plate_number = models.CharField(max_length = 10)
    
    def __str__(self) -> str:
        return self.vehicle_name
    
class Driver(BaseUserModel):
    employer = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username