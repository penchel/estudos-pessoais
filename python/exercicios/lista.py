numeros = input("escreva os números separados por um espaço: ")
map = map(int,numeros.split())
lista = list(map)
print("ordem decrescente")
lista.sort(reverse = True)
for numero in lista:
    print(numero, end=" ")
print("\nordem crescente")
for i in range(len(lista)-1, -1, -1):
    print("{}: {}".format(i, lista[i]), end=" ")
