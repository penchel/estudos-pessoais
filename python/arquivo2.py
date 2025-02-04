with open('apache_logs.txt', 'r') as log:
    conteudo = log.read()
caracteres = len(conteudo)
palavras = len(conteudo.split())
linhas = 1
for caractere in conteudo:
    if caractere == '\n':
        linhas = linhas + 1

print("linhas "+str(linhas))
print("caracteres "+str(caracteres))
print("palavras "+str(palavras))