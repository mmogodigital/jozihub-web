from django.conf.urls import patterns, include, url

from app.services import views

urlpatterns = patterns('',
    url(r'^$',
        views.Services.as_view(
            template_name='services/services.html',
        ),
        name='services'
    ),
                       
    url(r'^(?P<slug>[-\w]+)/$',
        views.ServiceDetail.as_view(
            template_name='services/service_detail.html',
        ),
        name='services_detail'
    ),
)