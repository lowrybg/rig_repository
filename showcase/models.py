from django.db import models
from hardware.models import Component
from showcase.validators import validate_no_console


class Rig(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(validators=[validate_no_console])
    created_at = models.DateTimeField(auto_now_add=True)


    components = models.ManyToManyField(
        Component,
        related_name='rigs',
        blank=True
    )

    def __str__(self):
        return self.name

