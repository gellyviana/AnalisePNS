#enconding: utf-8

lista1 = []

from dbfread import DBF
for arquivo1 in DBF('POPTBR14.dbf'):
    for i in arquivo1:
        print(dict(i)['POPULACAO'])
