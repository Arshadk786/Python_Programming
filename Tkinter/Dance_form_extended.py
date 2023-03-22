from tkinter import *

def display():
    print(f"First Name: {first_name.get()}")
    print(f"Last Name: {last_name.get()}")
    print(f"Dob: {dob.get()}")
    print(f"Age: {age.get()}")
    
    with open("Dance_form_extended.txt","a") as f:
        f.write(f"First Name: {first_name.get()}\n")
        f.write(f"Last Name: {last_name.get()}\n")
        f.write(f"Dob: {dob.get()}\n")
        f.write(f"Age: {age.get()}\n\n")

root = Tk()
root.title("Dance Admission Form")
root.geometry("800x500")

heading = Label(root, text="ADMISSION FORM", font="consolas 24 bold underline")
heading.grid(row= 0, column= 0)

Label(root, text="First Name: ",font="consolas 16 bold").grid(row=1, column=0)
Label(root, text="Last Name: ",font="consolas 16 bold").grid(row=2, column=0)
Label(root, text="DOB: ",font="consolas 16 bold").grid(row=3, column=0)
Label(root, text="Age: ",font="consolas 16 bold").grid(row=4, column=0)

first_name = StringVar()
last_name = StringVar()
dob = StringVar()
age = IntVar()

first_entry = Entry(root, textvariable=first_name).grid(row=1, column=1)
last_entry = Entry(root, textvariable=last_name).grid(row=2, column=1)
dob_entry = Entry(root, textvariable=dob).grid(row=3, column=1)
age_entry = Entry(root, textvariable=age).grid(row=4, column=1)

Button(text="Submit",command=display, padx=7, pady=7,bg="red", fg="white").grid(row=5, column=1)

root.mainloop()