from tkinter import *

def show(event):
    print(f"You have clicked at {event.x}, {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("800x500")

b1 = Button(text="Click Me!")
b1.pack()

# b1.bind('<Button-1>',quit)
b1.bind('<Double-1>',show)

root.mainloop()