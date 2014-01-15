# coding: utf-8

from django.views.generic import ListView

from django.shortcuts import get_object_or_404

from .models import Categoria


class CategoriaView(ListView):
    model = Categoria


class LinkView(ListView):
    template_name = 'media/link_list.html'
    queryset = None

    def dispatch(self, request, *args, **kwargs):
        self.queryset = get_object_or_404(Categoria, pk=kwargs.get('categoria'))

        return super(EpisodiosView, self).dispatch(request, *args, **kwargs)
