#Classe de Herói
class Heroi:
    #Definição do Atributos da classe:
    voa = False
    possui_arma = False
    lanca_teia = False
    frase_comum = ""
    #Definição dos métodos/;
    def falar(self):
        print(self.frase_comum)
    def detalhar(self):
        if self.voa:
            print("O herói voa.")
        if self.possui_arma:
            print("O herói possui arma.")
        if self.lanca_teia:
            print("O herói lança teia.")


#Programa Principal
homem_aranha = Heroi() #cria um objeto do tipo Heroi
homem_aranha.lanca_teia = True
print(homem_aranha.voa)
print(homem_aranha.lanca_teia)
he_man = Heroi() #cria um objeto do tipo Heroi
he_man.possui_arma = True
he_man.lanca_teia = False
he_man.voa = False
he_man.frase_comum = "Eu tenho a força"
he_man.falar()
homem_aranha.detalhar()
he_man.detalhar()

