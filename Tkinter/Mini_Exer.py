from tkinter import *


def cal():
    print(f"Addition = {first.get() + second.get()}")
    print(f"Subtraction = {first.get() - second.get()}")
    print(f"Multiplication = {first.get() * second.get()}")
    print(f"Division = {first.get() // second.get()}")


root = Tk()
root.title("Calculator")
root.geometry("600x300")

first = IntVar()
second = IntVar()

l = Label(text="Enter First Number: ")
l.grid(row=0)
l = Label(text="Enter Second Number: ")
l.grid(row=1)
textbox = Entry(root, textvariable=first)
textbox.grid(row=0, column=2)
textbox = Entry(root, textvariable=second)
textbox.grid(row=1, column=2)
Button(root, text="Calculate", command=cal).grid(row=2, column=2)
root.mainloop()
