from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from dateparser import parse

# Create your views here.
from django.views.generic.base import View


from booking_app.forms import AddClientForm, AddTreatmentForm, ClientLoginForm
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

        return render(request, "booking.html", {"form":form, "bookings":bookings, "treatment": treatment})


    def post(self, request, treatment_id):

        form = BookingForm()
        current_date = datetime.now()
        dates = Booking.objects.filter(date__gte= current_date)

        if form.is_valid():
            treatment = Treatment.objects.get(id=treatment_id)
            user = request.user
            booking_date = request.POST.get("date")
            booking_date = parse(booking_date).datetime()

            # validation of date back:
            if booking_date < current_date:
                message = "wprowadź poprawną datę"
                return render(request, "booking.html", {"form":form,"dates":dates, "message": message})

            # validation of double booking:
            for date in dates:
                if date == booking_date:
                    return render(request, "booking.html", {"form":form,"dates":dates, "message": "ten termin jest już zajęty!"})

            # validation of opening hours:
            # albo zrobic selecta i wyświetlac tylko dostepne godziny w wybranym dniu


            Booking.objects.create(date = booking_date, treatment= treatment, user=user)
            return redirect("/home")
        else:
            return render(request, "booking.html", {"form": form, "dates": dates})


# form = PresenceForm(initial={
#             'day': presence_day})



