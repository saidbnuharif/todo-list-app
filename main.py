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

        "task": task,
        "status": False

    })

    save_data()

    print("Task added")

    


def remove_task(task):

        data.remove(task)

        save_data()

        print("Task removed successfully")


def view_tasks():
    if not data:
        print("list is empty")
    else:
        for index, task in enumerate(data,start=1):
          print(f"{index}:{task}")    


def update_task(status,task):
   if  status == "yes": 
    data[task][status] = True
   else:
       print("Please complete the task")  

    
    


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
           task = input("Enter the task: ")
           add_task(task)

       elif choice == "2":
           task = input("Enter task to remove: ")
           if task not in data:
               print("Task not found in list")
           else:
               remove_task(task)

       elif choice == "3":
           if not data:
               print("List not found")
           else:
                view_tasks()  


       elif choice == "4":
          task = input("Enter your task")
          if task in data:
           status = "Does your task completed type yes / No"
           update_task(status,task)
          else:
              print("No task found") 
           
               
       elif choice == "5":
           print("exited from the program") 
           break
       
       else:
           print("Invalid choice")
       
                  
                      
            
    
