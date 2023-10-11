from tkinter  import *

win = Tk()
win.title("TIC-TAC-TOE")

 #add X or O
flag = 0
tie = 0
count = 0
def click(b):
    global flag,count,tie
    if(b.cget("text") == "" and tie == 0):
        if(flag == 0):
            l1.config(text="O TURN")
            b.config(text="X",bg="lightgreen")
            flag = 1
            count = count + 1
        else:
            l1.config(text="X TURN")
            b.config(text="O",bg="lightblue")
            flag = 0
            count = count + 1

    if(b1.cget("text") == "X" and b2.cget("text") == "X" and b3.cget("text") == "X" or
       b4.cget("text") == "X" and b5.cget("text") == "X" and b6.cget("text") == "X" or
       b7.cget("text") == "X" and b8.cget("text") == "X" and b9.cget("text") == "X" or
       b1.cget("text") == "X" and b4.cget("text") == "X" and b7.cget("text") == "X" or
       b2.cget("text") == "X" and b5.cget("text") == "X" and b8.cget("text") == "X" or
       b3.cget("text") == "X" and b6.cget("text") == "X" and b9.cget("text") == "X" or
       b1.cget("text") == "X" and b5.cget("text") == "X" and b9.cget("text") == "X" or
       b3.cget("text") == "X" and b5.cget("text") == "X" and b7.cget("text") == "X"):
        l1.config(text="X WON",bg="green",fg="black")
        tie = 1
    elif(b1.cget("text") == "O" and b2.cget("text") == "O" and b3.cget("text") == "O" or
       b4.cget("text") == "O" and b5.cget("text") == "O" and b6.cget("text") == "O" or
       b7.cget("text") == "O" and b8.cget("text") == "O" and b9.cget("text") == "O" or
       b1.cget("text") == "O" and b4.cget("text") == "O" and b7.cget("text") == "O" or
       b2.cget("text") == "O" and b5.cget("text") == "O" and b8.cget("text") == "O" or
       b3.cget("text") == "O" and b6.cget("text") == "O" and b9.cget("text") == "O" or
       b1.cget("text") == "O" and b5.cget("text") == "O" and b9.cget("text") == "O" or
       b3.cget("text") == "O" and b5.cget("text") == "O" and b7.cget("text") == "O"):
        l1.config(text="O WON",bg="green",fg="black")
        tie = 1
    elif(count == 9):
        l1.config(text="TIE",bg="red")
        tie = 1
        
    

#1ST FRAME
f1 = Frame(win)
f1.pack()

b1 = Button(f1,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b1))
b1.pack(side=LEFT)
b2 = Button(f1,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b2))
b2.pack(side=LEFT)
b3 = Button(f1,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b3))
b3.pack(side=LEFT)

#2ND FRAME
f2 = Frame(win)
f2.pack()

b4 = Button(f2,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b4))
b4.pack(side=LEFT)
b5 = Button(f2,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b5))
b5.pack(side=LEFT)
b6 = Button(f2,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b6))
b6.pack(side=LEFT)

#3RD FRAME
f3 = Frame(win)
f3.pack()

b7 = Button(f3,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b7))
b7.pack(side=LEFT)
b8 = Button(f3,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b8))
b8.pack(side=LEFT)
b9 = Button(f3,text="",width=15,height=7,bd=15,bg="peachpuff",font=('Arial',15),command=lambda:click(b9))
b9.pack(side=LEFT)

#4TH FRAME
f4 = Frame(win)
f4.pack()

l1 = Label(f4,text="PLAYING",font=("Helvetica",25))
l1.pack()

#win.geometry("500x500")
win.mainloop()
