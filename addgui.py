from tkinter import *

win = Tk()
win.title("ADDITION")

def add():
    e3.insert(0,int(e1.get())+int(e2.get()))

e1 = Entry(win,text="")
e1.pack()

e2 = Entry(win,text="")
e2.pack()

e3 = Entry(win,text="")
e3.pack()

btn = Button(win,text="ADD",command=add)
btn.pack()
btn.flash()


win.geometry("400x400")
win.mainloop()
