import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from dateparser import parse

# Create your views here.
from django.views.generic.base import View


from booking_app.forms import AddClientForm, AddTreatmentForm, ClientLoginForm, BookingForm
from booking_app.models import Booking, Treatment


class PriceListView(View):
    def get(self, request):
        price_list = Treatment.objects.all()
        return render(request, "home.html", {"price_list":price_list})


class AddClientView(View):

   def get(self, request):
       form = AddClientForm()
       return render(request, 'add_client.html', {'form': form})

   def post(self, request):
       form = AddClientForm(request.POST)

       if form.is_valid():
           first_name = form.cleaned_data['first_name']
           last_name = form.cleaned_data['last_name']
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           repeat_password = form.cleaned_data['repeat_password']

           if password != repeat_password:
               message = 'wpisane hasła nie są takie same'
               return render(request, 'add_client.html', {'form': form,
                                                        'message': message})
           else:
               try:
                   User.objects.create_user(password=password,first_name=first_name,
                                              last_name=last_name, username=username)

                   return redirect("/user_login")

               except IntegrityError:
                   return HttpResponse('ten numer telefonu jest już zarejesterowany')
       else:
           return render(request, 'add_client.html', {'form': form})



class ClientLoginView(View):

    def get(self, request):
        form= ClientLoginForm()
        return render(request, "user_login.html", {"form":form})


    def post(self, request):
        form = ClientLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(username = username, password = password)

            if user is not None:
                login(request,user)
                return redirect("/home")
            else:
                return render(request, "user_login.html", {"form": form, "message":"błędne dane"})



class AddTreatmentView(View):

    def get(self, request):
       form = AddTreatmentForm()
       return render(request, 'add_treatment.html', {'form': form})


    def post(self, request):
        form = AddTreatmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")


class BookingView(View):

    def get(self, request, treatment_id):
        form = BookingForm()
        bookings= Booking.objects.all()
        treatment= Treatment.objects.get(id=treatment_id)

        return render(request, "booking.html", {"form":form})


    def post(self, request, treatment_id):
        form = BookingForm(request.POST)
        # current_date = datetime.now()
        # dates = Booking.objects.filter(date__gte= current_date)

        if form.is_valid():
            treatment = Treatment.objects.get(id=treatment_id)
            user = request.user
            date = request.POST.get("date")
            # booking_date = parse(booking_date).datetime()
            time = request.POST.get("time")

            # # validation of date back:
            # if booking_date < current_date:
            #     message = "wprowadź poprawną datę"
            #     return render(request, "booking.html", {"form":form,"dates":dates, "message": message})
            #
            # # validation of double booking:
            # # if Booking.objects.filter(date = booking_date):
            # #     return render(request, "booking.html", {"form":form,"dates":dates, "message": "ten termin jest już zajęty!"})
            #
            #
            # # validation of double booking-time
            # booked_hours = [booking.time for booking in Booking.objects.filter(date= booking_date)]



            Booking.objects.create(date = date, time=time, treatment= treatment, user=user)
            return redirect("/home")
        else:
            print(form.errors)
            return render(request, "booking.html", {"form": form})


# form = PresenceForm(initial={
#             'day': presence_day})

    # rooms = GetRoom.get_available_room({}).exclude(id__in=self.room_booked)



    """
    
t = datetime.time(1, 2, 3)
print('t :', t)

d = datetime.date.today()
print('d :', d)

dt = datetime.datetime.combine(d, t)
print('dt:', dt)

combine() creates datetime instances from one date and one time instance.

$ python3 datetime_datetime_combine.py

t : 01:02:03
d : 2018-03-18
dt: 2018-03-18 01:02:03


    """