print("Olá, mundo!")

l = input("Informe a letra desejada: ")

if (l == "a" or l == "e" or l == "i" or l == "o" or l == "u"):
    print ("Essa letra é uma vogal")
elif (l == "/" or l == ";" or l == "?" or l == ":" or l == "." or l == ">" or l == "," or l == "<" or l == "]" or l == "}" or l == "º" or l == "~" or l == "^" or l == "[" or l == "{" or l == "ª" or l == "´" or l == "`" or l == "-" or l == "_" or l == ")" or l == "(" or l == "*" or l == "&" or l == "¨" or l == "%" or l == "$" or l == "#" or l == "@" or l == "!"):
    print ("Esse é um caracter especial")
else:
    print ("Essa letra é uma consoante")