from django.conf.urls import url

from jozihub.partners import views

urlpatterns = [
    url('', views.index, name="partners"),
] 
