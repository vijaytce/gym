from django.shortcuts import render
from .models import data,Name,test

# Create your views here.

def index (request):      
               
                
       
                return render(request, template_name='userdata.html')