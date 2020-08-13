
from tkinter import*

# create root window
root = Tk()

# root window title and dimension
root.title("Python.GUI.Project")
root.geometry('350x200')

# creating a function
def myfunc():
    Label(root, text="Saving...").pack()

# adding menu bar in root window
# new item in menu bar called 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu, tearoff=0)
m1 = Menu(menu, tearoff=0)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
m1.add_command(label="Save", command=myfunc)
lbl = Label(root, text = "Are you a Programmer?")
lbl.grid()

# separating two labels in menu
m1.add_separator()
m1.add_command(label="Exit", command=quit)
menu.add_cascade(label="File", menu=m1)

# adding one more drop down
m2 = Menu(menu, tearoff=0)

# adding label
m2.add_command(label="Find", command=myfunc)

# separator
m2.add_separator()
m2.add_command(label="Exit", command=quit)
menu.add_cascade(label="Edit", menu=m2)

# adding entry field
txt = Entry(root, width=10)
txt.grid(column =1, row=0)

def clicked():

    res = "You wrote " + txt.get()
    lbl.config(text = res)

# button widget with red text
btn = Button(root, text = "Click me" ,
        fg = "red", command=clicked)

btn.grid(column=2, row=0)

root.mainloop()
