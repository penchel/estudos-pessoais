frase = input("Escreva a frase: ")
vogais = "aeiouAEIOUãÃáÁÀàòóéê"
contador = 0
for char in frase:
    if char in vogais:
        contador+=1

print(f"Quantidade de vogais: {contador}")