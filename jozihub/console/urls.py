# from django.conf.urls import patterns, url

# from tunobase.corporate.media.console import views, forms
# from app.authentication.models import EndUser
from jozihub.console import views, forms

from django.conf.urls import url, include
# from jozihub.events import views, forms

urlpatterns = [
    url(r'^$', views.ConsoleLanding, name="console_landing_page"),

    # url(r'^users/create/$', views.UsersCreate, name="console_users_create"),
    # url(r'^users/update/(?P<pk>\d+)/$', views.UsersUpdate, name="console_users_update"),
    # url(r'^users/(?P<pk>\d+)/details/$', views.UsersDetails, name="console_users_detail"),
    # url(r'^users/delete/(?P<pk>\d+)/$', views.UsersDelete, name="console_users_delete"),
    # url(r'^users/$', views.UsersList, name="console_users_list"),
    # url(r'^export/$', views.UsersExport, name="console_users_export"),

    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------

    # url(r'^events/create/$', views.EventsCreate, name="console_events_create"),
    # url(r'^events/update/(?P<pk>\d+)/$', views.EventsUpdate, name="console_events_update"),
    # url(r'^events/(?P<pk>\d+)/details/$', views.EventsDetails, name="console_events_detail"),
    # url(r'^events/delete/(?P<pk>\d+)/$', views.EventsDelete, name="console_events_delete"),
    # url(r'^events/$', views.EventsList, name="console_events_list"),

    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------

    # url(r'^jobs/create/$', views.JobsCreate, name="console_jobs_create"),
    # url(r'^jobs/update/(?P<pk>\d+)/$', views.JobsUpdate, name="console_jobs_update"),
    # url(r'^jobs/(?P<pk>\d+)/details/$', views.JobsDetails, name="console_jobs_detail"),
    # url(r'^jobs/delete/(?P<pk>\d+)/$', views.JobsDelete, name="console_jobs_delete"),
    # url(r'^jobs/$', views.JobsList, name="console_jobs_list"),
]

# urlpatterns = patterns('',
#     # Console: Users
#     url(r'^users/create/$',
#         views.UsersCreate.as_view(
#             form_class=forms.UsersForm,
#             template_name='console/users/users_edit.html'
#         ),
#         name='console_users_create'
#     ),

#     url(r'^users/update/(?P<pk>\d+)/$',
#         views.UsersUpdate.as_view(
#             form_class=forms.UsersForm,
#             template_name='console/users/users_edit.html'
#         ),
#         name='console_users_update'
#     ),

#     url(r'^users/(?P<pk>\d+)/detail/$',
#         views.UsersDetail.as_view(
#             template_name='console/users/users_detail.html'
#         ),
#         name='console_users_detail'
#     ),

#     url(r'^users/delete/(?P<pk>\d+)/$',
#         views.UsersDelete.as_view(
#             template_name='console/users/users_confirm_delete.html'
#         ),
#         name='console_users_delete'
#     ),

#     url(r'^users/$',
#         views.UsersList.as_view(
#             template_name='console/users/users_list.html',
#             paginate_by=10
#         ),
#         name='console_users_list'
#     ),

#     url(r'^export/$',
#         views.UserExport.as_view(
#             queryset=EndUser.objects.all(),
#         ),
#         name='console_user_export'
#     ),
#     #-------------------------------------------------------------------------

#     #-------------------------------------------------------------------------
#     # Console: Events
#     url(r'^events/create/$',
#         views.EventsCreate.as_view(
#             form_class=forms.EventsForm,
#             template_name='console/events/events_edit.html'
#         ),
#         name='console_events_create'
#     ),

#     url(r'^events/update/(?P<pk>\d+)/$',
#         views.EventsUpdate.as_view(
#             form_class=forms.EventsForm,
#             template_name='console/events/events_edit.html'
#         ),
#         name='console_events_update'
#     ),

#     url(r'^events/(?P<pk>\d+)/detail/$',
#         views.EventsDetail.as_view(
#             template_name='console/events/events_detail.html'
#         ),
#         name='console_events_detail'
#     ),

#     url(r'^events/delete/(?P<pk>\d+)/$',
#         views.EventsDelete.as_view(
#             template_name='console/events/events_confirm_delete.html'
#         ),
#         name='console_events_delete'
#     ),

#     url(r'^events/$',
#         views.EventsList.as_view(
#             template_name='console/events/events_list.html',
#             paginate_by=10
#         ),
#         name='console_events_list'
#     ),
#     #-------------------------------------------------------------------------

#     #-------------------------------------------------------------------------
#     # Console: News
#     url(r'^news/create/$',
#         views.NewsCreate.as_view(
#             form_class=forms.NewsForm,
#             template_name='console/news/news_edit.html'
#         ),
#         name='console_news_create'
#     ),

#     url(r'^news/update/(?P<pk>\d+)/$',
#         views.NewsUpdate.as_view(
#             form_class=forms.NewsForm,
#             template_name='console/news/news_edit.html'
#         ),
#         name='console_news_update'
#     ),

#     url(r'^news/(?P<pk>\d+)/detail/$',
#         views.NewsDetail.as_view(
#             template_name='console/news/news_detail.html'
#         ),
#         name='console_news_detail'
#     ),

#     url(r'^news/delete/(?P<pk>\d+)/$',
#         views.NewsDelete.as_view(
#             template_name='console/news/news_confirm_delete.html'
#         ),
#         name='console_news_delete'
#     ),

#     url(r'^news/$',
#         views.NewsList.as_view(
#             template_name='console/news/news_list.html',
#             paginate_by=10
#         ),
#         name='console_news_list'
#     ),
#     #-------------------------------------------------------------------------

#     #-------------------------------------------------------------------------
#     # Console: Jobs
#     url(r'^jobs/create/$',
#         views.JobsCreate.as_view(
#             form_class=forms.JobsForm,
#             template_name='console/jobs/jobs_edit.html'
#         ),
#         name='console_jobs_create'
#     ),

#     url(r'^jobs/update/(?P<pk>\d+)/$',
#         views.JobsUpdate.as_view(
#             form_class=forms.JobsForm,
#             template_name='console/jobs/jobs_edit.html'
#         ),
#         name='console_jobs_update'
#     ),

#     url(r'^jobs/(?P<pk>\d+)/detail/$',
#         views.JobsDetail.as_view(
#             template_name='console/jobs/jobs_detail.html'
#         ),
#         name='console_jobs_detail'
#     ),

#     url(r'^jobs/delete/(?P<pk>\d+)/$',
#         views.JobsDelete.as_view(
#             template_name='console/jobs/jobs_confirm_delete.html'
#         ),
#         name='console_jobs_delete'
#     ),

#     url(r'^jobs/$',
#         views.JobsList.as_view(
#             template_name='console/jobs/jobs_list.html',
#             paginate_by=10
#         ),
#         name='console_jobs_list'
#     ),
#     #-------------------------------------------------------------------------

#     #-------------------------------------------------------------------------
#     # Console: Gallery
#     url(r'^gallery/create/$',
#         views.GalleryCreate.as_view(
#             form_class=forms.GalleryForm,
#             template_name='console/gallery/gallery_edit.html'
#         ),
#         name='console_gallery_create'
#     ),

#     url(r'^gallery/update/(?P<pk>\d+)/$',
#         views.GalleryUpdate.as_view(
#             form_class=forms.GalleryForm,
#             template_name='console/gallery/gallery_edit.html'
#         ),
#         name='console_gallery_update'
#     ),

#     url(r'^gallery/(?P<pk>\d+)/detail/$',
#         views.GalleryDetail.as_view(
#             template_name='console/gallery/gallery_detail.html'
#         ),
#         name='console_gallery_detail'
#     ),

#     url(r'^gallery/delete/(?P<pk>\d+)/$',
#         views.GalleryDelete.as_view(
#             template_name='console/gallery/gallery_confirm_delete.html'
#         ),
#         name='console_gallery_delete'
#     ),

#     url(r'^gallery/$',
#         views.GalleryList.as_view(
#             template_name='console/gallery/gallery_list.html',
#             paginate_by=10
#         ),
#         name='console_gallery_list'
#     ),
#     #-------------------------------------------------------------------------

#     #-------------------------------------------------------------------------
#     # Console: Startups
#     url(r'^startups/create/$',
#         views.StartupCreate.as_view(
#             form_class=forms.StartupForm,
#             template_name='console/startups/startups_edit.html'
#         ),
#         name='console_startups_create'
#     ),

#     url(r'^startups/update/(?P<pk>\d+)/$',
#         views.StartupUpdate.as_view(
#             form_class=forms.StartupForm,
#             template_name='console/startups/startups_edit.html'
#         ),
#         name='console_startups_update'
#     ),

#     url(r'^startups/(?P<pk>\d+)/detail/$',
#         views.StartupDetail.as_view(
#             template_name='console/startups/startups_detail.html'
#         ),
#         name='console_startups_detail'
#     ),

#     url(r'^startups/delete/(?P<pk>\d+)/$',
#         views.StartupDelete.as_view(
#             template_name='console/startups/startups_confirm_delete.html'
#         ),
#         name='console_startups_delete'
#     ),

#     url(r'^startups/$',
#         views.StartupList.as_view(
#             template_name='console/startups/startups_list.html',
#             paginate_by=10
#         ),
#         name='console_startups_list'
#     ),
#     #-------------------------------------------------------------------------

#     #-------------------------------------------------------------------------
#     # Console: Partners
#     url(r'^partners/create/$',
#         views.PartnerCreate.as_view(
#             form_class=forms.PartnerForm,
#             template_name='console/partners/partners_edit.html'
#         ),
#         name='console_partners_create'
#     ),

#     url(r'^partners/update/(?P<pk>\d+)/$',
#         views.PartnerUpdate.as_view(
#             form_class=forms.PartnerForm,
#             template_name='console/partners/partners_edit.html'
#         ),
#         name='console_partners_update'
#     ),

#     url(r'^partners/(?P<pk>\d+)/detail/$',
#         views.PartnerDetail.as_view(
#             template_name='console/partners/partners_detail.html'
#         ),
#         name='console_partners_detail'
#     ),

#     url(r'^partners/delete/(?P<pk>\d+)/$',
#         views.PartnerDelete.as_view(
#             template_name='console/partners/partners_confirm_delete.html'
#         ),
#         name='console_partners_delete'
#     ),

#     url(r'^partners/$',
#         views.PartnerList.as_view(
#             template_name='console/partners/partners_list.html',
#             paginate_by=10
#         ),
#         name='console_partners_list'
#     ),

#     #-------------------------------------------------------------------------
# # TODO Create service form
#     # Console: Services
#         url(r'^services/$',
#             views.ServiceList.as_view(
#                 template_name='console/services/services_list.html',
#             ),
#             name='console_services_list'
#         ),

#         url(r'^services/create/$',
#             views.ServiceCreate.as_view(
#                 form_class=forms.ServiceForm,
#                 template_name='console/services/service_edit.html'
#             ),
#             name='console_service_create'
#         ),

#         url(r'^services/update/(?P<pk>\d+)/$',
#             views.ServiceUpdate.as_view(
#                 form_class=forms.ServiceForm,
#                 template_name='console/services/service_edit.html'
#             ),
#             name='console_service_update'
#         ),

#         url(r'^services/(?P<pk>\d+)/detail/$',
#             views.ServiceDetail.as_view(
#                 template_name='console/services/service_detail.html'
#             ),
#             name='console_service_detail'
#         ),

#         url(r'^services/delete/(?P<pk>\d+)/$',
#             views.ServiceDelete.as_view(
#                 template_name='console/services/service_confirm_delete.html'
#             ),
#             name='console_service_delete'
#         ),

#     #-------------------------------------------------------------------------

#     # Console: Flatpages
#         url(r'^flatpages/$',
#             views.FlatPagesList.as_view(
#                 template_name='console/flatpages/flatpage_list.html',
#             ),
#             name='console_flatpage_list'
#         ),
#         url(r'^flatpages/(?P<pk>\d+)/$',
#             views.FlatPagesDetail.as_view(
#                 template_name='console/flatpages/flatpage_detail.html'
#             ),
#             name='console_flatpage_detail'
#         ),
#         url(r'^flatpages/update/(?P<pk>\d+)/$',
#             views.FlatPagesUpdate.as_view(
#                 form_class=forms.FlatPageForm,
#                 template_name='console/flatpages/flatpage_edit.html',
#             ),
#             name='console_flatpage_edit'
#         ),

# )
