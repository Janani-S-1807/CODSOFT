tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"name": task, "done": False})
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                status = "Completed" if tasks[i]["done"] else "Pending"
                print(f"{i + 1}. {tasks[i]['name']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['name']}")
            n = int(input("Enter task number to update: "))
            if 1 <= n <= len(tasks):
                tasks[n - 1]["name"] = input("Enter new task: ")
                print("Task updated successfully.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['name']}")
            n = int(input("Enter task number to mark as completed: "))
            if 1 <= n <= len(tasks):
                tasks[n - 1]["done"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['name']}")
            n = int(input("Enter task number to delete: "))
            if 1 <= n <= len(tasks):
                tasks.pop(n - 1)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")

    elif choice == "6":
        print("Thank you for using the To-Do List Application.")
        break

    else:
        print("Invalid choice. Please try again.")