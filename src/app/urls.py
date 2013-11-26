from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       
    (r'^news/', include('app.news.urls')),
    (r'^events/', include('app.events.urls')),
    (r'^partners/', include('app.partners.urls')),
    (r'^gallery/', include('app.gallery.urls')),
    
    (r'^', include('app.root.urls')),
)