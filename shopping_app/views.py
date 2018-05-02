from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login

class IndexView(generic.TemplateView):
    template_name = 'shopping_app/home.html'

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        
    else:
        # Return an 'invalid login' error message.
        print("invalid login")