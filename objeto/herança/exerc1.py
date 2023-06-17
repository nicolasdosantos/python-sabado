class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor(self):
        print(f"O valor do ingresso é R$ {self.valor:.2f}")
class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def valorVIP(self,adicional):
        self.adicional = adicional
        self.valor += self.adicional
        return self.valor
class VIP2(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def valorVIP(self,adicional):
        self.adicional = adicional
        self.valor += self.adicional + self.adicional
        return self.valor
compra = Ingresso(10)
compra_vip = VIP(10)
compra_vip.valorVIP(7)
compra.imprimeValor()
compra_vip.imprimeValor()
superVip= VIP2(10)
superVip.valorVIP(7)
superVip.imprimeValor()