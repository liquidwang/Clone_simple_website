from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='Sign_Up'),
    path('sign_in/', views.sign_in, name='Sign_In'),
    path('log_out/', views.log_out, name='Log_Out'),
]