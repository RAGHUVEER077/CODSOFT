import os
import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.file_path = "todo.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['title']} - {task['date']}")

    def add_task(self, title):
        date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task = {"title": title, "date": date_created}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{removed_task['title']}' removed successfully.")
        else:
            print("Invalid task index.")

    def run(self):
        while True:
            print("\n1. Show Tasks")
            print("2. Add Task")
            print("3. Remove Task")
            print("4. Quit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                title = input("Enter task title: ")
                self.add_task(title)
            elif choice == '3':
                task_index = int(input("Enter the task index to remove: "))
                self.remove_task(task_index)
            elif choice == '4':
                print("Quitting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
