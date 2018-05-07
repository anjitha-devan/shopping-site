from django.urls import path
from django.contrib.auth.views import login
from .views import  UserSignup,SuccessView,ProductListView,AddDetails,ProductSucessView,user_login, ProductDetailView,LogoutView

from . import views
urlpatterns = [
    path('Sign up', UserSignup.as_view(), name='sign up'),
    path('successfull',SuccessView.as_view(), name='successfull'),
    path('login/',login,name='login'),
    path('userlogin',user_login, name='user_login'),
    path('details',ProductListView.as_view(), name='details'),
    path('<int:pk>/',ProductDetailView.as_view(), name='productdetails'),
    path('add_details',AddDetails.as_view(), name='add_details'),
    path('product_success',ProductSucessView.as_view(), name='product_success'),
]
