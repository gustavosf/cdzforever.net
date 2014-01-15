# coding: utf-8

from django.db import models

from ..core.models import Timestamp

TIPOS = (
    ('Anime', 'Anime'),
    ('Manga', 'Mangá'),
    ('OVA', 'OVA'),
    ('Filme', 'Filme'),
    ('Jogos', 'Jogos'),
    ('OST', 'OST'),
    ('Outros', 'Outros'),
)


class Categoria(models.Model):
    nome = models.CharField(max_length=90)
    tipo = models.CharField(max_length=90, choices=TIPOS)

    def __unicode__(self):
        return "%s - %s" % (self.tipo, self.nome)


class Link(Timestamp):
    categoria = models.ForeignKey(Categoria)

    numero = models.IntegerField()
    titulo = models.CharField(max_length=90)
    arquivo = models.CharField(max_length=255)
    tamanho = models.IntegerField()
    link = models.URLField()
    legenda = models.URLField(blank=True, null=True)
    downloads = models.IntegerField(default=0)

    def __unicode__(self):
        return "#%d - %s" % (self.numero, self.titulo)

