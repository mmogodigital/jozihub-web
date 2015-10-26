from django.conf.urls import patterns, include, url

from app.startups import views

urlpatterns = patterns('',
    url(r'^$',
        views.Startup.as_view(
            template_name='startups/startups.html',
        ),
        name='startups'
    ),
                       
    url(r'^(?P<slug>[-\w]+)/$',
        views.StartupDetail.as_view(
            template_name='startups/startups_detail.html',
        ),
        name='startups_detail'
    ),
)