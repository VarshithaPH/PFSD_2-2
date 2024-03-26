from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    path('hello/', hello, name='Hello'),
    path('',newhomepage,name='newhomepage'),
    path('contact123/', contact123, name='contact123'),
    path('contactmail', contactmail, name='contactmail'),
]
