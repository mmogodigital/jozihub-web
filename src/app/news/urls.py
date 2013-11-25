from django.conf.urls import patterns, include, url

from app.news import views

urlpatterns = patterns('',
    url(r'^$',
        views.News.as_view(
            template_name='news/news.html',
        ),
        name='news'
    ),
                       
    url(r'^(?P<slug>[-\w]+)/$',
        views.NewsDetail.as_view(
            template_name='news/news_detail.html',
        ),
        name='news_detail'
    ),
)