class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

    def getNome(self):
        return self.nome
    
    def getAutor(self):
        return self.autor

class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.lista = []
    
    def guardaLivro(self,nome, ano):
        livro = Livro(nome,ano)
        self.lista.append(livro)
    
    def buscaLivroNome(self,nome):
        for livro in self.lista:
            if livro.getNome() == nome:
                print(f"autor: {livro.getAutor()}")

    def buscaLivroAutor(self,autor):
        for livro in self.lista:
            if livro.getAutor() == autor:
                print(f"nome: {livro.getNome()}")
                