tamanho = input("Qual o tamanho do ovo desejado\n*Pequeno (P)\n*Médio (M)\n*Grande (G)\n\n(Responder com a inicial:)")

if tamanho == "P":
    valor = 7.80
elif tamanho == "M":
    valor = 12.90
elif tamanho == "G":
    valor = 23.95

sabor = input("Qual é o sabor desejado:\n*Chocolate preto (P)\n*Chocolate branco (B)\n*Chocolate Ao-Leite (L)\n\n(Responder com a inicial.)")

if sabor == "P":
    valor= valor+9.67
elif sabor == "B":
    valor= valor+4.50
elif sabor == "L":
    valor= valor+9.32

recheio = input("Qual é o recheio desejado(Você pode escolher os dois recheios caso queira):\n*Chocolate preto (CP)\n*Chocolate branco (CB)\n*(Responder com a inicial.)")

if recheio == "CP":
    valor = valor+4.83
elif recheio == "CB":
    valor = valor+2.25
elif recheio == "CP e CB" or "CB e CP" or "cb e cp" or "cp e cb":
    valor = valor+4.83

acrescimo = input ("Qual será o acrescimo (Você pode adicionar mais da uma coisa): \n* MM'S (M) \n*KitKat (K) \n*Não quero(N) \n*(Responder cm a inicial suguerida.)")

if acrescimo == "M":
    valor= valor+4.67
elif acrescimo == "K":
    valor= valor+5.43
elif acrescimo == "M e K" or "K e M":
    valor= valor+10.1
elif acrescimo == "N":
    valor= valor+0.00

presente = input ("Sua compra sera presente?sim ou não(Responda seguindo a alternativa)")

if presente == "não" or "nao":
    valor= valor+0.00
elif presente == "sim":
    valor = valor+2.50

entrega = input ("Sua compra sera entrega?sim ou não \n(Responda seguindo a alternativa)")
