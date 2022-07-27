from django.contrib import admin
from owner.models import VehicleOwner
from . import models

# Register your models here.
class VehicleOwnerAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number")

admin.site.register(models.VehicleOwner, VehicleOwnerAdmin)
admin.site.register(models.Vehicle)
admin.site.register(models.Driver)
