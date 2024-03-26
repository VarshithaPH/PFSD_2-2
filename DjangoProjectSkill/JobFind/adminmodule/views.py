from django.shortcuts import render

# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html')