from django.contrib import admin
from .models import LocationReference


# Register your models here.
@admin.register(LocationReference)
class LocationReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_no_sign', 'latitude', 'longitude')
