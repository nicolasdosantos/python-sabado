valor = input("Informe um número: ")
try:
    soma = int(valor) + 10
    resultado = soma / int(valor)
except:
    print("Ocorreu um erro no sistema.")