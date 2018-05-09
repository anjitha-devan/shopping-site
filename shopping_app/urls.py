from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  *

urlpatterns = [
    path('Sign up', UserSignup.as_view(), name='sign up'),
    path('successfull',SuccessView.as_view(), name='successfull'),
    path('login/',auth_views.login, {'template_name': 'registration/login.html'},name='login'),
    path('userlogin',user_login, name='user_login'),
    path('details',ProductListView.as_view(), name='details'),
    path('<int:pk>/',ProductDetailView.as_view(), name='productdetails'),
    path('add_details',AddDetails.as_view(), name='add_details'),
    path('product_success',ProductSucessView.as_view(), name='product_success'),
    path('registration/<str:key>',  RegistrationSuccess.as_view(), name='product_success'),

]
