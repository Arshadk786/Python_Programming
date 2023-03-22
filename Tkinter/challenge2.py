from textwrap import fill
from tkinter import *
root = Tk()
root.title("Times Of India")
root.geometry("800x400")
Sp = PhotoImage(file="spidey.png")
article_pic =Label(image=Sp, padx=30, pady=20, borderwidth=5, relief="groove", bg="red")
article_pic.pack(padx=20, pady=30, side="top", fill=X)
content = Label(text="Spider-Man: No Way Home is being credited for revitalising the box office amid a pandemic. \nThe film has exceeded every expectation and is now the sixth-biggest grosser at the worldwide box office. \nThis would have been impressive before the pandemic, but for it to \nhappen now it is downright exceptional, even for an MCU movie.", padx=10, pady= 50, font="arial 19 italic", bg="cyan")
content.pack(padx=20, pady=30, side="top", fill=X)
root.mainloop()