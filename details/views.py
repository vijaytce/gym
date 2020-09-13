from django.shortcuts import render
from userdata.models import userdata

# Create your views here.
from django.shortcuts import render

# Create your views here.
def details (request):
    usersdata=userdata.objects.all()
    return render (request, 'detail.html', {'data':usersdata}) 