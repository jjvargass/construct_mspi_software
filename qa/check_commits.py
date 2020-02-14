import os
from git import Repo
import logging
import datetime
import calendar

date  = datetime.datetime.now()
fecha_inicio = date.replace(day = 1)
fecha_fin = date.replace(day = calendar.monthrange(date.year, date.month)[1])

print fecha_inicio
print fecha_fin

print "Formatos fecha Inicio"
# dd/mm/YY
d1 = fecha_inicio.strftime("%d/%m/%Y")
print("d1 =", d1)
# Textual month, day and year
d2 = fecha_inicio.strftime("%B %d, %Y")
print("d2 =", d2)
# mm/dd/y
d3 = fecha_inicio.strftime("%m/%d/%y")
print("d3 =", d3)
# Month abbreviation, day and year
d4 = fecha_inicio.strftime("%b-%d-%Y")
print("d4 =", d4)

print "Formatos fecha Fin"
# dd/mm/YY
d1 = fecha_fin.strftime("%d/%m/%Y")
print("d1 =", d1)
# Textual month, day and year
d2 = fecha_fin.strftime("%B %d, %Y")
print("d2 =", d2)
# mm/dd/y
d3 = fecha_fin.strftime("%m/%d/%y")
print("d3 =", d3)
# Month abbreviation, day and year
d4 = fecha_fin.strftime("%b-%d-%Y")
print("d4 =", d4)



# path = os.getcwd()
# repo = Repo(path)
# commits_list = list(repo.iter_commits())

# for i in range(len(commits_list)):
#     commit = commits_list[i]
#     print(commit.hexsha)
#     print(commit.author)
#     print(commit.message)
