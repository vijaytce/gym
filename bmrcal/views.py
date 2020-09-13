from django.shortcuts import render

# Create your views here.
def bmr (request):
    return render(request, 'bmr.html')