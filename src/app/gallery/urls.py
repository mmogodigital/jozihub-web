from django.conf.urls import patterns, include, url

from app.gallery import views

urlpatterns = patterns('',
    url(r'^$',
        views.Galleries.as_view(
            template_name='gallery/galleries.html',
        ),
        name='galleries'
    ),
                       
    url(r'^(?P<slug>[-\w]+)/$',
        views.GalleryDetail.as_view(
            template_name='gallery/gallery_detail.html',
        ),
        name='gallery_detail'
    ),
)