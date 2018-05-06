from django.contrib.auth.models import User
from rest_framework import serializers

from booking_app.models import Booking, Treatment


class BookingSerializer(serializers.ModelSerializer):
    serializers.SlugRelatedField(many=True, slug_field='name', queryset=Treatment.objects.all())
    serializers.SlugRelatedField(many=True, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Booking
        fields = ('id','time', 'date', 'treatment', 'user')
