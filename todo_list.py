my_tasks = []
while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task: ")
        if task == "":
            print("Please enter a task.")
        else:
            my_tasks.append(task)
            print("Task added.")
    elif choice == "2":
        if len(my_tasks) == 0:
            print("No tasks added yet.")
        else:
            print("\nYour Tasks:")

            for i, task in enumerate(my_tasks, 1):
                print(i, "-", task)
    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")