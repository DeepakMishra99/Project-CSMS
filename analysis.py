# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 02:42:41 2022

@author: DM
"""

from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
def analysis():
    
    t=tkinter.Tk()
    t.geometry("1600x800")
    t.title('Analysis')
    
    top_frame = Frame(t, width=1600, height=80)
    top_frame.pack(side='top', fill='both', padx=10, pady=5, expand=True)
     
    bottom_frame = Frame(t, width=1600, height=700,bg='royalblue4')
    bottom_frame.pack(side='bottom', fill='both', padx=10, pady=5, expand=True)
    
     # top frame
    c=Canvas(top_frame,width=1500,height=80,bg="royalblue4")
    c.pack(side='top', padx=1, pady=1)
    c.create_text(700,30,text='Analysis',font=('Copperplate Gothic Bold',40),fill='yellow green')
     
     
     # bottom frame
    c3=Canvas(bottom_frame,width=1600,height=750,bg="grey23")
    c3.pack(side='left', padx=10, pady=10)
    c3.create_text(700,30,text='Welcome to Customer Service Management Analysis',font=('Copperplate Gothic Bold',20,'underline'),fill='yellow green')
    
    db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
    cur=db.cursor()
    
    # product category
    pcat=[]
    s="select count(*) from product_category"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          pcat.append(res[0])
    l1=Label(c3,text="Product Category\n"+str(pcat[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l1.place(x=50,y=100)
    
    # product 
    pro=[]
    s="select count(*) from product"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          pro.append(res[0])
    l2=Label(c3,text="    Product    \n"+str(pro[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l2.place(x=550,y=100)
    
    # Service
    ser=[]
    s="select count(*) from service_master"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          ser.append(res[0])
    l3=Label(c3,text="    Services    \n"+str(ser[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l3.place(x=1050,y=100)
    
    # active engineer
    aeng=[]
    s="select count(*) from engineer where active='1'"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          aeng.append(res[0])
    l4=Label(c3,text="Active Engineers\n"+str(aeng[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l4.place(x=50,y=300)
    
    # deactive engineer
    deng=[]
    s="select count(*) from engineer where active='0'"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          deng.append(res[0])
    l5=Label(c3,text="Deactive Engineers\n"+str(deng[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l5.place(x=550,y=300)
    
    # staff
    staff=[]
    s="select count(*) from call_attendent_staff"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          staff.append(res[0])
    l6=Label(c3,text="     Staff     \n"+str(staff[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l6.place(x=1050,y=300)
    
    # customer
    cust=[]
    s="select count(*) from customer"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          cust.append(res[0])
    l7=Label(c3,text="    Customer    \n"+str(cust[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l7.place(x=50,y=500)
    
    # call assign
    assign=[]
    s="select count(*) from call_Assign"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          assign.append(res[0])
    l8=Label(c3,text="  Call Assigns  \n"+str(assign[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l8.place(x=550,y=500)
    
    # engineer
    solve=[]
    s="select count(*) from call_Solved"
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
          solve.append(res[0])
    l9=Label(c3,text="  Solved Calls  \n"+str(solve[0]), fg='white',bg='olivedrab', font=('Arial Rounded MT Bold',18,'bold'),relief='raised')
    l9.place(x=1050,y=500)
    
    t.mainloop()
