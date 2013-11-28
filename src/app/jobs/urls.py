from django.conf.urls import patterns, include, url
from django.views import generic as generic_views

from app.jobs import views

urlpatterns = patterns('',    
    url(r'^$',
        generic_views.TemplateView.as_view(
                template_name='jobs/jobs.html',
        ),
        name='jobs'
    ),

    url(r'^job/detail/$',
        generic_views.TemplateView.as_view(
                template_name='jobs/job_detail.html',
        ),
        name='job_detail'
    ),

    url(r'^post/job/$',
        generic_views.TemplateView.as_view(
                template_name='jobs/post_job.html',
        ),
        name='post_job'
    ),
                       
)