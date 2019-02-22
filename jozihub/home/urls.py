from django.conf.urls import url

from jozihub.home import views

urlpatterns = [
    url('', views.index, name="homepage"),
]
