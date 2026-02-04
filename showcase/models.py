from django.db import models
from hardware.models import Component


class Rig(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    components = models.ManyToManyField(
        Component,
        related_name='rigs',
        blank=True
    )

    def __str__(self):
        return self.name

