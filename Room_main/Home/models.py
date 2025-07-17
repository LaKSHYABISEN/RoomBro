from django.db import models

# Create your models here.

class Home(models.Model):
    Rooms = models.CharField(max_length=100)
    Flat = models.CharField(max_length=100)
    Buildings = models.CharField(max_length=200)
    Hotels = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Rooms
    
