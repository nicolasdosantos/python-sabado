valor = input("Informe um número: ")
try:
    soma = int(valor) + 10
    resultado = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro de divisão por zero [ZeroDivisionError].")
except ValueError:
    print("Ocorreu um erro de valor [ValueError].")
else:
    print("Não deu erro!!!")
finally:
    print("Esta linha será executada ocorrendo erro ou não!!!")