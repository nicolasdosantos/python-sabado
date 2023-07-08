#3. Classe Retangulo: Crie uma classe que modele um retangulo:
#a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a
#quantidade de pisos e de rodapés necessárias para o local.

class retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    def Comprimento(self, comprimento):
        self.comprimento = comprimento
    def Largura(self, largura):
        self.largura = largura
    def ReturnC(self):
        return self.comprimento
    def ReturnL(self):
        return self.largura
    def area(self):
        return self.comprimento * self.largura
    def perimetro(self):
        return (2 * self.comprimento) + (2 * self.largura)

c = float(input('Informe o valor do comprimento: '))
l = float(input('Informe o valor da largura: '))

