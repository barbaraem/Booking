from django.contrib import admin


from django.contrib.auth.models import Permission


from booking_app.models import Treatment, Booking

admin.site.register(Treatment)
admin.site.register(Booking)
