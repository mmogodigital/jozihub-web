from django.conf.urls import patterns, include, url
from django.contrib.flatpages.views import flatpage

from honeypot.decorators import check_honeypot

from tunobase.age_gate.decorators import age_gated

from app.root import views, forms

urlpatterns = patterns('',
    url(r'^$',
        views.Index.as_view(
            template_name='root/index.html',
        ),
        name='index'
    ),
                       
    url(r'^apply/$', 
        check_honeypot(views.Apply.as_view(
            template_name='root/apply.html',
            form_class=forms.ApplyForm
        )),
        name='apply'
    ),
                       
    url(r'^apply/success/$', 
        views.ApplySuccess.as_view(
            template_name='root/apply_success.html'
        ),
        name='apply_success'
    ),
)