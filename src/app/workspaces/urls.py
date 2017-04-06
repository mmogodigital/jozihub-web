from django.conf.urls import patterns, include, url

from app.workspaces import views

urlpatterns = patterns('',
    url(r'^$',
        views.Workspaces.as_view(
            template_name='workspaces/workspaces.html',
        ),
        name='workspaces'
    ),

    url(r'^(?P<slug>[-\w]+)/$',
        views.WorkspaceDetail.as_view(
            template_name='workspaces/workspace_detail.html',
        ),
        name='workspaces_detail'
    ),
)
