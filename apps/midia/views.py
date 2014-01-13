# coding: utf-8

from django.views.generic import ListView

from django.shortcuts import get_object_or_404

from .models import Serie


class SeriesView(ListView):
    template_name = 'midia/series.html'
    model = Serie


class EpisodiosView(ListView):
    template_name = 'midia/episodios.html'
    queryset = None

    def dispatch(self, request, *args, **kwargs):
        self.queryset = get_object_or_404(Serie, pk=kwargs.get('serie'))

        return super(EpisodiosView, self).dispatch(request, *args, **kwargs)
