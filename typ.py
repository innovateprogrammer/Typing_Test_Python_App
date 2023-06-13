from tkinter import *
from datetime import datetime
wino=Tk()
wino.title("Typing test by Aditya Gadre")
wino.geometry("1200x1200")
wino.configure(bg="Aqua")
global start
global end
global ded
ded="Mistake Analyzer : \n"
def calcu():
    global ded
    mis=0
    acc=0
    t=stopWatch(end-start)
    l=para.split()
    l1=len(para)
    para1=text.get()
    l2=len(para1)
    if(l2>l1):
        para1=para1[:l1]
    lis=para1.split()
    l2=len(para1)
    w=len(lis)
    speed=int(w/t)
    
    deda=""
    for x in l:
        if(x not in lis):
                mis+=1
                
    for y in lis:
        if(y not in l):
            ded+=str(y)+"\n"
    err=abs(l1-l2)
    mis+=err
    acc=((l1-mis)/l1)*100
    if(acc<0.0):
        acc=0.0
    
    deda+="Speed : "+str(speed)+" Words per minute\n"
    deda+="Accuracy = "+str(acc)
    leba.config(text=deda)
    mkd.config(text=ded)
    
def strt():
    global start
    text.config(state="normal")
    start=datetime.now()

def endt():
    global end
    end=datetime.now()
    text.config(state="disabled")
    calcu()

def ext():
    wino.destroy()
    
def stopWatch(value):

    valueD =(((value/365)/24)/60)
    valueH =(valueD)*365
    valueM = (valueH)*24
    v=str(valueM)
    s=""
    for d in v:
        if(d.isdigit()==True or d=="."):
            s+=d
    f=float(s)
    return f
    


para="Lorem Ipsum is simply dummy text of the printing \n and typesetting industry. Lorem Ipsum has been \n the industry's standard dummy text ever since the\n 1500s, when an unknown printer took a \n gallery of type and scrambled it to make a type specimen book."
leb=Label(wino,text=para,fg="white",bg="black",width=70,height=10)
leb.place(x=50,y=100)
lebs=Label(wino,text="Write above text",bg="white",width=30,height=2)
lebs.place(x=170,y=260)
button1=Button(text="Start",command=strt,width=10,height=2)
button1.place(x=50,y=320)

button2=Button(text="Submit",command=endt,width=10,height=2)
button2.place(x=200,y=320)
text=Entry(wino,width=30,font=('Helvetica',24))
text.place(x=50,y=400)
text.config(state="disabled")
mkd=Label(wino,text="Mistake Analyzer : ",bg="white",width=50,height=30)
mkd.place(x=600,y=100)
leba=Label(wino,text="",fg="white",bg="grey",width=70,height=10)
leba.place(x=50,y=500)
button3=Button(wino,text="Exit",command=ext,width=10,height=2)
button3.place(x=400,y=320)
mainloop()
    
        
        