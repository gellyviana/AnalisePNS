#encoding: utf-8

import xlrd
from sys import float_info

data_set = xlrd.open_workbook('./PNS2013/P_estilos_vida/P10_alimentacao.xls',encoding_override="latin-1")
 

sheet = data_set.sheet_by_index(0)

listaRegioes = ['Norte', 'Nordeste', 'Sul', 'Sudeste', 'Centro-Oeste']
max = ('',sheet.cell_value(14,1))
min = ('',sheet.cell_value(14,1))

for row in range(14,sheet.nrows-2):
    estado = sheet.cell_value(row, 0)
    proporcao=sheet.cell_value(row, 1)
    
    if not listaRegioes.__contains__(estado):
        if float(min[1]) > float(proporcao):
            min =(estado,proporcao)
        elif float(max[1]) < float(proporcao):
            max =(estado,proporcao)
        #print (estado)


print ('Estado com maior: '+ max[0])
print ('Estado com menor: '+ min[0])      
