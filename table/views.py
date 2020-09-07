from django.shortcuts import render
from data.models import dataset
# Create your views here.


def table (request):
    
    data = dataset.objects.all()
    
    
    return render (request, 'table.html',{'data':data})    