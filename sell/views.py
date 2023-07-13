from django.shortcuts import render
from django.http import HttpResponse
from .models import buy

# Create your views here.
def app(request):
   x=buy.objects.all()
   return render(request, 'index.html',{'x':x})
   return render(request, 'home.html', {'x': x})
def index(request):
    return HttpResponse('<h2>Thank You</h2>')
