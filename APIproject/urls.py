
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('APIapp.urls')),
    path('admin/', admin.site.urls),
]
