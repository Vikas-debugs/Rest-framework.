from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('APIapp.urls')),
    path('admin/', admin.site.urls),
    # your_project/urls.py
    path('captcha/', include('captcha.urls')),  # Add this line
]
