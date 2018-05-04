from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .models import *
from .forms import SignupForm,Login,ItemForm


class IndexView(generic.TemplateView):
    template_name = 'shopping_app/home.html'

class GetName(FormView):
    template_name = 'shopping_app/name.html'
    form_class = SignupForm
    success_url = 'successfull'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessView(generic.TemplateView):
    template_name = 'shopping_app/success.html'


class LoginView(FormView):
    template_name = 'shopping_app/login.html'
    form_class = Login

    def post(self,request):
        login_username = request.POST['username']
        login_password = request.POST['password']

        try:
            name_obj = Signup.objects.get(Username=login_username,Password=login_password)
        except:
            name_obj = None
        if name_obj:
            choice_val = name_obj.User_type
            if choice_val == 'SR': 
                return HttpResponseRedirect('add_details')
            else:
                return HttpResponseRedirect('details')
        else:
            return HttpResponseRedirect('error')


class DetailView(generic.TemplateView):
    template_name = 'shopping_app/detail.html'
class AddDetails(FormView):
    template_name = 'shopping_app/add_details.html'
    form_class = ItemForm
    success_url = 'product_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductSucessView(generic.TemplateView):
    template_name = 'shopping_app/product_success.html'

class ProductListView(generic.ListView):
    template_name = 'shopping_app/detail.html'
    model = ItemDetails


    '''def post(self, request, args, *kwargs):
        print ("dfxghjgfchj")
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
        else:
            return self.form_invalid(form)'''

'''def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        
    else:
        # Return an 'invalid login' error message.
        print("invalid login")'''


'''def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'shopping_app/name.html', {'form': form})'''
