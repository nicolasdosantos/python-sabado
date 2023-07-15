from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self,bonus_ataque,bonus_defesa):
        self.bonus_ataque = bonus_ataque
        self.bonus_defesa = bonus_defesa
    def atacar(self):
        pass
    def defender(self):
        pass