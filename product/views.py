from django.shortcuts import render
from django.http import HttpResponse
from .models import sell

# Create your views here.
def index(request):
   x=sell.objects.all()
   return render(request, 'set.html',{'x':x})
def about(request):
    return HttpResponse('<h2>HELLO</h2>')

