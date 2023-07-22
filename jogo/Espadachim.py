from Personagem import Personagem

class Espadachim(Personagem):
    def __init__(self, nome, nivel):
        super().__init__(nome, "Espadachim", nivel, 100, 10, 5)
        self.bonus_ataque = 15
        self.bonus_defesa = 5

    def atacar(self):
        print(f"O {self.nome} retalhou seu inimigo com {self.pontos_de_ataque + self.bonus_ataque} pontos de ataque!")

    def defender(self):
        print(f"{self.nome} bloqueou com {self.bonus_defesa} pontos de defesa adicionais, atravez de suas espadas!")