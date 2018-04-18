from django.contrib.auth.models import User

from booking_app.models import Treatment
from django import forms
import re


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


        # czy zmienić to i dodać whidgeta na password????
        # password = forms.CharField(label = "password", widget=forms.PasswordInput)

 # number= filter(lambda x: x.isdigit(), number)