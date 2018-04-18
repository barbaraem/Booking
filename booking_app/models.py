from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Treatment(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.DurationField() #może zmień na choice _field


class Booking(models.Model):
    date = models.DateTimeField()
    treatment = models.ForeignKey(Treatment)
    user = models.ForeignKey(User) # może dodaj checkbox, że wyraża zgodę na użycie telefonu


