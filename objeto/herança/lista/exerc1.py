#1. Classe Bola: Crie uma classe que modele uma bola:
#a. Atributos: Cor, circunferência, material
#b. Métodos: trocaCor e mostraCor

class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        print(f"A bolinha é da cor {self.cor}, tem uma circunferencia de {self.circunferencia}, e seu material é de {self.material}\n")
    def TrocaCor(self,cor):
        self.cor = cor
        print(f"A cor da bolinha agora é {self.cor}")
    def MostrarCor(self):
        return self.cor
    
b = bola("azul", 10, "couro")
#print(b.MostrarCor())
b.TrocaCor("vermelha")
#print(b.MostrarCor())