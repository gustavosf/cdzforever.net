# coding: utf-8

from django.conf.urls import patterns, url

from .views import CategoriaView, LinkView

urlpatterns = patterns(
    '',

    url(r'^$', CategoriaView.as_view(), name='categoria'),
    url(r'links/(?P<serie>\d+)/$', LinkView.as_view(), name='links'),
)
