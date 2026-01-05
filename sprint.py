main = True

tasks = []
while main:
    print("[MENU]")
    print("1. Add a task")
    print("2. Find a task")
    print("3. View all tasks")
    print("4. Delete a task")
    print("5. Exit program")

    num = input("Select number from menu: ").strip()

    # add task
    if (num == "1"):
        print("\n[ADDING A TASK]")
        new_task = input("Enter a new task: ")
        new_task_difficulty = input("Enter a priority level (Easy, Medium, Hard): ")
        tasks.append({'task': new_task, 'difficulty': new_task_difficulty})
        print("")

    # find a task
    elif (num == "2"):
        print("\n[FINDING A TASK]")

        if len(tasks) == 0:
            print("To-do list is empty.\n")
            continue

        i = 0
        search = input("Enter task to find: " )
        for task in tasks:
            if (task['task'] == search):
                print(f"'{search}' found at index {i+1} of to-do list. Priority is {task['difficulty']}.\n")
                break
            i+=1
        else:
            print(f"{search} not found.\n")        

    # view all tasks
    elif (num == "3"):
        print("\n[VIEWING ALL TASKS]")

        if len(tasks) == 0:
            print("To-do list is empty.\n")

        i = 0
        for task in tasks:
            print(f"{i+1}. {task['task']} ({task['difficulty']})")
            i+=1

        print("")

    # delete task
    elif (num == "4"):
        print("\n[DELETING A TASK]")

        delete = input("Enter task to delete: ")
        i = 0
        for task in tasks:
            if (task['task'] == delete):
                tasks.pop(i)
            i+=1

        print("")


    # quit program
    elif (num == 5):
        main = False

    else:
        print("Invalid input.\n")