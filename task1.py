def to_do_list():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.") 
        elif choice == "2":
            if not tasks:
                print("No tasks to remove.")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                try:
                    task_index = int(input("Enter task number to remove: ")) - 1
                    if 0 <= task_index < len(tasks):
                        removed_task = tasks.pop(task_index)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "3":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "4":
            print("Exiting the to-do list. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
to_do_list()