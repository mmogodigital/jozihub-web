from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       
    (r'^news/', include('app.news.urls')),
    
    (r'^', include('app.root.urls')),
)