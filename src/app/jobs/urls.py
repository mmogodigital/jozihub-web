from django.conf.urls import patterns, include, url
from django.views import generic as generic_views

from honeypot.decorators import check_honeypot

from app.jobs import views, form

urlpatterns = patterns('',    
    url(r'^$',
        generic_views.JobList.as_view(
                template_name='jobs/jobs.html',
        ),
        name='list_jobs'
    ),
    url(r'^postjob/$', 
        check_honeypot(views.PostJob.as_view(
            template_name='jobs/post_a_job.html',
            form_class=forms.PostJobForm
        )),
        name='post_job'
    ),
                       
    url(r'^postjob/success/$', 
        views.PostJobSuccess.as_view(
            template_name='jobs/success.html'
        ),
        name='success'
    ),
                       
)
