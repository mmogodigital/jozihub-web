from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('startups/', include('jozihub.startups.urls')),
    url('', include('jozihub.home.urls')),
]
