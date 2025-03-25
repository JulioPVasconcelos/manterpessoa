lista_tarefas = []

def adicionar_tarefa(tarefa: str):
    lista_tarefas.append(tarefa)
=======
    lista_tarefas.append(tarefa)

def remover_tarefa(tarefa: str):
    if tarefa in lista_tarefas:
        lista_tarefas.remove(tarefa)
