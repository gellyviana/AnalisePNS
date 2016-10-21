#encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import xlrd

data_set = xlrd.open_workbook('./PNS2013/Q_doencas_cronicas/Q32.xls',encoding_override="latin-1")
 

sheet = data_set.sheet_by_index(0)

listaRegioes = ['Norte', 'Nordeste', 'Sul', 'Sudeste', 'Centro-Oeste']


listaRP = {}

for row in range(13,sheet.nrows-2):
    regiao = sheet.cell_value(row, 0)
    proporcao=sheet.cell_value(row, 1)
    
    if listaRegioes.__contains__(regiao):
        listaRP[regiao]=float(proporcao)


print (listaRP)       

n_groups = 5

means_men = tuple(listaRP.values())

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
plt.xticks(index + bar_width, tuple(listaRP.keys()))

plt.show()
