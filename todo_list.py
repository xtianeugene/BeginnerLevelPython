import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)

    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add 2. View 3. Done 4. Delete 5. Quit")
        choice = input("Choice: ").strip()
        if choice == "1":
            tasks.append({"task": input("Task: "), "done": False})
            save_tasks(tasks)
        elif choice == "2":
            for i, t in enumerate(tasks, 1):
                mark = "✔" if t["done"] else " "
                print(f"{i}. [{mark}] {t['task']}")
        elif choice == "3":
            i = int(input("Task number: ")) - 1
            if 0 <= i < len(tasks):
                tasks[i]["done"] = True
                save_tasks(tasks)
        elif choice == "4":
            i = int(input("Task number: ")) - 1
            if 0 <= i < len(tasks):
                tasks.pop(i)
                save_tasks(tasks)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()