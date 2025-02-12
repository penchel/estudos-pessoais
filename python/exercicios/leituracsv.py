import csv
with open('dados.csv','r',encoding="utf-8") as arquivo:
    linha = arquivo.readline()
    colunas = linha.strip().split(",")
    qtdcolunas = len(colunas)
    linha = arquivo.readline()
    lista = []
    while linha:
        dados = linha.strip().split(",")
        dicionario = {}
        for i in range(0,qtdcolunas):
            dicionario[colunas[i]] = dados[i]
        lista.append(dicionario)
        linha = arquivo.readline()
for item in lista:
    print(item)

