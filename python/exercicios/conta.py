class Contabancaria:
    def __init__(self,nome):
        self.nome = nome
        self.saldo = 0

    def depositar(self,valor):
        self.saldo+=valor
    
    def saque(self,valor):
        if(valor>self.saldo):
            print("saldo insuficiente")
        else:
            self.saldo-=valor
    
    def consulta(self):
        return self.saldo