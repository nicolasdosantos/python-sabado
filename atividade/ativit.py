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

# ATRIBUINDO LIMITE DO ESTOQUE 

for i in range(len(produtos)):
    if estoque[i] <= minimo[i]:
        print(f"\nProduto{produtos[i]} com a quantidade minima")