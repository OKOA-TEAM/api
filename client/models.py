from django.db import models
from userManager.models import BaseUserModel

#Changed the "Client" model to "ClientModel"
class ClientModel(BaseUserModel):
    date_created = models.TimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.first_name
