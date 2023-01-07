from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'accounts.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('',include('events.urls')),
    path('',include('startups.urls')),
    path('',include('owners.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)