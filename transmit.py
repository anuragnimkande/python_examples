'''from urllib.request import Request, urlopen       
#specify url
url = 'https://mdbelectrosoft.in/MDBES/Workshop.php?unit=44'

while(1):
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    response = urlopen(req, timeout=2).read()
    print(response)
'''

from tkinter import *
from urllib.request import Request, urlopen


'''
#specify url
k = 100
while(1):
    url = 'http://mdbelectrosoft.in/MDBES/Workshop.php?unit=46&sensor='
    req = Request(url + str(k), headers={'User-Agent': 'XYZ/3.0'})
    response = urlopen(req, timeout=4).read()
    print(response)
    k=k-1
'''


def call():
    s = t1.get()
    url = 'http://mdbelectrosoft.in/MDBES/Workshop.php?unit=46&sensor='
    req = Request(url + str(s), headers={'User-Agent': 'XYZ/3.0'})
    response = urlopen(req, timeout=4).read()
    print(response)

win = Tk()

t1 = Entry(win,text="")
t1.pack()

b1 = Button(win,text="SUBMIT",command=call)
b1.pack()


win.mainloop()
