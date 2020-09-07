from django.shortcuts import render
from .models import data,Name,test

# Create your views here.

def index (request):
        if request.method=="POST":
                print("this is post")
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                #print(firstname,lastname)
                ins =test(firstname=firstname,lastname=lastname)
                ins.save()
                print('the data inserted sucessfully')
                
       
        return render(request, 'home.html')