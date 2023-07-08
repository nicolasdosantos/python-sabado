from Tarefas import ListaDeTarefas, Tarefa
lista_de_tarefas = ListaDeTarefas()

while True:
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        id = input("Digite o id da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        tarefa = Tarefa(id, descricao)
        lista_de_tarefas.adicionar_tarefa(tarefa)
    elif escolha == "2":
        id = input("Digite o id da tarefa: ")
        lista_de_tarefas.remover_tarefa(id)
    elif escolha == "3":
        lista_de_tarefas.listar_tarefas()
    elif escolha == "4":
        break