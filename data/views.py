from django.shortcuts import render
from .models import data,Name 

# Create your views here.

def index (request):
    
        
        return render(request, 'home.html',  )