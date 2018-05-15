from django import forms
from .models import Signup, ItemDetails
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = Signup
        fields = ['first_name', 'last_name', 'email', 'username', 'User_type']


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username'}), label='Username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemDetails
        exclude = ['user']
