from django.shortcuts import render
from .models import data,Name,test

# Create your views here.

def index (request):     
        name =request.POST.get("")
                
       
        return render(request, template_name='home.html')