p = float(input("Informe seu peso:"))

h = float(input("Informe sua altura"))

result = p / (h**h) 

if (result < 18.5):
    print("Voce esta abaixo do peso")
elif (result > 18.5):
    print("Voce esta no peso ideal")
elif (result > 25):
    print("Voce esta com exesso de peso")
elif (result > 30):
    print("Voce esta com obesidade gru I")
elif (result > 35):
    print("Voce esta com obesidade gru II")
else:
    print("Voce esta com obesidade gru III")