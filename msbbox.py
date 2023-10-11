from tkinter import *
from tkinter import messagebox
#import tkinter as a

w = Tk()

tog = 0

def showMessage():
    global tog
    txt.insert(0,"HELLO ...!!")
    msg = messagebox.showinfo("","OHAYO ..!!")

    if(tog == 0):
        btn_display.config(text="SAYONARA")
        btn_display.config(fg="green",bg="yellow")
        tog = 1
    else:
        btn_display.config(text="DISPLAY")
        btn_display.config(fg="yellow",bg="black")
        tog = 0

mode = 1
def mode():
    global mode
    txt.insert(0,"")
    if(mode == 0):
        w.config(bg="black")
        btn_mode.config(text="LIGHT")
        txt.insert(0,"ABBA JABBA")
        mode = 1
    else:
        w.config(bg="white")
        btn_mode.config(text="DARK")
        txt.insert(0,"DABBA")
        mode = 0
    

#input box
txt = Entry(w,text="",fg="blue",font=("Times New Roman",20))
txt.pack()

#exit btn Creation
btn_exit = Button(w,text="EXIT",fg="red",font=("Arial",10),command=w.destroy)
btn_exit.pack()
btn_exit.place(x=180,y=50)

#display btn creation
btn_display = Button(w,text="DISPLAY",fg="green",font=("Arial",10),command=showMessage)
btn_display.pack()
btn_display.place(x=90,y=50)

btn_mode = Button(w,text="DARK",fg="purple",font=("Arial",10),command=mode)
btn_mode.pack()
btn_mode.place(x=120,y=90)

btn_mode = Button(w,text="CLEAR",fg="purple",font=("Arial",10),command=txt.insert(0,""))
btn_mode.pack()
btn_mode.place(x=120,y=130)

w.geometry("300x300")
w.mainloop()

