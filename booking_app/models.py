from django.contrib.auth.models import User
from django.db import models
import datetime


class Treatment(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.DurationField() #może zmień na choice _field

    def __str__(self):
        return self.name

class Booking(models.Model):
    time = models.TimeField(blank=True)
    date = models.DateField()
    treatment = models.ForeignKey(Treatment)
    user = models.ForeignKey(User) # może dodaj checkbox, że wyraża zgodę na użycie telefonu

    # def __str__(self):
    #     return self.date


    def get_hours_list(self, day):

        #tommorow = current_date + datetime.timedelta(days=1)
        #tommorow_bookings = Booking.objects.filter(date=tommorow)

        # booked_hours=[el.datetime.time()for el in tommorow_bookings]

        opening_time = datetime.time(10,0)
        closing_time = datetime.time(18,0)
        # datetime.timedelta(hours=1)


        current_time = opening_time
        arr = []
        while current_time < closing_time:
            arr.append(current_time)
            current_time += datetime.timedelta(hours=1)

        return arr