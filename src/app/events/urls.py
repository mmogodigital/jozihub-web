from django.conf.urls import patterns, include, url

#from tunobase.corporate.media import views as media_views
from app.events import views, forms


urlpatterns = patterns('',
    url(r'^$',
        views.Events.as_view(
            template_name='events/events.html',
        ),
        name='events'
    ),
    url(r'^venue_hire/$', 
        views.VenueHire.as_view(
            form_class=forms.VenueHireForm,
            template_name='events/venue_hire.html'
        ),
        name='venue_hire'
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        views.EventDetail.as_view(
            template_name='events/event_detail.html',
        ),
        name='event_detail'
    ),
)
