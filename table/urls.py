from django.urls import path
from . import  views
urlpatterns = [    
    path('',views.table, name='table'),
    path('startapp/',views.table, name='startapp'),
    
]
