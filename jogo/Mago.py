from Personagem import Personagem

class Mago(Personagem):
    def __init__(self,pontos_de_magia,habilidades_magicas):
        self.pontos_de_magia = pontos_de_magia
        self.habilidades_magicas = habilidades_magicas
    def atacar(self):
        pass
    def defender(self):
        pass