from django.contrib import admin
from django.contrib.auth.models import User

from marketplace.models import PriceReport, Listing


@admin.register(PriceReport)
class PriceReportAdmin(admin.ModelAdmin):
    list_display = ('component','price','store_name','created_at')
    list_filter = ('store_name',)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','price','condition','seller')
    list_filter = ('condition',)
