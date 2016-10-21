#encoding: utf-8

import xlrd

data_set = xlrd.open_workbook('./PNS2013/N_percepcao_saude/N4.xls',encoding_override="latin-1")
 

sheet = data_set.sheet_by_index(0)

listaRegioes = ['Norte', 'Nordeste', 'Sul', 'Sudeste', 'Centro-Oeste']
max = ('',0)

listaRP = []

for row in range(14,sheet.nrows-2):
    estado = sheet.cell_value(row, 0)
    proporcao=sheet.cell_value(row, 1)
    
    if listaRegioes.__contains__(estado):
        listaRP.append((estado,proporcao))
    elif float(max[1]) < float(proporcao):
        max =(estado,proporcao)
    #print (estado)


print (max)
print (listaRP)       
