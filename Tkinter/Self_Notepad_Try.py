from distutils import command
from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Notepad++")

main_menu = Menu(root)

file_menu = Menu(main_menu,tearoff=0)
# creating first item menu := File
file_menu.add_command(label="New")
file_menu.add_command(label="New Window")
file_menu.add_command(label="Open..")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As...")

file_menu.add_separator()

file_menu.add_command(label="Page Setup...")
file_menu.add_command(label="Print")

file_menu.add_separator()

file_menu.add_command(label="Exit",command=quit)

main_menu.add_cascade(label="File",menu=file_menu)

# Creating second option :- Edit
edit_menu = Menu(main_menu,tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_separator()

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Delete")

edit_menu.add_separator()

edit_menu.add_command(label="Sesrch with Bing...")
edit_menu.add_command(label="Find")
edit_menu.add_command(label="Find Next")
edit_menu.add_command(label="Find Previous")
edit_menu.add_command(label="Replace...")
edit_menu.add_command(label="Go To...")

edit_menu.add_separator()
edit_menu.add_command(label="Select All")
edit_menu.add_command(label="Date/Time")

main_menu.add_cascade(label="Edit",menu=edit_menu)

root.config(menu=main_menu)
root.mainloop()