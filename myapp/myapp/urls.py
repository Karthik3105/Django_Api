
from django.contrib import admin
from django.urls import path,include
# from .views import *
from django.conf import settings
# from django.conf.urls.static import static
from myapp_new import views
from django.conf.urls.static import static

urlpatterns = [
    path('resume/',include('myapp_new.urls'))
    path('admin/', admin.site.urls),
    # path('index/',home),
    # path('about/',about),
    #  path('emp/',include('emp.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
