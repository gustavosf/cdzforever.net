# coding: utf-8

import pprint

import os

from django.conf import settings

from django.core.management.base import BaseCommand, CommandError

from mega import Mega

class Command(BaseCommand):
    help = 'Sincroniza os arquivos locais com os arquivos do Mega'

    def __init__(self, *args, **kwargs):
        usuario, senha = settings.MEGA['email'], settings.MEGA['password']

        mega = Mega({'verbose': True})
        self.m = mega.login(usuario, senha)

        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        arquivos = self.m.get_files()
        remoto = [a['a']['n'] for k, a in arquivos.items() if a.get('s')]

        upload = list()

        for root, dirs, files in os.walk(settings.MEGA['path']):
            for file in files:
                name, ext = os.path.splitext(file)
                if ext in settings.MEGA['exts'] and file not in remoto:
                    upload.append(os.path.join(root, file))

        self.stdout.write('Arquivos para fazer upload: %d' % len(upload))

        for file in upload:
            self.stdout.write('Fazendo upload: %s' % os.path.basename(file))
            self.m.upload(file)
