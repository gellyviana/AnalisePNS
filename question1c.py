#encoding: utf-8

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
listaCidade.append((data_set['Município'])[listaAux.index(listasoma[0])][7:])
listaCidade.append((data_set['Município'])[listaAux.index(listasoma[1])][7:])
listaCidade.append((data_set['Município'])[listaAux.index(listasoma[2])][7:])


n_groups = 3

means_men = (listasoma[0],listasoma[1],listasoma[2])

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config)


plt.xlabel('Regiões')
plt.ylabel('Proporções')
plt.title('Proporção por Região')
plt.xticks(index + bar_width, tuple(listaCidade))

plt.show()
