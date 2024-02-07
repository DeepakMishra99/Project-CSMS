# -*- coding: utf-8 -*-
"""
Created on Sat May 14 01:57:48 2022

@author: DM
"""

import pymysql
import random
from tkinter import Canvas,Button,Entry,Label
import tkinter
from tkinter import ttk
from tkinter import messagebox

#INSERT
def cas_insert():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Insert')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_insert.ico")
    def insert():
    
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(e2.get())
        c=str(e3.get())
        d=str(e4.get())
        e=str(e5.get())
        f=int(e6.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0:
              messagebox.showinfo("Save","Some entry is empty check it")
        else:
            s="insert into call_attendent_staff values('%s','%s','%s','%s','%s',%d)"%(a,b,c,d,e,f)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Save","Data saved")
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            db.close()
    
    def email():
        em=e5.get()
        import smtplib
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('mishradeepak0101@gmail.com','deera@1910')
        email.otp=random.randint(1000,9999)
        a="Your OTP is "+str( email.otp) +"\n Don't share to anyone."
        
        s.sendmail('mishradeepak0101@gmail.com',em,a)
        messagebox.showinfo("Send OTP","OTP is send.")
        
        s.quit()
        
    def verify():
        
        a=int(ent_otp.get())
        if a==email.otp:
            messagebox.showinfo("Verify","You are verified.\n Thankyou for your verification.")
        else:
            messagebox.showinfo("Verify","Your OTP is incorrect.")
    def bck():
        t.destroy()
       
      # insert form

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Insert Call Attendent Staff',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Staff Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e1.place(x=350,y=150)
    l2=Label(t,text='Staff Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Phone', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Address', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Email', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    BT=Button(t,text="Send OTP", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',12),activeforeground="red",command=email)
    BT.place(x=700,y=310)
    
    otp=Label(t,text='OTP', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    otp.place(x=350,y=350)
    ent_otp=Entry(t,width=20,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    ent_otp.place(x=400,y=350)
    BT=Button(t,text="Verify", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',12),activeforeground="red",command=verify)
    BT.place(x=700,y=350)
    
    l6=Label(t,text='Active', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=390)
    e6=ttk.Combobox(t,width=20)
    e6.place(x=350,y=390)
    data=['1','0']
    e6['values']=data
    
    
    
    btn1=Button(t,text="Save", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=insert)
    btn1.place(x=250,y=490)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=450,y=490)

    t.mainloop()

    
#DELETE
def cas_delete():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Delete')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_delete.ico")
    def de():
       
       db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
       cur=db.cursor()
       x=str(e1.get())
       if len(x)==0:
             messagebox.showinfo("Delete","Staff Id entry is empty.\n Please fill it first.")
       else:
           s="delete from call_attendent_staff where staffid=%s"%(x)
           cur.execute(s)
           db.commit()
           messagebox.showinfo("Delete","Data Deleted")
           e1.delete(0,100)
           db.close()
    def fill_staffid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select staffid from call_attendent_staff" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def bck():
        t.destroy()
       
     # delete

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Delete Call Attendent Staff',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Staff Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',16))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_staffid()
    e1['values']=data
    
    btn1=Button(t,text="Delete", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=de)
    btn1.place(x=250,y=250)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=bck)
    btn2.place(x=450,y=250)

    t.mainloop()


# UPDATE
def cas_update():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Update')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_update.ico")
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(e2.get())
        c=str(e3.get())
        d=str(e4.get())
        e=str(e5.get())
        f=int(e6.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0:
              messagebox.showinfo("Update","Some entry is empty check it")
        else:
            s="update call_attendent_staff set staff_name='%s',phone='%s',address=='%s',email=='%s',active=%d where staffid='%s'"%(b,c,d,e,f,a)
            cur.execute(s)
            db.commit()
           
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
           
            messagebox.showinfo("Update","Update done")
            db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Staff Id entry is empty.\n Please fill it first.")
        else:
            s="select staff_name,phone,address,email,active from call_attendent_staff where staffid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])        
            db.close()
    def fill_staffid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select staffid from call_attendent_staff" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def email():
        em=e5.get()
        import smtplib
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('mishradeepak0101@gmail.com','deera@1910')
        email.otp=random.randint(1000,9999)
        a="Your OTP is "+str( email.otp) +"\n Don't share to anyone."
        
        s.sendmail('mishradeepak0101@gmail.com',em,a)
        messagebox.showinfo("Send OTP","OTP is send.")
        
        s.quit()
        
    def verify():
        
        a=int(ent_otp.get())
        if a==email.otp:
            messagebox.showinfo("Verify","You are verified.\n Thankyou for your verification.")
        else:
            messagebox.showinfo("Verify","Your OTP is incorrect.")
    def bck():
        t.destroy()
       
      # Update

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Update Call Attendent Staff',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Staff Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_staffid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Staff Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Phone', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Address', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Email', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    BT=Button(t,text="Send OTP", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',12),activeforeground="red",command=email)
    BT.place(x=700,y=310)
    
    otp=Label(t,text='OTP', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    otp.place(x=350,y=350)
    ent_otp=Entry(t,width=20,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    ent_otp.place(x=400,y=350)
    BT=Button(t,text="Verify", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',12),activeforeground="red",command=verify)
    BT.place(x=700,y=350)
    
    l6=Label(t,text='Active', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=390)
    e6=ttk.Combobox(t,width=20)
    e6.place(x=350,y=390)
    data=['1','0']
    e6['values']=data
    
    btn1=Button(t,text="Update", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=updatedata)
    btn1.place(x=250,y=490)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=450,y=490)

    t.mainloop()
    
   
    
   

# FIND
def cas_find():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Find')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_find.ico")
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Staff Id entry is empty.\n Please fill it first.")
        else:
            s="select staff_name,phone,address,email,active from call_attendent_staff where staffid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])        
            db.close()
    def fill_staffid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select staffid from call_attendent_staff" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def bck():
        t.destroy()
       
# find

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Find Call Attendent Staff',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Staff Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_staffid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Staff Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Phone', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Address', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Email', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    l6=Label(t,text='Active', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)

    
    btn=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn.place(x=350,y=450)

    t.mainloop()

