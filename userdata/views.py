from django.shortcuts import render
from .models import userdata


# Create your views here
def userdataa (request):
   
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        weight=request.POST['weight']
        height=request.POST['height']
        bmi=request.POST['bmi']
        print(name,age,weight,height,bmi)
        num=userdata.objects.create(name=name,age=age,weight=weight,height=height,bmi=bmi)
        num.save()
        
                
    return render(request, 'userdata.html')