from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


# Create your views here.
def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        try:
            user = User.objects.create(username=username, password=password, email=email, phone_number=phone_number)
            # Redirect to dashboard or homepage upon successful sign up
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, 'Failed to sign up. Please try again.')
            return render(request, 'signup.html')

    return render(request, 'signup.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('success')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')