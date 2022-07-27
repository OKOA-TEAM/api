from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseUserModel(models.Model): # change from BaseUserModel to ProfileModel
    user = models.ForeignKey(User, on_delete=models.CASCADE) # change from user to useraccount
    phone_number = models.CharField(max_length=12, default="Null")
    NIDA_id_number = models.CharField(max_length=25, default = "Null")
    previlage = models.CharField(max_length=10, default = "client") # Remove default and change "mode" to "cd "
    state = models.BooleanField(default = True)