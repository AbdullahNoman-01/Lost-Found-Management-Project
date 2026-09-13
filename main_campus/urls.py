from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('authentications/', include('authentications.urls')),
    path('lost_items/', include('lost_items.urls')),
    path('found_items/', include('found_items.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
