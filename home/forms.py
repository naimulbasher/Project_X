from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Bus, Bus_Route, Bus_Stopage

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddBusStopage(forms.ModelForm):
    class Meta:
        model = Bus_Stopage
        fields = ['stopage_name', 'location']

class AddBusRoute(forms.ModelForm):
    class Meta:
        model = Bus_Route
        fields = ['bus_stopage', 'bus']
