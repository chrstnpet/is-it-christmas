from django.contrib import admin
from django.urls import path, include

from newyear import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newyear.urls')),
]
