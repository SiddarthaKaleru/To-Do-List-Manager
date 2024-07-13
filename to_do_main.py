import matplotlib.pyplot as py
class to_do:
    def __init__(self,file):
        self.file=file
        self.tasks=self.load()
    def load(self):
        tasks=[]
        try:
            with open(self.file,'r') as file1:
                tasks=file1.read().splitlines()
        except (IOError,FileNotFoundError):
            print("Error in File Handling.")
        return tasks
    def save(self):
        with open(self.file,'w') as f:
            f.write('\n'.join(self.tasks))
    def add(self):
        task2=input("Enter the Task: ")
        self.tasks.append(task2+"  (Incomplete)")
        self.save()
        print("Task added Successfully.")
    def mark(self):
        if len(self.tasks)==0:
            print("No task to marked.")
            return
        print("Current Tasks:")
        for i,t in enumerate(self.tasks):
            print(f"{i+1}.{t}")
        try:
            m=int(input("Enter the number of the Task to be marked as Completed:"))
            if m<1 or m>len(self.tasks):
                raise Exception
            else:
                index = m - 1
                self.tasks[index] = self.tasks[index].replace("(Incomplete)", "(Completed)")
                self.save()
            print("The given Task is marked as Completed")
        except :
            print("Invalid Input.")
    def remove(self):
        if len(self.tasks)==0:
            print("No task to remove.")
            return
        print("Current Tasks:")
        for i,t in enumerate(self.tasks):
            print(f"{i+1}.{t}")
        try:
            c=int(input("Enter the number of the Task to be removed:"))
            if c<1 or c>len(self.tasks):
                raise Exception
            else:
                removed=self.tasks.pop(c-1)
                self.save()
            print(f"Task '{removed}' removed Successfully.")
        except :
            print("Invalid Input.")
    def display(self):
        if len(self.tasks)==0:
            print("No task to display.")
        else:
            print("Current Tasks:")
            for i,t in enumerate(self.tasks):
                print(f"{i+1}.{t}")
            c_count = sum("(Completed)" in task for task in self.tasks)
            i_count = len(self.tasks) - c_count
            labels = ['Completed', 'Incomplete']
            counts = [c_count, i_count]
            colors = ['blue', 'red']
            py.pie(counts, labels=labels,colors=colors,autopct='%1.1f%%', startangle=90)
            py.axis('equal') 
            py.title('Task Completion Status')
            py.show()
file="task.txt"
task=to_do(file)
while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("Enter 1 for add a task\nEnter 2 for mark the task as completed\nEnter 3 for remove a task\nEnter 4 for display the tasks\nEnter 5 to Exit")
    try:
        n=int(input("Enter your choice: "))
        if n==1:
            task.add()
        elif n==2:
            task.mark()
        elif n==3:
            task.remove()
        elif n==4:
            task.display()
        elif n==5:
            print("Exiting the Program.")
            print("\nThank you for using To-Do list Manager.")
            break
        else:
            print("You entered Wrong value\nPlease try again.")
    except:
        print("Entered Invalid Input")