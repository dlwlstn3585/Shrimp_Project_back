from django.db import models

class NoParkingZone(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name