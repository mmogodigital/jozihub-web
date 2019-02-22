from django.conf.urls import url

from jozihub.services import views

urlpatterns = [
    url('', views.index, name="services"),
]
