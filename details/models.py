from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.
def details (request):
    return render (request, 'detail.html')