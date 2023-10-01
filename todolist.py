from tkinter import *
from tkinter import messagebox

# Function to add a new task
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

# Function to delete the selected task
def deleteTask():
    try:
        lb.delete(ANCHOR)
    except:
        pass

# Function to update the selected task
def updateTask():
    try:
        selected_task = lb.curselection()[0]
        updated_task = my_entry.get()
        lb.delete(selected_task)
        lb.insert(selected_task, updated_task)
        my_entry.delete(0, "end")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main Tkinter window
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-Do List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

# Create a frame for the listbox
frame = Frame(ws)
frame.pack(pady=10)

# Create the listbox
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

# Initialize the list with some tasks
task_list = [
    
]

for item in task_list:
    lb.insert(END, item)

# Create a scrollbar for the listbox
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Create an entry widget for task input
my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.pack(pady=20)

# Create a frame for buttons
button_frame = Frame(ws)
button_frame.pack(pady=20)

# Create the Add Task button
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Create the "Delete Task" button
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Create the "Update Task" button
updateTask_btn = Button(
    button_frame,
    text='Update Task',
    font=('times 14'),
    bg='#63c2de',
    padx=20,
    pady=10,
    command=updateTask
)
updateTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
