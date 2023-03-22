from tkinter import *
root = Tk()
root.title("Button")
root.geometry("800x500")
root.maxsize(1366, 768)

def name1():
    print(1)
    
def name2():
    print(2)
    
def name3():
    print(3)
    
def name4():
    print(4)
    
f1 = Frame(root, bg= "grey", borderwidth=5, relief="sunken")
f1.pack(side="left", anchor="nw")
b1 = Button(f1,bg= "red",fg="white", text="Button1", padx=10, pady=10, command=name1)
b1.pack(side="left", anchor="nw", padx=5)

b2 = Button(f1,bg= "red",fg="white", text="Button2", padx=10, pady=10, command=name2)
b2.pack(side="left", anchor="nw", padx=5)

b3 = Button(f1,bg= "red",fg="white", text="Button3", padx=10, pady=10, command=name3)
b3.pack(side="left", anchor="nw", padx=5)

b4 = Button(f1,bg= "red",fg="white", text="Button4", padx=10, pady=10, command=name4)
b4.pack(side="left", anchor="nw",padx=5)
root.mainloop()