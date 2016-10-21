#encoding: utf-8

import xlrd

data_set = xlrd.open_workbook('RELATORIO_DTB_BRASIL_MUNICIPIO.xls',encoding_override="latin-1")
#inputSheet = data_set.sheet_by_name('data_set')
 

sheet = data_set.sheet_by_index(0)

rows =[]

listaCities = []

for row in range(sheet.nrows):
        estado = sheet.cell_value(row, 1)
        if estado == 'Rio Grande do Norte':
            microregiao1=sheet.cell_value(row, 3)
            microregiao2=sheet.cell_value(row, 5)
            if microregiao1 == 'Leste Potiguar' and microregiao2=='Natal':
                #print(microregiao)
                listaCities.append(str(sheet.cell(row, 8))[5:])


print (listaCities)       
