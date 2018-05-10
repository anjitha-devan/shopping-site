from django import forms
from .models import Signup, ItemDetails


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'User_type']


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username'}), label='Username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemDetails
        exclude = ['user']


'''class SignupForm(forms.Form):
	seller = 'SR'
	buyer = 'BR'
	avilable_permission=(('SR','seller'),('BR','buyer'))
	your_name = forms.CharField(label='Your name', max_length=100)
	email = forms.EmailField()
	username = forms.CharField(label='User name', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	choice = forms.ChoiceField(choices=avilable_permission,label='user type', widget=forms.Select(), required=True)'''
