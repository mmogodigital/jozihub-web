from django.conf.urls import url
from . import views

from jozihub.startups import views

urlpatterns = [
    url('', views.index, name="startups"),
    url('', views.details, name="startups_detail"),
]
