from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x500")
root.minsize(500, 200)
root.maxsize(1366, 768)
# photo = PhotoImage(file="photo-1553095066-5014bc7b7f2d.jpg")
image = Image.open("photo-1553095066-5014bc7b7f2d.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()
root.mainloop()
