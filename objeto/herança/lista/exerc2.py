#2. Classe Quadrado: Crie uma classe que modele um quadrado:
#a. Atributos: Tamanho do lado
#b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class quadrado:
    def __init__(self,lado):
        self.lado = lado
    def Lado(self, lado):
        self.lado = lado
    def retornoLado(self):
        return self.lado
    def area(self):
        return self.lado * self.lado
    
q = quadrado(19)
print(q.area())