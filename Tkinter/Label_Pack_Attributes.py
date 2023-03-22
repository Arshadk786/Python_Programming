from textwrap import fill
from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Arshad's Project")
root_label = Label(text='''
                   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod \ntempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim \nveniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea \ncommodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                   velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint \noccaecat cupidatat non proident, sunt in culpa qui officia deserunt \nmollit anim id est laborum.''', bg="grey", fg="black", font="algerian 19 bold", padx=50, pady=40, borderwidth=7, relief="solid")
root_label.pack(anchor="w", side="left", fill=Y)
root.mainloop()