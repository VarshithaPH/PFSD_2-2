from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', projecthomepage, name='projecthomepage'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),


]
