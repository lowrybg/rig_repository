from django.contrib import admin
from .models import Rig

@admin.register(Rig)
class RigAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')


