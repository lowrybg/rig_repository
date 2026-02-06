from django.contrib import admin
from .models import Brand, Component

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name','brand', 'type', 'weight_g')
    list_filter = ('type', 'brand')
