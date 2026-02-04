from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.name


class Component(models.Model):
    TYPE_CHOICES = [
        ('GPU', 'Graphics Card'),
        ('CPU', 'Processor'),
        ('RAM', 'Memory'),
        ('MB', 'Motherboard'),
        ('STR', 'Storage'),
        ('PSU', 'Power Supply'),
    ]


    name = models.CharField(max_length=150)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    weight_g = models.PositiveIntegerField(help_text="Weight in grams", blank=True, null=True)

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='components'
    )


    def __str__(self):
        return f"{self.brand.name} {self.name}"

