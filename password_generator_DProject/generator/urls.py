from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('password_generator.urls')),
    path('home/', include('password_generator.urls')),
    path('password/', include('password_generator.urls')),
    path('about/', include('password_generator.urls')),
    path('admin/', admin.site.urls),
]
