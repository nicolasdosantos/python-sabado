n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))

media = (n1 + n2 + n3) / 3

if(media >= 7):
    print("Aprovado, sua nota foi: " + str(media))
elif (media >= 3):
    print("Melhore, sua nota foi: " + str(media))
else:
    print("Morra, sua nota foi: " + str(media))