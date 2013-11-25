from django.conf.urls import patterns, include, url

from app.events import views

urlpatterns = patterns('',
    url(r'^$',
        views.Events.as_view(
            template_name='events/events.html',
        ),
        name='events'
    ),
                       
    url(r'^(?P<slug>[-\w]+)/$',
        views.EventDetail.as_view(
            template_name='events/event_detail.html',
        ),
        name='event_detail'
    ),
)