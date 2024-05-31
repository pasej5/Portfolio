from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'), #path is empty because we want to prefix this in the main urlsfile
]
