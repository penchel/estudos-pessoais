frase = input("Escreva a frase:").upper()
lista = [palavra.strip(',') for palavra in frase.split()]
dicionario = {}
for word in lista:
    if word in dicionario:
        dicionario.update({word: dicionario[word]+1})
    else:
        dicionario.update({word: 1})

for chave in dicionario:
    print(chave+": "+str(dicionario[chave]))