'''
Created on 03 Dec 2013

@author: christina
'''
from django.conf.urls import patterns, url

#from tunobase.corporate.media.console import views, forms
from app.console import views, forms

urlpatterns = patterns('',
    url(r'^$',
        views.ConsoleLanding.as_view(),
        name='console_landing_page'
    ),

#    #-------------------------------------------------------------------------
#    # Console: Events
#    url(r'^events/create/$',
#        views.EventsCreate.as_view(
#            form_class=forms.EventsForm,
#            template_name='console/events/events_edit.html'
#        ),
#        name='console_events_create'
#    ),
#
#    url(r'^events/update/(?P<pk>\d+)/$',
#        views.EventsUpdate.as_view(
#            form_class=forms.EventsForm,
#            template_name='console/events/events_edit.html'
#        ),
#        name='console_events_update'
#    ),
#
#    url(r'^events/(?P<pk>\d+)/detail/$',
#        views.EventsDetail.as_view(
#            template_name='console/events/events_detail.html'
#        ),
#        name='console_events_detail'
#    ),
#
#    url(r'^events/delete/(?P<pk>\d+)/$',
#        views.EventsDelete.as_view(),
#        name='console_events_delete'
#    ),
#
#    url(r'^events/list/$',
#        views.EventsList.as_view(
#            template_name='console/events/events_list.html',
#            paginate_by=20
#        ),
#        name='console_events_list'
#    ),
#    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    # Console: Users
    url(r'^users/create/$',
        views.UsersCreate.as_view(
            form_class=forms.UsersForm,
            template_name='console/users/users_edit.html'
        ),
        name='console_users_create'
    ),

    url(r'^users/update/(?P<pk>\d+)/$',
        views.UsersUpdate.as_view(
            form_class=forms.UsersForm,
            template_name='console/users/users_edit.html'
        ),
        name='console_users_update'
    ),

    url(r'^users/(?P<pk>\d+)/detail/$',
        views.UsersDetail.as_view(
            template_name='console/users/users_detail.html'
        ),
        name='console_users_detail'
    ),

    url(r'^users/delete/(?P<pk>\d+)/$',
        views.UsersDelete.as_view(),
        name='console_users_delete'
    ),

    url(r'^users/list/$',
        views.UsersList.as_view(
            template_name='console/users/users_list.html',
            paginate_by=20
        ),
        name='console_users_list'
    ),
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
#    # Console: News
#    url(r'^events/create/$',
#        views.EventsCreate.as_view(
#            form_class=forms.EventsForm,
#            template_name='console/events/events_edit.html'
#        ),
#        name='console_events_create'
#    ),
#
#    url(r'^events/update/(?P<pk>\d+)/$',
#        views.EventsUpdate.as_view(
#            form_class=forms.EventsForm,
#            template_name='console/events/events_edit.html'
#        ),
#        name='console_events_update'
#    ),
#
#    url(r'^events/(?P<pk>\d+)/detail/$',
#        views.EventsDetail.as_view(
#            template_name='console/events/events_detail.html'
#        ),
#        name='console_events_detail'
#    ),
#
#    url(r'^events/delete/(?P<pk>\d+)/$',
#        views.EventsDelete.as_view(),
#        name='console_events_delete'
#    ),
#
#    url(r'^events/list/$',
#        views.EventsList.as_view(
#            template_name='console/events/events_list.html',
#            paginate_by=20
#        ),
#        name='console_events_list'
#    ),
#    #-------------------------------------------------------------------------
#
#    #-------------------------------------------------------------------------
#    # Console: Gallery
#    url(r'^events/create/$',
#        views.EventsCreate.as_view(
#            form_class=forms.EventsForm,
#            template_name='console/events/events_edit.html'
#        ),
#        name='console_events_create'
#    ),
#
#    url(r'^events/update/(?P<pk>\d+)/$',
#        views.EventsUpdate.as_view(
#            form_class=forms.EventsForm,
#            template_name='console/events/events_edit.html'
#        ),
#        name='console_events_update'
#    ),
#
#    url(r'^events/(?P<pk>\d+)/detail/$',
#        views.EventsDetail.as_view(
#            template_name='console/events/events_detail.html'
#        ),
#        name='console_events_detail'
#    ),
#
#    url(r'^events/delete/(?P<pk>\d+)/$',
#        views.EventsDelete.as_view(),
#        name='console_events_delete'
#    ),
#
#    url(r'^events/list/$',
#        views.EventsList.as_view(
#            template_name='console/events/events_list.html',
#            paginate_by=20
#        ),
#        name='console_events_list'
#    ),
#    #-------------------------------------------------------------------------
)
