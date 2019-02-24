# from django.views.generic.base import TemplateView
# from django.contrib.admin.views.decorators import staff_member_required
# from honeypot.decorators import check_honeypot

from django.conf.urls import url

from jozihub.authentication import views

urlpatterns = [
    url('secure/register', views.registration, name="registration"),
    url('secure/login', views.login, name="login"),
]
