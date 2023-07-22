from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome, nivel):
        super().__init__(nome, "Mago", nivel, 50, 5, 0)
        self.pontos_de_magia = 100
        self.habilidades_magicas = ["bola de fogo", "raio", "bareira magica"]

    def atacar(self):
        print(f"{self.nome} atacou com {self.habilidades_magicas[0]}, e deixou seu inimigo ferido!")
        self.pontos_de_magia -= 20

    def defender(self):
        print(f"{self.nome} se defendeu com {self.habilidades_magicas[2]}, onde sua defesa concreta!")
        self.pontos_de_magia -= 10