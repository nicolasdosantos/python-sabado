p1 = [8,9,7,9,4,6,7]
p2 = [8,9,7,9,9,6,9]
prova1 = sum(p1)/len(p1)
prova2 = sum(p2)/len(p2)
if prova1 > prova2:
    print(f"os alunos obtiveram uma maior nota na prova 1, a media dos alunos foi: {prova1} ")
else:
    print(f"os alunos obtiveram uma maior nota na prova 2, a media dos alunos foi: {prova2} ")