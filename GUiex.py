from tkinter import *
from tkinter import messagebox
#import tkinter as a

w = Tk()

def showMessage():
    msg = messagebox.showinfo("INFO","ELVISHH BHAII ...!!")

#Button Creation
btn = Button(w,text="SUBMIT",command=showMessage)
btn.pack()
btn.place(x=30,y=50)


w.mainloop()

