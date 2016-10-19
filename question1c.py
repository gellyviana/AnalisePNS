#encoding: latin-1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set = pd.read_csv('NOVO.csv')
listasoma = []

for valor in data_set['2010']:
    listasoma.append(int(valor))

for i in (0, len(listasoma)-1):
    listasoma[i] += int(data_set['2011'][i]) + int(data_set['2012'][i]) +int(data_set['2013'][i])+int(data_set['2014'][i])

listaAux= listasoma
listasoma.sort()
listasoma.reverse()

listaCidade=[]
listaCidade.append((data_set['Município'])[listaAux.index(listasoma[0])])
listaCidade.append((data_set['Município'])[listaAux.index(listasoma[1])])
listaCidade.append((data_set['Município'])[listaAux.index(listasoma[2])])

#Grafico
#plt.title ('Três primeiros municípios com maiores numero de Nascimento.')
y_axis = [listasoma[0],listasoma[1],listasoma[2]]
x_axis = [listaCidade[0],listaCidade[1],listaCidade[2]]

width_n = 0.4
bar_color = 'pink'

#plt.bar(x_axis, y_axis, width=width_n,color=bar_color)
plt.xticks([1, 2, 3, 4, 5, 6], ['Vá1', 'V2', 'V3', 'V4', 'V5', 'V6'])

data_set.plot()
plt.show()
