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
        print("Bem-vindo ao jogo de combate sobre as linhas de comando!")
        while True:
            comando = input("Digite algum comandos a seguir para realizar alguma ação (criar personagem, criar combate, sair): ")
            if comando == "criar personagem":
                nome = input("Digite o nome do personagem: ")
                classe = input("Digite a classe que os personagem tera(Guerreiro, Mago, Arqueiro, Espadachim): ")
                self.criar_personagem(nome, classe)
            elif comando == "criar combate":
                nome_personagem1 = input("Digite o nome do primeiro personagem: ")
                nome_personagem2 = input("Digite o nome do segundo personagem: ")
                self.criar_combate(nome_personagem1, nome_personagem2)
            elif comando == "sair":
                print("Saindo! Obrigado por jogar nosso jogo, até a proxima")
                break
            else:
                print("Comando inválido!")

    def listar_personagens(self):
        print("Lista de personagens:")
        for personagem in self.personagens:
            print(f"Nome: {personagem.nome}\tClasse: {personagem.classe}")

    def escolher_personagem1(self, nome_personagem):
        personagem = self._buscar_personagem_por_nome(nome_personagem)
        if personagem:
            self.personagem1 = personagem
            print(f"Personagem 1 escolhido: {personagem.nome} ({personagem.classe})")
        else:
            print(f"Personagem selecionado'{nome_personagem}' não foi encontrado,verifique se o nome esta correto")


    def escolher_personagem2(self, nome_personagem):
        personagem = self._buscar_personagem_por_nome(nome_personagem)
        if personagem:
            self.personagem2 = personagem
            print(f"Personagem 2 escolhido: {personagem.nome} ({personagem.classe})")
        else:
            print(f"Personagem selecionado'{nome_personagem}' não foi encontrado,verifique se o nome esta correto")

    def _buscar_personagem_por_nome(self, nome_personagem):
        for personagem in self.personagens:
            if personagem.nome == nome_personagem:
                return personagem
        return None