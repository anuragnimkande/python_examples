from tkinter import *
import time
from urllib.request import Request, urlopen

def call2(): 
    global s
    s.write(b"1")

def call1():
    global s
    s.write(b"0")

def random():
    i = 1
    while(i<10):
        call1()
        time.sleep(1)
        call2()
        time.sleep(1)
        i = i + 1

def send1():
    url = 'http://mdbelectrosoft.in/MDBES/Workshop.php?unit=30&sensor='
    req = Request(url + "1", headers={'User-Agent': 'XYZ/3.0'})
    response = urlopen(req, timeout=4).read()
    print(response)

def send0():
    url = 'http://mdbelectrosoft.in/MDBES/Workshop.php?unit=30&sensor='
    req = Request(url + "0", headers={'User-Agent': 'XYZ/3.0'})
    response = urlopen(req, timeout=4).read()
    print(response)


win = Tk()
b1 = Button(win,text="ON",command=send1,font=("Arial",20),bd=5,fg="green")
b1.grid(row=1,column=1)

b2 = Button(win,text="OFF",command=send0,font=("Arial",20),bd=5,fg="red")
b2.grid(row=1,column=2)




win.mainloop()
