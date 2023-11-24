import csv

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})

    def mark_task_done(self, task_id):
        if 1 <= task_id <= len(self.tasks) and not self.tasks[task_id - 1]['done']:
            self.tasks[task_id - 1]['done'] = True
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

    def save_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for task_info in self.tasks:
                writer.writerow([task_info['task'], task_info['done']])

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                self.tasks = [{'task': row[0], 'done': row[1] == 'True'} for row in reader]
        except FileNotFoundError:
            print('Arquivo não encontrado. Criando uma nova lista de tarefas.')

# Exemplo de uso:
todo_list = ToDoList()

# Carregar lista de tarefas do arquivo (ou criar uma nova se o arquivo não existir)
todo_list.load_from_file('todolist.csv')

# Exibir a lista de tarefas
todo_list.display_tasks()

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

# Salvar a lista de tarefas no arquivo
todo_list.save_to_file('todolist.csv')
