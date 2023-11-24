class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})

    def mark_task_done(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            self.tasks[task_id - 1]['done'] = True
            print(f'Tarefa {task_id} marcada como concluída.')
        else:
            print('ID de tarefa inválido.')

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

# Exibir a lista de tarefas
todo_list.display_tasks()
