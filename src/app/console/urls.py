'''
Created on 03 Dec 2013

@author: christina
'''
from django.conf.urls import patterns, url

#from tunobase.corporate.media.console import views, forms
from app.console import views, forms

urlpatterns = patterns('',
    url(r'^$',
        views.ConsoleLanding.as_view(
            template_name='console/landing_page.html'
        ),
        name='console_landing_page'
    ),
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
        views.UsersDelete.as_view(
            template_name='console/users/users_confirm_delete.html'
        ),
        name='console_users_delete'
    ),

    url(r'^users/$',
        views.UsersList.as_view(
            template_name='console/users/users_list.html',
            paginate_by=10
        ),
        name='console_users_list'
    ),
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    # Console: Events
    url(r'^events/create/$',
        views.EventsCreate.as_view(
            form_class=forms.EventsForm,
            template_name='console/events/events_edit.html'
        ),
        name='console_events_create'
    ),

    url(r'^events/update/(?P<pk>\d+)/$',
        views.EventsUpdate.as_view(
            form_class=forms.EventsForm,
            template_name='console/events/events_edit.html'
        ),
        name='console_events_update'
    ),

    url(r'^events/(?P<pk>\d+)/detail/$',
        views.EventsDetail.as_view(
            template_name='console/events/events_detail.html'
        ),
        name='console_events_detail'
    ),

    url(r'^events/delete/(?P<pk>\d+)/$',
        views.EventsDelete.as_view(
            template_name='console/events/events_confirm_delete.html'
        ),
        name='console_events_delete'
    ),

    url(r'^events/$',
        views.EventsList.as_view(
            template_name='console/events/events_list.html',
            paginate_by=10
        ),
        name='console_events_list'
    ),
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    # Console: News
    url(r'^news/create/$',
        views.NewsCreate.as_view(
            form_class=forms.NewsForm,
            template_name='console/news/news_edit.html'
        ),
        name='console_news_create'
    ),

    url(r'^news/update/(?P<pk>\d+)/$',
        views.NewsUpdate.as_view(
            form_class=forms.NewsForm,
            template_name='console/news/news_edit.html'
        ),
        name='console_news_update'
    ),

    url(r'^news/(?P<pk>\d+)/detail/$',
        views.NewsDetail.as_view(
            template_name='console/news/news_detail.html'
        ),
        name='console_news_detail'
    ),

    url(r'^news/delete/(?P<pk>\d+)/$',
        views.NewsDelete.as_view(
            template_name='console/news/news_confirm_delete.html'
        ),
        name='console_news_delete'
    ),

    url(r'^news/$',
        views.NewsList.as_view(
            template_name='console/news/news_list.html',
            paginate_by=10
        ),
        name='console_news_list'
    ),
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    # Console: Jobs
    url(r'^jobs/create/$',
        views.JobsCreate.as_view(
            form_class=forms.JobsForm,
            template_name='console/jobs/jobs_edit.html'
        ),
        name='console_jobs_create'
    ),

    url(r'^jobs/update/(?P<pk>\d+)/$',
        views.JobsUpdate.as_view(
            form_class=forms.JobsForm,
            template_name='console/jobs/jobs_edit.html'
        ),
        name='console_jobs_update'
    ),

    url(r'^jobs/(?P<pk>\d+)/detail/$',
        views.JobsDetail.as_view(
            template_name='console/jobs/jobs_detail.html'
        ),
        name='console_jobs_detail'
    ),

    url(r'^jobs/delete/(?P<pk>\d+)/$',
        views.JobsDelete.as_view(
            template_name='console/jobs/jobs_confirm_delete.html'
        ),
        name='console_jobs_delete'
    ),

    url(r'^jobs/$',
        views.JobsList.as_view(
            template_name='console/jobs/jobs_list.html',
            paginate_by=10
        ),
        name='console_jobs_list'
    ),
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    # Console: Gallery
    url(r'^gallery/create/$',
        views.GalleryCreate.as_view(
            form_class=forms.GalleryForm,
            template_name='console/gallery/gallery_edit.html'
        ),
        name='console_gallery_create'
    ),

    url(r'^gallery/update/(?P<pk>\d+)/$',
        views.GalleryUpdate.as_view(
            form_class=forms.GalleryForm,
            template_name='console/gallery/gallery_edit.html'
        ),
        name='console_gallery_update'
    ),

    url(r'^gallery/(?P<pk>\d+)/detail/$',
        views.GalleryDetail.as_view(
            template_name='console/gallery/gallery_detail.html'
        ),
        name='console_gallery_detail'
    ),

    url(r'^gallery/delete/(?P<pk>\d+)/$',
        views.GalleryDelete.as_view(
            template_name='console/gallery/gallery_confirm_delete.html'
        ),
        name='console_gallery_delete'
    ),

    url(r'^gallery/$',
        views.GalleryList.as_view(
            template_name='console/gallery/gallery_list.html',
            paginate_by=10
        ),
        name='console_gallery_list'
    ),
    #-------------------------------------------------------------------------
    # Console: Flatpages
        url(r'^flatpages/$',
            views.FlatPagesList.as_view(
                template_name='console/flatpages/flatpage_list.html',
            ),
            name='console_flatpage_list'
        ),
        url(r'^flatpages/(?P<pk>\d+)/$',
            views.FlatPagesDetail.as_view(
                template_name='console/flatpages/flatpage_detail.html'
            ),
            name='console_flatpage_detail'
        ),
        url(r'^flatpages/update/(?P<pk>\d+)/$',
            views.FlatPagesUpdate.as_view(
                form_class=forms.FlatPageForm,
                template_name='console/flatpages/flatpage_edit.html',
            ),
            name='console_flatpage_edit'
        ),
)
