from Arqueiro import Arqueiro
from Mago import Mago
from Guerreiro import Guerreiro
from Espadachim import Espadachim
from Combate import Combate

class Jogo():
    def __init__(self):
        self.personagens = []
        self.combate = Combate()
        self.personagem1 = None
        self.personagem2 = None

    def criar_personagens_basicos(self):
        self.criar_personagem("Guts", "Guerreiro")
        self.criar_personagem("Natsu", "Mago")
        self.criar_personagem("Usop", "Arqueiro")
        self.criar_personagem("Zoro","Espadachim")

    def criar_personagem(self, nome, classe):
        if classe == "Guerreiro":
            personagem = Guerreiro(nome, 1)
        elif classe == "Mago":
            personagem = Mago(nome, 1)
        elif classe == "Arqueiro":
            personagem = Arqueiro(nome, 1)
        elif classe == "Espadachim":
            personagem = Espadachim(nome, 1)
        else:
            print("Classe de personagem inválida!")
            return

    def criar_combate(self):
        if self.personagem1 is None or self.personagem2 is None:
            print("Os personagens selecionados não foram encontrados, verifique se os nomes estão corretos!")
            return
        self.combate.lutar(self.personagem1, self.personagem2)

    def iniciar_jogo(self):
        pass
    def listar_personagens(self):
        pass
    def escolher_personagem1(self):
        pass
    def escolher_personagem2(self):
        pass
    def buscar_personagem(self):
        pass