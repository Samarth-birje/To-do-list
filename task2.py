tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt","w") as file:
        for t in tasks:
            file.write(t + "\n")

def add_task():
    task = input("enter a task: ")
    tasks.append(task)
    save_tasks()


def remove_task():
    view_tasks()
    num = int(input("enter the number to remove the tasks:"))-1
    if 0 <= num < len(tasks):
        tasks.pop(num)
        save_tasks()

def view_tasks():
    print("\nYour tasks:")
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t}")

load_tasks()
while True:
    print("\n1. Add \n 2. Remove\n 3. View\n 4. Exit")
    choice = input("choose:")

    if choice == "1": add_task()
    elif choice == "2": remove_task()
    elif choice == "3": view_tasks()
    elif choice == "4": break