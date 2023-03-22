from tkinter import *

root = Tk()
root.title("Canvas Widget")
canvas_height = 500
canvas_width = 800

root.geometry(f"{canvas_width}x{canvas_height}")
canvas_widget = Canvas(root, height=canvas_height, width=canvas_width)
canvas_widget.pack()

canvas_widget.create_line(0, 0, 800, 500)
canvas_widget.create_line(800, 0, 0, 500)

canvas_widget.create_rectangle(100, 120, 300, 400, fill="blue")

canvas_widget.create_text(400, 250, text="HELLO")

canvas_widget.create_oval(100, 120, 300, 400, fill="red")

img = PhotoImage(file="spidey.png")
canvas_widget.create_image(10,60, image=img,anchor="nw")
root.mainloop()