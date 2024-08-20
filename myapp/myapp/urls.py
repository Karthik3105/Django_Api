
from django.contrib import admin
from django.urls import path,include
# from .views import *
# from django.conf import settings
# from django.conf.urls.static import static
from myapp_new import views

urlpatterns = [
    path('resume/',include('myapp_new.urls'))
    # path('admin/', admin.site.urls),
    # path('index/',home),
    # path('about/',about),
    #  path('emp/',include('emp.urls')),
]
