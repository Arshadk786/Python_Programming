from tkinter import *
import tkinter.messagebox as mb

def msb():
    mb.showinfo("Info", "You have Clicked on the button")
def askQues():
    value = mb.askquestion("Question","Do you want to click again?")
    if value == "yes":
        print("You Cannot")
    else:
        print("Thank you for clicking")
    
def arc():  #askretrycancel
    a = mb.askretrycancel("Question","Do you want to click again?")
    print(a)
    if a == True:
        mb.showinfo("Info", "Pls Dont")
    else:
        mb.showinfo("Question","GOOD")
    
    
root = Tk()
Button(text="Click me",command=msb, relief=RAISED).pack(side=TOP)
Button(text="Click me",command=askQues, relief=RAISED).pack(side=TOP)
Button(text="Click me",command=arc, relief=RAISED).pack(side=TOP)
root.mainloop()