# coding: utf-8

from django.conf.urls import patterns, url

from .views import SeriesView, EpisodiosView

urlpatterns = patterns(
    '',

    url(r'^$', SeriesView.as_view(), name='series'),
    url(r'episodios/(?P<serie>\d+)/$', EpisodiosView.as_view(), name='episodios'),
)
