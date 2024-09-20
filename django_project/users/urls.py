from django.urls import path 
from . import views

urlpatterns= [
    path ('registercust/',views.registercust, name= 'registercust'),
    path ('login/',views.login, name= 'login'),
    path ('logout/',views.logout, name= 'logout'),
]