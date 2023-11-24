class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})

    def mark_task_done(self, task_id):
        if 1 <= task_id <= len(self.tasks) and not self.tasks[task_id - 1]['done']:
            self.tasks[task_id - 1]['done'] = True
            # Movendo a tarefa para o início da lista
            self.tasks.insert(0, self.tasks.pop(task_id - 1))
            print(f'Tarefa {task_id} marcada como concluída.')
        else:
            print('Tarefa não encontrada ou já realizada.')

    def edit_task(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            new_description = input(f"Digite a nova descrição para a tarefa {task_id}: ")
            self.tasks[task_id - 1]['task'] = new_description
            print(f'Tarefa {task_id} editada com sucesso.')
        else:
            print('Tarefa não encontrada.')

    def register_new_task(self):
        new_task_description = input("Digite a descrição da nova tarefa (começando com maiúscula): ")
        if new_task_description[0].isupper():
            self.add_task(new_task_description)
            task_id = len(self.tasks)
            print(f'Tarefa {task_id}. {new_task_description} [ ] registrada!')
        else:
            print('A descrição da tarefa deve começar com maiúscula.')

    def display_tasks(self):
        print('Lista de Tarefas:')
        for i, task_info in enumerate(self.tasks, start=1):
            task_status = '[x]' if task_info['done'] else '[ ]'
            print(f"{i}. {task_info['task']} {task_status}")

# Exemplo de uso:
todo_list = ToDoList()

todo_list.add_task("Preparar a marmita")
todo_list.add_task("Arrumar a mochila")
todo_list.add_task("Fechar as janelas")

# Marcar a primeira tarefa como concluída
todo_list.mark_task_done(1)

# Registrar uma nova tarefa
todo_list.register_new_task()

# Exibir a lista de tarefas
todo_list.display_tasks()

# Editar uma tarefa existente
todo_list.edit_task(2)

# Exibir a lista de tarefas após a edição
todo_list.display_tasks()
