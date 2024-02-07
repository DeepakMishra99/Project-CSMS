# -*- coding: utf-8 -*-
"""
Created on Sat May 14 01:10:04 2022

@author: DM
"""

import pymysql
from tkinter import Canvas,Button,Entry,Label
import tkinter
from tkinter import ttk
from tkinter import messagebox

#INSERT
def sm_insert():
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
        e=int(e5.get())
        f=int(e6.get())
        g=int(e7.get())
        h=str(e8.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(h)==0:
              messagebox.showinfo("Save","Some entry is empty.\n Please fill it first.")
        else:
        
            s="insert into service_master values('%s','%s','%s','%s',%d,%d,%d,'%s')"%(a,b,c,d,e,f,g,h)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Save","Data saved")
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e8.delete(0,100)
            
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
    def fill_pid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          y=[]
          s="select pid from product"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              y.append(res[0])
          return y
    
        
    def total():
        n1=int(e5.get())
        n2=int(e6.get())
        tota=n1+n2
        e7.insert(0,tota)
        
        
    
    def bck():
        t.destroy()
       
      # insert form

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Insert Service Master',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Service Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e1.place(x=350,y=150)
    l2=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=ttk.Combobox(t,width=20)
    e2.place(x=350,y=190)
    data1=fill_pcatid()
    e2['values']=data1
    l3=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=ttk.Combobox(t,width=20)
    e3.place(x=350,y=230)
    data2=fill_pid()
    e3['values']=data2
    l4=Label(t,text='Service Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Spare Cost', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    l6=Label(t,text='Service Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
   
    l7=Label(t,text='Total Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=390)
    e7=Entry(t,width=20,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e7.place(x=350,y=390)
    btn=Button(t,text="Total", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=total)
    btn.place(x=600,y=390)
    l8=Label(t,text='Service Duration', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l8.place(x=100,y=430)
    e8=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e8.place(x=350,y=430)
    
    
    btn1=Button(t,text="Save", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=insert)
    btn1.place(x=200,y=530)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=530)

    t.mainloop()
    
#DELETE
def sm_delete():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Delete')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_delete.ico")
    def de():
       
       db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
       cur=db.cursor()
       x=str(e1.get())
       if len(x)==0:
             messagebox.showinfo("Delete","Service Id entry is empty.\n Please fill it first.")
       else:
           s="delete from service_master where service_id='%s'"%(x)
           cur.execute(s)
           db.commit()
           messagebox.showinfo("Delete","Data Deleted")
           e1.delete(0,100)
           db.close()
    def fill_serviceid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select service_id from service_master"
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
    c.create_text(250,20,text='Delete Service Master',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Service Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',16))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_serviceid()
    e1['values']=data
    
    btn1=Button(t,text="Delete", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=de)
    btn1.place(x=200,y=250)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=bck)
    btn2.place(x=400,y=250)

    t.mainloop()


# UPDATE
def sm_update():
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
        e=int(e5.get())
        f=int(e6.get())
        g=int(e7.get())
        h=str(e8.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(h)==0:
              messagebox.showinfo("Update","Some entry is empty.\n Please fill it first.")
        else:
            s="update service_master set pcatid='%s',pid='%s',service_name='%s',spare_cost=%d,service_charge=%d,total_charge=%d,service_dur='%s' where service_id='%s'"%(b,c,d,e,f,g,h,a)
            cur.execute(s)
            db.commit()
           
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e8.delete(0,100)
            messagebox.showinfo("Update","Update done")
            db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Service Id entry is empty.\n Please fill it first.")
        else:
            s="select pcatid,pid,service_name,spare_cost,service_charge,total_charge,service_dur from service_master where service_id='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
    
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e8.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            e7.insert(0,data[5])
            e8.insert(0,data[6])
            db.close()
    def fill_serviceid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select service_id from service_master" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
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
    def fill_pid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          y=[]
          s="select pid from product"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              y.append(res[0])
          return y
    def total():
        n1=int(e5.get())
        n2=int(e6.get())
        tota=n1+n2
        e7.insert(0,tota)
    
    
    def bck():
        t.destroy()
       
      # Update

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Update Service Master',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Service Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_serviceid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=ttk.Combobox(t,width=20)
    e2.place(x=350,y=190)
    data1=fill_pcatid()
    e2['values']=data1
    l3=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=ttk.Combobox(t,width=20)
    e3.place(x=350,y=230)
    data2=fill_pid()
    e3['values']=data2
    l4=Label(t,text='Service Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Spare Cost', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    l6=Label(t,text='Service Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
    l7=Label(t,text='Total Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=390)
    e7=Entry(t,width=20,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e7.place(x=350,y=390)
    btn=Button(t,text="Total", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=total)
    btn.place(x=600,y=390)
    l8=Label(t,text='Service Duration', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l8.place(x=100,y=430)
    e8=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e8.place(x=350,y=430)
    
    
    btn1=Button(t,text="Update", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=updatedata)
    btn1.place(x=200,y=530)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=530)

    t.mainloop()

# FIND
def sm_find():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Find')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_find.ico")
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Service Id entry is empty.\n Please fill it first.")
        else:
            s="select pcatid,pid,service_name,spare_cost,service_charge,total_charge,service_dur from service_master where service_id='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
    
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e8.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            e7.insert(0,data[5])
            e8.insert(0,data[6])
            db.close()
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select service_id from service_master"
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
    c.create_text(250,20,text='Find Service Master',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Service Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=filldata()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Service Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Spare Cost', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    l6=Label(t,text='Service Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
    l7=Label(t,text='Total Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=390)
    e7=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e7.place(x=350,y=390)
    l8=Label(t,text='Service Duration', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l8.place(x=100,y=430)
    e8=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e8.place(x=350,y=430)
    

    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=350,y=530)

    t.mainloop()
