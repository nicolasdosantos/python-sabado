from abc import ABCMeta, abstractmethod

class CartaoMenssagem(metaclass=ABCMeta):
    def __init__(self, remetente):
        self.remetente = remetente
    @abstractmethod
    def destinatario(self):
        pass


class MensagemDiadosNamorados (CartaoMenssagem):
    def destinatario(self):
        nome = str(input("Qual o nome da pessoa que sera entrege?"))
        print("Feliz dias dos namorados "+ nome)


class MensagemNatal(CartaoMenssagem):
    def destinatario(self):
        nome = str(input("Qual o nome da pessoa que sera entrege?"))
        print("Feliz Natal "+ nome)


class MensagemAniversario(CartaoMenssagem):
    def destinatario(self):
        nome = str(input("Qual o nome da pessoa que sera entrege?"))
        print("Feliz aniversario "+ nome)


menssagem = MensagemAniversario()
menssagem.destinatario()