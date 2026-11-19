import json
import os

data_file = "to_do_list_.json"
def load_tasks():
    if not os.path.exists(data_file):
        return[]
    try:
        with open(data_file, "r")as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("WARNING:Data file is corrupted .Starting with the empty list.")
        return[]
    
def save_tasks(tasks):
    with open(data_file, "w") as file:
        json.dump(tasks, file , indent=4)     
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is currently empty.")
        return
    
    print("\n YOUR TO-DO LIST")
    for index,task in enumerate(tasks,start=1):
        status_mark ="[X]" if task.get("Completed") else""
        print(f"{index}.{status_mark} {task['title']}")
        print("------------------")
def add_task(tasks):
    title =input("Enter the new task:").strip()
    if title:
        tasks.append({"title":title,"Completed":False})
        save_tasks(tasks)
        print("Success:Task Added.")
    else:
        print("Error:Task description cannot be empty.")
def complete_task(tasks): 
        
    if not tasks:
        print("Error:No tasks available to complete.")
        return
    try:
        task_id =int(input("\n Enter the task number to mark as done:"))
        if 1 <= task_id <=len(tasks):
            if tasks[task_id -1]["Completed"]:
                print("Notice:This task is already Completed.")                
            else:
                tasks[task_id -1]["completed"] = True
                save_tasks(tasks)
                print(("Success:Task has been marked as done."))
        else:
            print(f"Error:Task number{task_id} does not exist.")
    except ValueError:
        print("Error:Please enter a valid numerical value.")
def delete_task(tasks):
    if not tasks:
        print("Error:No tasks available to remove.")
        return 
    try:
        task_id =int(input("\n Enter the task number to remove"))
        if 1 <= task_id <= len(tasks):
            removed_task = tasks.pop(task_id - 1)
            save_tasks(tasks)
            print(f"Success:Deleted task '{removed_task['title']}'.")
        else:
            print(f"Error:Task number{task_id}does not exist.")
    except ValueError:
        print("Error:please enter a valid numerical value.")
                
def main():
    tasks = load_tasks()
    while True:
        view_tasks(tasks)
        print("\n Available Options:")
        print("1.Add a task")
        print("2.Mark task as done")
        print("3.Delete a Task")
        print("4.Exit")
            
        choice =input("select an option(1-4):").strip()
            
        if choice =="1":
            add_task(tasks)
        elif choice =="2":
            complete_task(tasks)
        elif choice =="3":
            delete_task(tasks)
        elif choice =="4":
            print("Exiting Application.")
            break
        else:
            print("Error:Invalid selection.Please choose a number between 1 and 4.")
    
if __name__=="__main__":
    main()