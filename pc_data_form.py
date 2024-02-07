# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:43:51 2022

@author: DM
"""


import pymysql
from tkinter import Canvas,Button,Entry,Label
import tkinter
from tkinter import ttk
from tkinter import messagebox

#INSERT
def pc_insert():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Insert')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_insert.ico")
    def insert():
    
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(e2.get())
        if len(a)==0 or len(b)==0:
              messagebox.showinfo("Save","Product Category Id entry is empty.\n Please fill it first.")
        else:
        
            s="insert into product_category values('%s','%s')"%(a,b)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Save","Data saved")
            e1.delete(0,100)
            e2.delete(0,100)
            
            db.close()
    
    def bck():
        t.destroy()
    
       
      # insert form

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Insert Product Category',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e1.place(x=350,y=150)
    l2=Label(t,text='Category Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    
    
    btn1=Button(t,text="Save", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=insert)
    btn1.place(x=200,y=290)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=290)

    t.mainloop()

    
#DELETE
def pc_delete():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Delete')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_delete.ico")
    def de():
       
       db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
       cur=db.cursor()
       x=str(e1.get())
       if len(x)==0:
             messagebox.showinfo("Delete","Product Category Id entry is empty.\n Please fill it first.")
       else:
           s="delete from product_category where pcatid='%s'"%(x)
           cur.execute(s)
           db.commit()
           messagebox.showinfo("Delete","Data Deleted")
           e1.delete(0,100)
           db.close()
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
    def bck():
        t.destroy()
       
     # delete

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Delete Product Category',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',16))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_pcatid()
    e1['values']=data
    
    btn1=Button(t,text="Delete", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=de)
    btn1.place(x=200,y=250)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=bck)
    btn2.place(x=400,y=250)

    t.mainloop()


# UPDATE
def pc_update():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Update')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_update.ico")
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(e2.get())
        if len(a)==0 or len(b)==0:
              messagebox.showinfo("Update","Product Category Id entry is empty.\n Please fill it first.")
        else:
       
            s="update product_category set catname='%s' where pcatid='%s'"%(b,a)
            cur.execute(s)
            db.commit()
           
            e1.delete(0,100)
            e2.delete(0,100)
           
            messagebox.showinfo("Update","Update done")
            db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Product Category Id entry is empty.\n Please fill it first.")
        else:
            s="select catname from product_category where pcatid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            
            e2.delete(0,100)
            e2.insert(0,data[0])
            
            db.close()
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
    
    def bck():
        t.destroy()
       
      # Update

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Update Product Category',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_pcatid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Category Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',15))
    e2.place(x=350,y=190)    
    
    btn1=Button(t,text="Update", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=updatedata)
    btn1.place(x=200,y=290)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=290)

    t.mainloop()

# FIND
def pc_find():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Find')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_find.ico")
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Product Category Id entry is empty.\n Please fill it first.")
        else:
            s="select catname from product_category where pcatid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            
            e2.delete(0,100)        
            e2.insert(0,data[0])
            
            db.close()
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
    
    def bck():
        t.destroy()
       
# find

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Find Product Category',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_pcatid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Category Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',15))
    e2.place(x=350,y=190)
        
    btn1=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn1.place(x=350,y=290)

    t.mainloop()
