from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):

	class Meta:
		model = Signup
		fields = "__all__"

class Login(forms.Form):
	username = forms.CharField(label='Username', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)

'''class SignupForm(forms.Form):
	seller = 'SR'
	buyer = 'BR'
	avilable_permission=(('SR','seller'),('BR','buyer'))
	your_name = forms.CharField(label='Your name', max_length=100)
	email = forms.EmailField()
	username = forms.CharField(label='User name', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	choice = forms.ChoiceField(choices=avilable_permission,label='user type', widget=forms.Select(), required=True)'''
