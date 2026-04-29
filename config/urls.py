from django.contrib import admin
from django.urls import path, include # Make sure 'include' is added here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # This tells Django to use core/urls.py for the home page
]
