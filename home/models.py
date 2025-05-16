from django.db import models

class LocationUpdate(models.Model):
    """
    Model to store location updates for delivery drivers.
    """
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Driver {self.driver_id} at ({self.latitude}, {self.longitude})"
