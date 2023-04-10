from django.shortcuts import render
from django.http import HttpResponse
from .models import Project_details


def home(request):
    return render(request, 'home.html')

def portfolio(request):
    data = Project_details.objects.all()
    return render(request, 'portfolio.html', {'data':data})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')