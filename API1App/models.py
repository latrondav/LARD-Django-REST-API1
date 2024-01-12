from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    year_founded = models.PositiveIntegerField()

    def __str__(self):
        return self.name
