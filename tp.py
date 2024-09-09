def tp():
    tasks=[]
    print("----Welcome to the Task Management App----")
    
    total=int(input('Enter the number of tasks: '))
    for i in range(1,total+1):
        task_name=input(f"Enter the task{i} = ")
        tasks.append(task_name)
    
    print(f"todays task are\n{tasks}")
    while True:
        operation = int(input('Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop'))
        if operation==1:
            add=input("Enter the task: ")
            tasks.append(add)
            print(f"Task {add} has been added")
        elif operation==2:
            update_val=input('Enter the task name to be update: ')
            if update_val in tasks:
                up=input("enter new task: ")
                ind=tasks.index(update_val)
                tasks[ind]=up
                print(f'Updated task {up}')
        elif operation==3:
            del_val=input("enter the task name to be deleted: ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"task{del_val} has been deleted")
        elif operation==4:
            print(f"Total tasks are {tasks}")
        elif operation==5:
            print('Closing the program')
            break
        else:
            print('Invalid input')
tp()