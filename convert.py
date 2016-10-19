#encoding:utf-8

ler=open("Nascimentos_RN.csv","r")
saida=open("NOVO","w")

for linha in ler.readlines():
	for car in linha:
		if(car==";"):
			saida.write(",")
		else:
			saida.write(car)
