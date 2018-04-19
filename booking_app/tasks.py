from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
from twilio.rest import Client

import arrow

from .models import Booking, Treatment


# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = Client()

@shared_task
def send_sms_reminder(id):
    """Send a reminder to a phone using Twilio SMS"""
    # Get our appointment from the database
    try:
        booking = Booking.objects.get(id=id)
    except Booking.DoesNotExist:
        # The appointment we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    booking_date = arrow.get(booking.date)
    body = 'Przypomnienie o umówionej wizycie {}'.format(booking_date)
    phone_number= booking.user__username
    message = client.messages.create(
        body=body,
        to=phone_number,
        from_=settings.TWILIO_NUMBER,
)