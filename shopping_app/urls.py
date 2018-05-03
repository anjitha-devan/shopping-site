from django.urls import path
from .views import GetName,SuccessView,LoginView,DetailView
from . import views
urlpatterns = [
    path('Sign up',GetName.as_view(), name='sign up'),
    path('successfull',SuccessView.as_view(), name='successfull'),
    path('login',LoginView.as_view(), name='login'),
    path('details',DetailView.as_view(), name='details'),
]
