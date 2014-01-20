from django.conf.urls import patterns, include, url

from tunobase.corporate.media import views as media_views


urlpatterns = patterns('',
    url(r'^$',
        media_views.Events.as_view(
            template_name='events/events.html',
        ),
        name='events'
    ),
                       
    url(r'^(?P<slug>[-\w]+)/$',
        media_views.EventDetail.as_view(
            template_name='events/event_detail.html',
        ),
        name='event_detail'
    ),
)
