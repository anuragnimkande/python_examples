from tkinter import *

win = Tk()
win.title("ADDITION")

def add():
    e3.delete(0,"end")
    e3.insert(0,int(e1.get())+int(e2.get()))

def sub():
    e3.delete(0,"end")
    e3.insert(0,int(e1.get())-int(e2.get()))

def mul():
    e3.delete(0,"end")
    e3.insert(text=int(e1.get())*int(e2.get()))

def div():
    e3.delete(0,"end")
    e3.config(text=int(e1.get())/int(e2.get()))

l1 = Label(win,text="ENTER 1ST NO : ",font=("Times New Roman",12))
l1.grid(row=1,column=1)
e1 = Entry(win,text="",font=("Times New Roman",12))
e1.grid(row=1,column=2)

l2 = Label(win,text="ENTER 2ND NO : ",font=("Times New Roman",12))
l2.grid(row=2,column=1)
e2 = Entry(win,text="",font=("Times New Roman",12))
e2.grid(row=2,column=2)

l3 = Label(win,text="RESULT : ",font=("Times New Roman",12))
l3.grid(row=3,column=1)
e3 = Entry(win,text="",font=("Times New Roman",12))
e3.grid(row=3,column=2)


btn1 = Button(win,text="ADD",command=add,bg="black",fg="white",font=("Times New Roman",12))
btn1.grid(row=4,column=1)

btn2 = Button(win,text="SUB",command=sub,bg="black",fg="white",font=("Times New Roman",12))
btn2.grid(row=4,column=2)

btn3 = Button(win,text="MUL",command=mul,bg="black",fg="white",font=("Times New Roman",12))
btn3.grid(row=5,column=1)

btn4 = Button(win,text="DIV",command=div,bg="black",fg="white",font=("Times New Roman",12))
btn4.grid(row=5,column=2)

win.mainloop()
