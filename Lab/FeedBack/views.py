from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def contact123(request):
    return render(request, 'contact.html')


from .models import *
from django.shortcuts import render, redirect


def hello(request):
    return HttpResponse("<center>Welcome to Travel&Tourism Management Page</center>")


def newhomepage(request):
    return render(request, 'NewHomePage.html')


def contactmail(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        Lastname = request.POST.get('Lastname')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        data = contactus(firstname=firstname, Lastname=Lastname, email=email, comments=comments)
        data.save()
        return redirect('newhomepage')
    return render(request, 'contact.html')
