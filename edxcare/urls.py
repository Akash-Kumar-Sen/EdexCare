from django.conf import settings
from django.conf.urls.static import static

from .views import index,aboutus,resources,contactus
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',aboutus,name='aboutus'),
    path('resources/',resources,name='resources'),
    path('contactus/',contactus,name='contactus'),
    path('solutions/',include('HomeActions.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
