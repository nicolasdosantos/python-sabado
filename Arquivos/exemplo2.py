arquivo = open("arquivo_teste.txt", "r")
print(arquivo.read())
arquivo.close()


arquivo = open("arquivo_teste.txt", "r")
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline(5)) 
arquivo.close()