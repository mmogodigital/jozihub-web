from django.conf.urls import patterns, include, url

from app.csv_export import views

urlpatterns = patterns('',
    url(r'^users$', views.export_view, name='export'),
)