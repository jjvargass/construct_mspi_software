#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from git import Repo
import logging
import datetime
import calendar

date  = datetime.datetime.now()
fecha_inicio = date.replace(day = 1)
fecha_fin = date.replace(day = calendar.monthrange(date.year, date.month)[1])
# formato
form_fecha_inicio = fecha_inicio.strftime("%Y-%m-%d")
form_fecha_fin = fecha_fin.strftime("%Y-%m-%d")
# filtros
# --after=2020-02-11 00:00
after = '--after=' + str(form_fecha_inicio) +' 00:00'
# --before=2020-02-12 23:59
before = '--before=' + str(form_fecha_fin) + ' 23:59'

path = os.getcwd()
repo = Repo(path)

print "### Intervalo de {}  hasta {}  ###".format(form_fecha_inicio, form_fecha_fin)

#commits_list = repo.git.log('--oneline', after, before, '--format=%B').split('\n')
commits_list = repo.git.log('--oneline', '--after=2020-02-17 00:00', '--before=2020-02-17 23:59', '--format=%B').split('\n')

# limpiar lista
while("" in commits_list):
    commits_list.remove("")

for i in commits_list:
    print i