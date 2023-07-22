from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome, nivel):
        super().__init__(nome, "Guerreiro", nivel, 100, 10, 5)
        self.bonus_ataque = 5
        self.bonus_defesa = 10

    def atacar(self):
        print(f"O {self.nome} atacou ferozmento com {self.pontos_de_ataque + self.bonus_ataque} pontos de ataque!")

    def defender(self):
        print(f"{self.nome} se defendeu com {self.bonus_defesa} pontos de defesa adicionais!")