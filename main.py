from utils import get_highest_priority_task, save_tasks, load_tasks, search_tasks, sort_tasks_by_priority
from utils import build_priority_queue, get_next_task
from task import Task

tasks_data = load_tasks()
tasks = []

for t in tasks_data:
    task = Task(t["title"], t["priority"], t["due_date"])
    task.completed = t["completed"]
    tasks.append(task)

def add_task():
    title = input("Enter task title: ")
    priority = int(input("Enter priority (1-5): "))
    if priority < 1 or priority > 5:
        print("Priority must be between 1 and 5")
        return
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = Task(title, priority, due_date)
    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added!")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("🗑 Task deleted!")
    else:
        print("Invalid index")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n📋 YOUR TASKS:")
    print("-" * 40)

    for i, task in enumerate(tasks):
        status = "✔" if task.completed else "❌"
        print(f"{i+1}. {task.title}")
        print(f"   Priority: {task.priority} | Due: {task.due_date} | {status}")
        print("-" * 40)

def mark_completed():
    view_tasks()
    index = int(input("Enter task number to mark complete: ")) - 1

    if 0 <= index < len(tasks):
        tasks[index].completed = True
        save_tasks(tasks)
        print("✔ Task marked completed!")
    else:
        print("Invalid index")

def search_task():
    keyword = input("Enter keyword to search: ")

    results = search_tasks(tasks, keyword)

    if not results:
        print("No matching tasks found.")
        return

    print("\n🔍 Search Results:")
    for i, task in enumerate(results):
        print(f"{i+1}. {task.title} | Priority: {task.priority}")

def sort_tasks():
    sorted_list = sort_tasks_by_priority(tasks)

    print("\n📊 Tasks Sorted by Priority:")
    for i, task in enumerate(sorted_list):
        print(f"{i+1}. {task.title} | Priority: {task.priority}")
    
def suggest_task():
    heap = build_priority_queue(tasks)
    task = get_next_task(heap)

    if not task:
        print("No tasks available.")
    else:
        print("\n💡 Next Best Task:")
        print(f"{task.title} | Priority: {task.priority}")

def menu():
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Completed")
        print("5. Search Task")
        print("6. Sort Tasks")
        print("7. Suggest Task")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            search_task()
        elif choice == "6":
            sort_tasks()
        elif choice == "7":
            suggest_task()
        elif choice == "8":
            break
        else:
            print("Invalid choice")

menu()