from tkinter import *

def file():
    f=open("Dance.txt","r")
    print(f.readlines())
    f.close()


root = Tk()
root.geometry("800x500")
# Non Dropdown Menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=file)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

# Dropdown Menu using .add_cascade()
mymenu = Menu(root)
m1 = Menu(mymenu)
m1.add_command(label="New File",command=file)
m1.add_command(label="Open File",command=file)
m1.add_command(label="Save File",command=file)
m1.add_command(label="Save File As",command=file)

mymenu.add_cascade(label ="File", menu=m1)
root.config(menu=mymenu)
root.mainloop()