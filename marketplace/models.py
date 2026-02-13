from django.contrib.auth.models import User
from django.db import models

from hardware.models import Component


class PriceReport(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='price_report')
    store_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.price} - {self.store_name}"

class Listing(models.Model):
    CONDITION_CHOICES = [
        ('NEW', 'Brand New'),
        ('USED', 'Used - Like New'),
        ('OLD', 'Used - Good'),
        ('DMG', 'Damaged/For Parts'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES, default='USED')
    related_component = models.ForeignKey(Component, on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    contact_email = models.EmailField(help_text="Buyer will contact you here")

    def __str__(self):
        return f"{self.title} ({self.price})"