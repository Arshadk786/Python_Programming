from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Frames")
f = Frame(root, bg= "red", borderwidth=5, relief="groove")
f.pack(side="left", fill= Y)
l = Label(f,text="I am in the Frame",bg= "red", fg= "yellow")
l.pack(padx= 40, pady= 20)
f2 = Frame(root,bg="yellow", borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP, fill= X, padx=10)
l = Label(f2, text= "Welcome To Heading", padx=20, bg="yellow", fg= "red")
l.pack()
root.mainloop()