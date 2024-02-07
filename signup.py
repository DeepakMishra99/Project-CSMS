# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:20:20 2022
s
@author: DM
"""


import pymysql
import tkinter
from tkinter import Canvas,Button,Label,Entry
from tkinter import messagebox

def sign():
    
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title("Signup")
    def signin():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(e2.get())
        c=str(e3.get())
        d=str(e4.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0:
              messagebox.showinfo("Save","Some entry is empty check it")
        else:
        
            s="insert into register values('%s','%s','%s','%s')"%(a,b,c,d)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Save","Data saved")
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            
            db.close()
    def backtologin():
        t.destroy()
    c=Canvas(t,width=800,height=800,bg='DeepPink3',)
    c.place(x=0, y=0)
    
    c1=Canvas(t,width=800,height=800,bg='white')
    c1.pack(padx=80,pady=80)
   
    #login
    c2=Canvas(t,width=300,height=50,bg='MediumPurple4')
    c2.place(x=250,y=100)
    c2.create_text(45,8,text="Create Account!",fill='white',font=('Arial Rounded MT Bold',20,'bold'),justify="center",anchor="nw")
    
    
   
    
    
    #Fullname
    l1=Label(c1,text='Full Name:', fg='purple4',bg='white', font=('Arial Rounded MT Bold',16))
    l1.place(x=80,y=150)
    e1=Entry(c1,width=20,bd=2,relief='groove',font=('Arial Rounded MT Bold',16))
    e1.place(x=250,y=150)
    
    #Date of Birth
    l2=Label(c1,text='Date of Birth:', fg='purple4',bg='white', font=('Arial Rounded MT Bold',16))
    l2.place(x=80,y=190)  
    e2=Entry(c1,width=20,bd=2,relief='groove',font=('Arial Rounded MT Bold',16))    
    e2.place(x=250,y=190)
    
    # Email
    l3=Label(c1,text='Email:', fg='purple4',bg='white', font=('Arial Rounded MT Bold',16))
    l3.place(x=80,y=230)
    e3=Entry(c1,width=20,bd=2,relief='groove',font=('Arial Rounded MT Bold',16))
    e3.place(x=250,y=230)
    
    # Password
    l4=Label(c1,text='Password:', fg='purple4',bg='white', font=('Arial Rounded MT Bold',16))
    l4.place(x=80,y=270)
    e4=Entry(c1,width=20,bd=2,show='*',relief='groove',font=('Arial Rounded MT Bold',16))
    e4.place(x=250,y=270)
            
     #Create Button     
    btn1=Button(c1,text="Create", fg="white",bg="MediumPurple4",font=('Arial Rounded MT Bold',16),command=signin)
    btn1.place(x=250,y=350)
    
    # signin
    l5=Label(t,text='If you have an account:\t\t', fg='Black',bg='white', font=('Arial Rounded MT Bold',12))
    l5.place(x=150,y=500)
    btn3=Button(t,text="Signin", fg="white",bg="DeepPink3",font=('Arial Rounded MT Bold',10),activeforeground="red",command=backtologin)
    btn3.place(x=350,y=500)
     
    
    t.mainloop()
