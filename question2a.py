#encoding: latin-1

import xlrd

data_set = xlrd.open_workbook('RELATORIO_DTB_BRASIL_MUNICIPIO.xls',encoding_override="latin-1")
#inputSheet = data_set.sheet_by_name('data_set')
 

sheet = data_set.sheet_by_index(0)

rows =[]

listaCities = []

for row in range(sheet.nrows):
    for col in range(sheet.row_len(row)):
        celula = sheet.cell_value(row, col)
        if celula == 'Seridó Oriental' or 'Seridó Ocidental':
            listaCities = sheet.cell(row, 8)


print listaCities       
