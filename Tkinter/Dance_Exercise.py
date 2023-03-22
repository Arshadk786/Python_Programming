from  tkinter import *

def display():
    print(f"First Name: {first.get()}")
    print(f"Last Name: {last.get()}")
    print(f"Location: {loc.get()}")
    with open("Dance.txt","a") as f:
        f.write(f"First Name: {first.get()}\n")
        f.write(f"Last Name: {last.get()}\n")
        f.write(f"Location: {loc.get()}\n\n")
        f.close()
    
root = Tk()
root.title("Dance Academy Form")
root.geometry("800x500")
root.maxsize(1366, 768)

first = StringVar()
last = StringVar()
loc = StringVar()

Label(text="Admission Form", font="calibri 24 bold underline").grid(row=0, column= 55)
Label(text="First Name: ", font="calibri 15 bold").grid(row=1, column=2)

first_entry = Entry(root, textvariable=first)
first_entry.grid(row=1,column=3)

Label(text="Last Name: ", font="calibri 15 bold").grid(row=2, column=2)
last_entry = Entry(root, textvariable=last)
last_entry.grid(row=2, column=3)

Label(text="Location: ", font="calibri 15 bold").grid(row=3, column=2)
loc_entry = Entry(root, textvariable=loc)
loc_entry.grid(row=3, column=3)

Button(text="Submit", command=display, padx=10, pady=10).grid(row=4, column=3)

root.mainloop()