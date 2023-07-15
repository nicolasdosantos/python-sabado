from Personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self,bonus_presisao,habilidades_com_arco):
        self.bonus_presisao = bonus_presisao
        self.habilidades_com_arco = habilidades_com_arco
    def atacar(self):
        pass
    def defender(self):
        pass