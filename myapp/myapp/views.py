from django.http import HttpResponse
import datetime
from django.shortcuts import render





def home(request):
    date = datetime.datetime.now()
    print("test function is called form view")
    #return HttpResponse("<h1>Hello this is index page</h1>"+str(date))
    return render(request,"home.html")

def about(request):
    
    #print("test function is called form view")
     return render(request,"about.html")   