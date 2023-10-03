from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <- Import the settings from django.conf
from django.conf.urls.static import static  # <- You've already imported this, but this is its standard location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

# This ensures during development, Django serves user-uploaded media files.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
