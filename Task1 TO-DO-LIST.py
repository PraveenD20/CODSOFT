def task():
     tasklist=[]

     total_task=int(input("\n enter how many tasks do you want to add = "))
     
     for i in range (1,total_task+1):                  
         task_name=input(f"\nenter your task no {i}  = ")
         tasklist.append(task_name)
     print(f"\n your tasks are \n {tasklist}")

     while True:
          print("\n list of operations")
          print("1. Add Task")
          print("2. Show Tasks")
          print("3. Mark Task as Done")
          print("4. Delete")
          print("5. Exit")
          
          operation=int(input("Enter any operations "))
          if operation==1:
              add_task=input("Enter your task  =")
              tasklist.append(add_task)
              print(f" task {add_task} is added")

          elif operation==2:
              print(" \n Your Tasks Are")
              print(f"\n{tasklist}")
          elif operation==3:
                for i, task in enumerate(tasklist):
                  print(f"{i+1}.{tasklist}")
                  index=int(input("Enter the task number to mark as done:  "))-1

                  if 0<=index<len(tasklist):
                      tasklist[index] +="->Done"
                      break
                  else:
                      print("invalid task number")
                  
          elif operation==4:
              for i, task in enumerate(tasklist):
                  print(f" {tasklist}")
                  ind=int(input("Enter the task number to dlete:  "))-1

                  if 0<=ind<len(tasklist):
                      del tasklist[ind]
                      break
                  else:
                      print("invalid task number")
          
          elif operation==5:
               print(" \nWe are leaving the to-do list\n\n")
               print("")
               break
              
          else:
              print(" Invalid Operation")
              break
     
print("\n~~~~~~~~~~  WELCOME  ~~~~~~~~~~ \n ")
print("=====TO DO LIST Application=====")
task()
