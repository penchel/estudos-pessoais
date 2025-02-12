lista = []
for i in range(3):
    lista.append(int(input("insira o número {}:".format(i+1))))

lista.sort()
print(lista[0])
