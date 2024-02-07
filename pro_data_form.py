# -*- coding: utf-8 -*-
"""
Created on Fri May 13 23:23:36 2022

@author: DM
"""
import pymysql
from tkinter import Canvas,Button,Entry,Label
import tkinter
from tkinter import ttk
from tkinter import messagebox

#INSERT
def pro_insert():
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
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0:
              messagebox.showinfo("Save","Some entry is empty check it")
        else:
              s="insert into product values('%s','%s','%s','%s')"%(a,b,c,d)
              cur.execute(s)
              db.commit()
               
            
              messagebox.showinfo("Save","Data saved")
              e1.delete(0,100)
              e2.delete(0,100)
              e3.delete(0,100)
              e4.delete(0,100)
        
        
        db.close()
    
    def bck():
        t.destroy()
        
    def fill_pcatid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select pcatid from product_category" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
       
      # insert form

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Insert Product',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e1.place(x=350,y=150)
    l2=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=ttk.Combobox(t,width=20)
    e2.place(x=350,y=190)
    data=fill_pcatid()
    e2['values']=data
    l3=Label(t,text='Model', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Description', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    
    
    btn1=Button(t,text="Save", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=insert)
    btn1.place(x=200,y=370)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=370)

    t.mainloop()
 
#DELETE
def pro_delete():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Delete')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_delete.ico")
    def de():
       
       db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
       cur=db.cursor()
       
       x=str(e1.get())
       if len(x)==0:
             messagebox.showinfo("Delete","Product Id entry is empty.\n Please fill it first.")
       else:
           s="delete from product where pid='%s'"%(x)
           cur.execute(s)
           db.commit()
           messagebox.showinfo("Delete","Data Deleted")
           e1.delete(0,100)
           db.close()
       
   
        
    def fill_pid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select pid from product" 
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
    c.create_text(250,20,text='Delete Product',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',16))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_pid()
    e1['values']=data
    
    btn1=Button(t,text="Delete", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=de)
    btn1.place(x=200,y=250)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=bck)
    btn2.place(x=400,y=250)

    t.mainloop()


# UPDATE
def pro_update():
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
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0:
              messagebox.showinfo("Update","Some entry is empty check it")
       
        else: 
            s="update product set pcatid='%s',model='%s',pro_desc='%s' where pid='%s'"%(b,c,d,a)
            cur.execute(s)
            db.commit()
           
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
           
            messagebox.showinfo("Update","Update done")
            db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Product Id entry is empty. Please fill it first")
        else:
            s="select pcatid,model,pro_desc from product where pid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
    
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            
            db.close()
    def fill_pid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select pid from product" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def fill_pcatid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        y=[]
        s="select pcatid from product_category" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            y.append(res[0])
        return y
    
    def bck():
        t.destroy()
       
      # Update

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Update Product',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_pid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=ttk.Combobox(t,width=20)
    e2.place(x=350,y=190)
    data=fill_pcatid()
    e2['values']=data
    l3=Label(t,text='Model', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Description', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)    
    
    btn1=Button(t,text="Update", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=updatedata)
    btn1.place(x=200,y=370)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=370)

    t.mainloop()

# FIND
def pro_find():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Find')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_find.ico")
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Product Id entry is empty. Please fill it first")
        else:
            s="select pcatid,model,pro_desc from product where pid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
    
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            
            db.close()
    def fill_pid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select pid from product" 
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
    c.create_text(250,20,text='Find Product',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_pid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Model', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Description', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)    
    
    btn1=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn1.place(x=350,y=370)

    t.mainloop()


