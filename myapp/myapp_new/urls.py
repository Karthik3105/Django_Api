from django.contrib import admin
from django.urls import path,include
from .views import *
from myapp_new import views


urlpatterns = [
    path('',views.HomeView.as_view()),
    
]