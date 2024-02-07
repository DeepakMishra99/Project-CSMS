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
def eng_insert():
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
        f=str(e6.get())
        g=int(e7.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0:
              messagebox.showinfo("Save","Some entry is empty check it")
        else:
            s="insert into engineer values('%s','%s','%s','%s','%s','%s',%d)"%(a,b,c,d,e,f,g)
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
    
    def email():
        em=e5.get()
        import smtplib
        from email.message import EmailMessage
        s=smtplib.SMTP('SMTP-mail.outlook.com',587)
        s.starttls()
        s.login('deemis007@outlook.com','deemis@007')
        email.otp=random.randint(1000,9999)
        a="Your OTP is "+ str(email.otp) +"\n Don't share to anyone."
        print(a)
        msg = EmailMessage()
        msg['subject'] = 'Hello.'   
        msg['from'] ="deemis007@outlook.com"
        msg['to'] = em
        msg.set_content(a) 
        
        
        s.send_message(msg)
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
    c.create_text(250,20,text='Insert Engineer',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e1.place(x=350,y=150)
    l2=Label(t,text='Engineer Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
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
    
    l6=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=390)
    e6=ttk.Combobox(t,width=20)
    e6.place(x=350,y=390)
    data=fill_pcatid()
    e6['values']=data
    l7=Label(t,text='Active', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=430)
    e7=ttk.Combobox(t,width=20)
    e7.place(x=350,y=430)
    data=['1','0']
    e7['values']=data 
    
    
    
    btn1=Button(t,text="Save", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=insert)
    btn1.place(x=200,y=530)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=530)

    t.mainloop()
    
#DELETE
def eng_delete():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Delete')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_delete.ico")
    def de():
       
       db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
       cur=db.cursor()
       x=str(e1.get())
       if len(x)==0:
             messagebox.showinfo("Delete","Engineer Id is empty. \n Please fill it first.")
       else:
           s="delete from engineer where eng_id='%s'"%(x)
           cur.execute(s)
           db.commit()
           messagebox.showinfo("Delete","Data Deleted")
           e1.delete(0,100)
           db.close()
    def fill_engid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select eng_id from engineer"
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
    c.create_text(250,20,text='Delete Engineer',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',16))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_engid()
    e1['values']=data
    
    btn1=Button(t,text="Delete", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=de)
    btn1.place(x=200,y=250)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=bck)
    btn2.place(x=400,y=250)

    t.mainloop()


# UPDATE
def eng_update():
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
        f=str(e6.get())
        g=int(e7.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 :
             messagebox.showinfo("Update","Some entry is empty check it")
        else:
            s="update engineer set eng_name='%s',phone='%s',address='%s',email='%s',pcatid='%s',active=%d where eng_id='%s'"%(b,c,d,e,f,g,a)
            cur.execute(s)
            db.commit()
           
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
           
            messagebox.showinfo("Update","Update done")
            db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Engineer Id is empty. \n Please fill it first.")
        else:
            s="select eng_name,phone,address,email,pcatid,active from engineer where eng_id='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
    
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            e7.insert(0,data[5])
            
            db.close()
    def fill_engid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select eng_id from engineer" 
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
    
    def email():
        em=e5.get()
        import smtplib
        from email.message import EmailMessage
        s=smtplib.SMTP('SMTP-mail.outlook.com',587)
        s.starttls()
        s.login('deemis007@outlook.com','deemis@007')
        email.otp=random.randint(1000,9999)
        a="Your OTP is "+ str(email.otp) +"\n Don't share to anyone."
        print(a)
        msg = EmailMessage()
        msg['subject'] = 'Hello.'   
        msg['from'] ="deemis007@outlook.com"
        msg['to'] = em
        msg.set_content(a) 
        
        
        s.send_message(msg)
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
    c.create_text(250,20,text='Update Engineer',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_engid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Engineer Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
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
    
    l6=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=390)
    e6=ttk.Combobox(t,width=20)
    e6.place(x=350,y=390)
    data=fill_pcatid()
    e6['values']=data
    l7=Label(t,text='Active', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=430)
    e7=ttk.Combobox(t,width=20)
    e7.place(x=350,y=430)
    data=['1','0']
    e7['values']=data 
    
        
    
    btn1=Button(t,text="Update", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=updatedata)
    btn1.place(x=200,y=530)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=400,y=530)

    t.mainloop()

# FIND
def eng_find():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Find')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_find.ico")
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Engineer Id is empty. \n Please fill it first.")
        else:
            s="select eng_name,phone,address,email,pcatid,active from engineer where eng_id='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
    
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            e7.insert(0,data[5])
            
            db.close()
            
    def fill_engid():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select eng_id from engineer"
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
    c.create_text(250,20,text='Find Engineer',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    data=fill_engid()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=550,y=150)
   
    l2=Label(t,text='Engineer Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
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
    l6=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
    l7=Label(t,text='Active', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=390)
    e7=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e7.place(x=350,y=390)    
    
    btn1=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn1.place(x=350,y=490)

    t.mainloop()


