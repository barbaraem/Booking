import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from booking_app.models import Booking, Treatment





class FilterCurrentMovieListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        now    = datetime.datetime.now()
        now_30 = now + datetime.timedelta(days=30)
        data = data.filter(screening__date__gte=now, screening__date__lte = now_30)
        return super(FilterCurrentMovieListSerializer, self).to_representation(data)



class BookingSerializer(serializers.ModelSerializer):
    serializers.SlugRelatedField(many=True, slug_field='name', queryset=Treatment.objects.all())
    serializers.SlugRelatedField(many=True, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Booking
        fields = ('id','time', 'date', 'treatment', 'user')

