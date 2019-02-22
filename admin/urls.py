from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('startups/', include('jozihub.startups.urls')),
    url('events/', include('jozihub.events.urls')),
    url('services/', include('jozihub.services.urls')),
    url('partners/', include('jozihub.partners.urls')),
    url('console/', include('jozihub.console.urls')),
    url('authentication/', include('jozihub.authentication.urls')),
    url('', include('jozihub.home.urls')),
]
