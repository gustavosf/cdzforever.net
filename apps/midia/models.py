# coding: utf-8

from django.db import models

from ..core.models import Timestamp

CATEGORIAS = (
    ('Anime', 'Anime'),
    ('Mangá', 'Mangá'),
    ('OVA', 'OVA'),
    ('Filme', 'Filme'),
    ('Jogos', 'Jogos'),
    ('OST', 'OST'),
)


class Serie(models.Model):
    nome = models.CharField(max_length=90)
    categoria = models.CharField(max_length=90, choices=CATEGORIAS)

    def __unicode__(self):
        return "%s - %s" % (self.categoria, self.nome)


class Episodio(Timestamp):
    numero = models.IntegerField()
    titulo = models.CharField(max_length=90)
    serie = models.ForeignKey(Serie)
    link = models.URLField()
    downloads = models.IntegerField(default=0)

    def __unicode__(self):
        return "#%d - %s" % (self.numero, self.titulo)

