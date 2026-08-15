tasks = []

while True:
    print("\n==============================")
    print("       TO-DO LIST")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            for i, item in enumerate(tasks, 1):
                if item["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(i, ".", item["task"], "-", status)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, 1):
                print(i, ".", item["task"])

            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, 1):
                print(i, ".", item["task"])

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                print("Task removed:", removed_task["task"])
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")