def main():
  tasks = []
  while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
      new_task = input("Enter a new task: ")
      tasks.append(new_task)
      print("Task added!")
    elif choice == '2':
      if not tasks:
        print("No tasks added yet!")
      else:
        for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task}")
    elif choice == '3':
      if not tasks:
        print("No tasks to mark as done!")
      else:
        for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task}")
        task_to_mark = int(input("Enter the number of the task to mark done: "))
        if 1 <= task_to_mark <= len(tasks):
          tasks.pop(task_to_mark - 1)
          print("Task marked as done!")
        else:
          print("Invalid task number!")
    elif choice == '4':
      print("Exiting the To-Do List.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
