dicio = {"casa":"alugada",
         "estado civil":"casado ne pai",
         "classe social":"podre de rico",
         "cargo":"gerente administrativo"}

while True:
    pergunta = input("deseja saber: (casa, estado civil, classe social ou cargo?) ")
    if pergunta == "fim":
        break
    if pergunta in dicio:
        print (f"{pergunta}: {dicio[pergunta]}")