from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Treatment(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.DurationField()


class Booking(models.Model):
    date = models.DateTimeField()
    treatment = models.ForeignKey(Treatment)
    user = models.ForeignKey("Client")


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()

