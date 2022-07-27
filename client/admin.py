from django.contrib import admin
from .models import ClientModel


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number","date_created")
    
admin.site.register(ClientModel, ClientAdmin)