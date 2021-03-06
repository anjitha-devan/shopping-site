from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, render_to_response
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import SignupForm, Login, ItemForm
from django.template import RequestContext
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.core.signing import Signer
import datetime
from django.urls import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from shopping_app.mixin import ActiveOnlyMixin


class IndexView(generic.TemplateView):
    template_name = 'shopping_app/home.html'


class UserSignup(FormView):
    template_name = 'shopping_app/name.html'
    form_class = SignupForm
    success_url = 'login'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.password = make_password(obj.password)
        obj.is_active = False
        form.save()
        signer = Signer()
        signed_value = signer.sign(obj.email)
        key = ''.join(signed_value.split(':')[1:])
        reg_obj = Registration.objects.create(user=obj, key=key)
        msg_html = render_to_string('shopping_app/email-act.html', {'key': key})

        send_mail("123", "123", 'anjitha.test@gmail.com', [obj.email], html_message=msg_html, fail_silently=False)
        return super().form_valid(form)


# @login_required
# @method_decorator(login_required, name='dispatch')
class SuccessView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'shopping_app/success.html'


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
                if signup_obj.User_type == 'SR':
                    return HttpResponseRedirect('add_details')
                else:
                    return HttpResponseRedirect('details')
        else:
            return HttpResponse("Invalid user login")
    else:
        # Bad login details were provided. So we can't log the user in.
        # print ("Invalid login details: {0}, {1}".format(username, password))
        # return HttpResponse("Invalid login details supplied.")
        return render_to_response('user/profile.html', {}, context)


# @login_required
# @method_decorator(login_required, name='dispatch')
class AddDetails(LoginRequiredMixin, ActiveOnlyMixin, CreateView):
    template_name = 'shopping_app/add_details.html'
    model = ItemDetails
    fields = ('Upload_image', 'Product_name', 'Discription', 'Price')
    success_url = 'product_success'

    def form_valid(self, form):
        obj = form.save()
        obj.user = self.request.user
        return super(AddDetails, self).form_valid(form)


# @login_required
# @method_decorator(login_required, name='dispatch')
class ProductSucessView(LoginRequiredMixin, ActiveOnlyMixin, generic.ListView):
    template_name = 'shopping_app/uploaded-listing.html'
    paginate_by = 6

    def get_queryset(self):
        return ItemDetails.objects.filter(user=self.request.user)


# @login_required
# @method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    template_name = 'shopping_app/detail.html'
    model = ItemDetails
    paginate_by = 6


# @login_required
class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shopping_app/product_detail.html'
    model = ItemDetails


class RegistrationSuccess(TemplateView):
    template_name = 'shopping_app/registration-success.html'

    def get(self, request, *args, **kwargs):
        key = self.kwargs.get("key")
        try:
            reg_obj = Registration.objects.get(key=key)
            obj = Signup.objects.get(id=reg_obj.user_id)
            obj.is_active = True
            obj.save()
            context = {'user': reg_obj, 'status': True}
            return self.render_to_response(context)
        except Registration.DoesNotExist:
            return self.render_to_response({'status': False})


class DeleteProduct(LoginRequiredMixin, ActiveOnlyMixin, DeleteView):
    model = ItemDetails
    success_url = reverse_lazy('product_success')


class EditProduct(LoginRequiredMixin, ActiveOnlyMixin, UpdateView):
    template_name = 'shopping_app/edit-product.html'
    model = ItemDetails
    fields = ['Upload_image', 'Product_name', 'Discription', 'Price']
    success_url = reverse_lazy('product_success')
