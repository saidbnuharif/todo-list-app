import json

# with open("tasks.json","w")as file:
#     json.dump([],file,)

with open("tasks.json","r")as file:
    data = json.load(file)

def save_data():
    with open("tasks.json","w")as file:
        json.dump(data,file,indent=4)  
        print("data saved")

def add_task(task):

    data.append({

        "task": task.lower(),
        "status": False
    })

    save_data()

    print("Task added")

    


def remove_task(task):
    print(task)

    for item in data:
        print(item)

        if item["task"] == task:

            data.remove(item)

            save_data()

            print("Task removed successfully")

            return

    print("Task not found")
    

def view_tasks():
    if not data:
        print("list is empty")
    else:
        for index, task in enumerate(data,start=1):
          print(f"{index}:{task}")    


def update_task(status,task):

    for item in data:

        if item["task"] == task:

            if status.lower() == "yes":

                item["status"] = True

            elif status.lower() == "no":

                item["status"] = False

            save_data()

            print("Task status updated")

            return

    print("Task not found")    

    
    


while True:
       print("""
       enter your choice:
       1:add
       2:remove
       3:find all
       4:update
       5:exit                              
       """)  

       choice = input("Enter your choice: ")

       if choice == "1":
           task = input("Enter the task: ").lower()
           add_task(task)

       elif choice == "2":
           task = input("Enter task to remove: ").lower()
           remove_task(task)
          

       elif choice == "3":
           if not data:
               print("List not found")
           else:
                view_tasks()  


       elif choice == "4":

         updating_task = input("Enter your task: ")
        
         updating_status = input("Did you complete task? (yes/no): ")

         update_task(updating_status,updating_task)
           
               
       elif choice == "5":
           print("exited from the program") 
           break
       
       else:
           print("Invalid choice")
        
                    
            
    
