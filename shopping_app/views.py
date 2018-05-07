from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView ,ListView,DetailView
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import SignupForm,Login,ItemForm
from django.template import RequestContext
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class IndexView(generic.TemplateView):
    template_name = 'shopping_app/home.html'

class UserSignup(FormView):
    template_name = 'shopping_app/name.html'
    form_class = SignupForm
    success_url = 'successfull'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.password = make_password( obj.password )

        form.save()
        return super().form_valid(form)

# @login_required
@method_decorator(login_required, name='dispatch')
class SuccessView(generic.TemplateView):
    template_name = 'shopping_app/success.html'

class LogoutView(FormView):

    def get(self, request, args, *kwargs):
        #print (self.request.user.username)
        logout(request)
        return HttpResponseRedirect('/')

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                signup_obj = Signup.objects.get(username=username)
                print(signup_obj.User_type,'dfghj')
                if signup_obj.User_type =='SR':
                    return HttpResponseRedirect('add_details')
                else:
                    return HttpResponseRedirect('details')
        else:
            return HttpResponse("xxx.")
    else:
        # Bad login details were provided. So we can't log the user in.
        print ("Invalid login details: {0}, {1}".format(username, password))
        return HttpResponse("Invalid login details supplied.")
    '''else:
                    return render_to_response('user/profile.html', {}, context)'''


'''class LoginView(FormView):
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
'''

'''class DetailView(generic.TemplateView):
    template_name = 'shopping_app/detail.html' '''
# @login_required
class AddDetails(FormView):
    template_name = 'shopping_app/add_details.html'
    form_class = ItemForm
    success_url = 'product_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
# @login_required
class ProductSucessView(generic.TemplateView):
    template_name = 'shopping_app/product_success.html'
# @login_required
class ProductListView(ListView):
    template_name = 'shopping_app/detail.html'
    model = ItemDetails
# @login_required
class ProductDetailView(DetailView):
    template_name = 'shopping_app/product_detail.html'
    model = ItemDetails

