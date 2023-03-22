from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("Tkinter")
label = Label(text="READY", borderwidth=5, relief="groove", padx=50, pady=10, bg= "red", fg= "white", font="arial 19 bold")
label.pack(side="bottom", fill=X)
root.mainloop()