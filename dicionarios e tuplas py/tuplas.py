lista = [1,2,3,4,5,6,7,8,9,10]
sla = int(input("Dejesa informar um numero? "))
lista.append(sla)
for i in lista:
    if i % 2 == 0 :
        lista.remove(i)
print(lista)