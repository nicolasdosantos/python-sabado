from Personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self, nome, nivel):
        super().__init__(nome, "Arqueiro", nivel, 75, 7,3)
        self.bonus_precisao = 10
        self.habilidades_com_arco = ["Tiro Certeiro", "Flecha Impacto"]
    def atacar(self):
        print(f"O {self.nome} teve uma mira certeira e atacou com sua habilidade {self.habilidades_com_arco[0]} e obteve {self.bonus_precisao}% de precisão adicional!")
    def defender(self):
        print(f"{self.nome} se esquivou do ataque, com sua agilidade alta!")