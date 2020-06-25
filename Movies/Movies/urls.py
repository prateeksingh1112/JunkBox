from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.index , name="home"),
    path('admin/', admin.site.urls),
    path('movi/' , include('movi.urls')),
]
# urlpatterns = urlpatterns + staticfiles_urlpatterns

