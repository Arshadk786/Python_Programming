from tkinter import *

def sizeChange():
    win_width.get()
    win_height.get()
    root.geometry(f"{win_width.get()}x{win_height.get()}")

root = Tk()
win_height = IntVar()
win_width = IntVar()

Label(root, text="Enter the Size of Window: ",font="Consolas 14 bold").grid(row=0, column=2)

l1 = Label(root, text="Height: ", font="Consolas 14 bold").grid(row=1, column=2,ipadx=10,ipady=10)
l2 = Label(root, text="Width: ",  font="Consolas 14 bold").grid(row=2, column=2, ipadx=10,ipady=10)

e1 = Entry(root, textvariable=win_height).grid(row=1, column=3,padx=10,pady=10)
e2 = Entry(root, textvariable=win_width).grid(row=2, column=3,padx=10,pady=10)

Button(root, text="Apply", command=sizeChange,padx=15,pady=15, bd=3, relief=GROOVE, fg="white", bg="red").grid(row=3,column=3,columnspan=2)
root.mainloop()