from django.urls import path
from . import views
urlpatterns = [
    path('', views.userdata, name='userdata' ),
]
