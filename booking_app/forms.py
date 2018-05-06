from django.contrib.auth.models import User

from booking_app.models import Treatment, Booking
from django import forms
import re
from bootstrap_datepicker.widgets import DatePicker


class AddClientForm(forms.Form):
    first_name= forms.CharField(label="imię",max_length=64)
    last_name= forms.CharField(label="nazwisko",max_length=64)
    password = forms.CharField(label="hasło", widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="powtórz hasło", widget=forms.PasswordInput)
    username = forms.IntegerField(label="nr telefonu")

    def clean_username(self):
        number = str(self.cleaned_data['username'])
        number = re.sub(r"\D", "", number)
        pattern = r"^\d{9}$"
        if not re.match(pattern, number):
            raise forms.ValidationError("Podaj poprawny numer")
        return number


class AddTreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = "__all__"


class ClientLoginForm(forms.Form):
    username = forms.IntegerField(label="nr telefonu")
    password = forms.CharField(label="hasło", widget=forms.PasswordInput)


class BookingForm(forms.Form):

    date = forms.DateField(widget=DatePicker(
            options={
                "maxViewMode": 0,
                "todayBtn": True,
                "language": "pl-PL",
                "daysOfWeekDisabled": "0,7",
                "daysOfWeekHighlighted": "1,2,3,4,5,6",
                "calendarWeeks": True,
                "todayHighlight": True,
                "format": "yyyy-mm-dd",
                "autoclose": True,
            }
        ))
    time = forms.TimeField()


# "YYYY-MM-DD HH:mm",



"""
 
 # number= filter(lambda x: x.isdigit(), number)
"""

