from tkinter import *
def display():
    print(f"Username is {userval.get()}")
    print(f"Password is {passval.get()}")
root = Tk()
root.geometry("600x300")
root.title("Grid And Entry Widget")
l1 = Label(root, text="User: ")
l2 = Label(root, text="Password: ")
# l1.pack()
# l2.pack()
l1.grid(row=0,column=3)
l2.grid(row=1,column=3)

userval = StringVar()
passval = StringVar()

Entry(textvariable=userval).grid(row=0, column= 5)
Entry(textvariable=passval).grid(row=1, column= 5)

Button(text="Submit", command=display).grid(row= 4, column= 4)
root.mainloop()