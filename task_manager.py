def add_task(task, description=''):
    task_entry = {'task': task, 'description': description}
    tasks.append(task_entry)
    print(f"Задача '{task}' добавлена с описанием: {description}")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Текущие задачи:")
        for idx, t in enumerate(tasks, 1):
            desc = f" — {t['description']}" if t['description'] else ''
            print(f"{idx}. {t['task']}{desc}")

if __name__ == "__main__":
    while True:
        command = input("Введите команду (add/show/exit): ").strip().lower()
        if command == 'add':
            task_name = input("Название задачи: ").strip()
            task_desc = input("Описание (можно оставить пустым): ").strip()
            add_task(task_name, task_desc)
        elif command == 'show':
            show_tasks()
        elif command == 'exit':
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда.")
