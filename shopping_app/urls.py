from django.urls import path
from .views import GetName,SuccessView,LoginView,ProductListView,AddDetails,ProductSucessView
from . import views
urlpatterns = [
    path('Sign up',GetName.as_view(), name='sign up'),
    path('successfull',SuccessView.as_view(), name='successfull'),
    path('login',LoginView.as_view(), name='login'),
    path('details',ProductListView.as_view(), name='details'),
    path('add_details',AddDetails.as_view(), name='add_details'),
    path('product_success',ProductSucessView.as_view(), name='product_success'),

]
