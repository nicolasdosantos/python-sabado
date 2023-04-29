# CRIAÇÃO DAS VARIAVEIS 

produtos = ['Tomate', 'Batata', 'Limão']
estoque = [100,200,50]
minimo = [10, 20, 5]

# MOSTRANDO AS LINHAS DE PRODUTOS 

for i in range(len(produtos)):
    print(f"A quatidade de {produtos[i]} é {estoque[i]} e seu estoque minimo é de {minimo[i]}")

# USUARIO ADICIONANDO COISAS NA LISTA

prod = input("Digite o seu produto aqui: ")
est = int(input("Digite o seu estoque aqui: "))
minimos = int(input("Digite o seu minimo de estoque aqui: "))

# ATRIBUINDO OQUE ELE DIGITOU

produtos.append(prod)
estoque.append(est)
minimo.append(minimos)

# MOSTRANDO O QUE ELE DIGITOU

for i in range(len(produtos)):
    print(f"A quatidade de {produtos[i]} é {estoque[i]} e seu estoque minimo é de {minimo[i]}")

# MOSTRANDO SE A QUANTIDADE DE PRODUTOS É MENOR 

for i in range(len(produtos)):
    if estoque[i] <= minimo[i]:
        print(f"Produto{produtos[i]} com a quantidade minima")

# LISTA DENTRO DE UMA LISTA, PARA COLOCAR AS INFORMAÇÕES EM UMA SÓ

lista = []
for i in range(len(produtos)):
    lista.append([produtos[i],estoque[i],minimo[i]])
print(lista)

# USUARIO REMOVE ITEM DA LISTA 

while True:
    remove = input("Digite o produto que voce quer apagar produto aqui: ")
    if remove in produtos:
        break
    else:
        print("Produto invalido: ")
    ind = produtos.index(remove)
    produtos.remove(remove)
    estoque.remove(estoque[ind])
    minimo.remove(minimo[ind])
    print(produtos,estoque,minimo)

# PARTE DA COMPRA DE PRODUTO

compras = []
while True:
    compra_produto = input("Digite o seu produto aqui: ")
    compra_quantidade = int(input("Informe a quantidade de produtos:"))
    compras.append([compra_produto, compra_quantidade])
    repete = input("Deseja continuar sua compra?S ou N: ")
    print(repete)
    if repete.upper() == "N" or "n":
        break
print(compras)

# COMPARAÇÃO COM O PEDIDO E O ESTOQUE

for itens in compras:
  if itens[0] not in produtos: 
    print(f"Produto {itens[0]} não tem")
  elif itens[1] > estoque[produtos.index(itens[0])]:
    print('Saldo insuficiente de {itens[0]}')