from django.conf.urls import patterns, include, url

from app.partners import views

urlpatterns = patterns('',
    url(r'^$',
        views.Partners.as_view(
            template_name='partners/partners.html',
        ),
        name='partners'
    ),
)