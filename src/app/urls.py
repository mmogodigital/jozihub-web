from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^authentication/', include('app.authentication.urls')),
    (r'^console/', include('app.console.urls')),
    (r'^news/', include('app.news.urls')),
    (r'^events/', include('app.events.urls')),
    (r'^partners/', include('app.partners.urls')),
    (r'^gallery/', include('app.gallery.urls')),
    (r'^jobs/', include('app.jobs.urls')),
    (r'^startups/', include('app.startups.urls')),
    (r'^services/', include('app.services.urls')),
    (r'^', include('app.root.urls')),
)
