import pymysql
from tkinter import Canvas,Button,Entry,Label,StringVar
import tkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
#INSERT
def callSolved_insert():
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
       
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0:
              messagebox.showinfo("Save","Some entry is empty check it")
        else:
            s="insert into call_solved values('%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f)
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
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Call Reference No. entry is empty.\n Please fill it first.")
        else:
            s="select eng_id,custid,pcatid,pid from call_assign where call_ref_no='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
          
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e5.insert(0,data[4])   
           
            db.close()
    def fill_callrefno():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select call_ref_no from call_assign" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def bck():
        t.destroy()
       
      # insert form

    b1=datetime.now()
    s1=b1.strftime("%d/%m/%Y")
    call_solved=StringVar(t,value=s1)
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Insert Call Solved',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Call Reference No.', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=40)
    e1.place(x=350,y=150)
    data=fill_callrefno()
    e1['values']=data
    btn=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn.place(x=650,y=150)
    l2=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Customer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    l6=Label(t,text='Solved Date', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14),textvariable=call_solved)
    e6.place(x=350,y=350)
    
    
    btn1=Button(t,text="Save", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=insert)
    btn1.place(x=250,y=450)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=450,y=450)

    t.mainloop()

#DELETE
def callSolved_delete():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Delete')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_delete.ico")
    def de():
       
       db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
       cur=db.cursor()
       x=str(e1.get())
       if len(x)==0:
             messagebox.showinfo("Delete","Call Reference No. entry is empty.\n Please fill it first.")
       else:
           s="delete from call_solved where call_ref_no=%s"%(x)
           cur.execute(s)
           db.commit()
           messagebox.showinfo("Delete","Data Deleted")
           e1.delete(0,100)
           db.close()
    def fill_callrefno():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select call_ref_no from call_assign" 
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
    c.create_text(250,20,text='Delete Call_Solved',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Call Reference No.', fg='black',bg='light blue', font=('Arial Rounded MT Bold',16))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=40)
    e1.place(x=350,y=150)
    data=fill_callrefno()
    e1['values']=data
    
    btn1=Button(t,text="Delete", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=de)
    btn1.place(x=250,y=250)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=bck)
    btn2.place(x=450,y=250)

    t.mainloop()


# UPDATE
def callSolved_update():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Update')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_update.ico")
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(e6.get())
       
        if len(a)==0 or len(b)==0 :
              messagebox.showinfo("Update","Some entry is empty.\n Please fill it first.")
        else:
            
            s="update call_solved set solved_date='%s' where call_ref_no='%s'"%(b,a)
            cur.execute(s)
            db.commit()
           
            e1.delete(0,100)
            e6.delete(0,100)
           
           
            messagebox.showinfo("Update","Update done")
            db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0 :
              messagebox.showinfo("Find","Call Reference No. entry is empty.\n Please fill it first.")
        else:
            s="select eng_id,custid,pcatid,pid,solved_date from call_solved where call_ref_no='%s'"%(x)
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
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select call_ref_no from call_solved" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def bck():
        t.destroy()
       
      # Update

    b1=datetime.now()
    s1=b1.strftime("%d/%m/%Y")
    call_solved=StringVar(t,value=s1)
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Update Call Solved',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Call Reference No.', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=40)
    e1.place(x=350,y=150)
    data=filldata()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=650,y=150)
   
    l2=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Customer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    l6=Label(t,text='Solved Date', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,textvariable=call_solved,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
    
    
    
    btn1=Button(t,text="Update", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=updatedata)
    btn1.place(x=250,y=450)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=450,y=450)

    t.mainloop()

# FIND
def callSolved_find():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Find')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_find.ico")
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        if len(x)==0:
              messagebox.showinfo("Find","Call Reference No. entry is empty.\n Please fill it first.")
        else:
            s="select eng_id,custid,pcatid,pid,solved_date from call_solved where call_ref_no='%s'"%(x)
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
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select call_ref_no from call_solved" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def bck():
        t.destroy()
       
      # Find

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Find Call Solved',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Call Reference No.', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=40)
    e1.place(x=350,y=150)
    data=filldata()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=650,y=150)
   
    l2=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e2.place(x=350,y=190)
    l3=Label(t,text='Customer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e3.place(x=350,y=230)
    l4=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e4.place(x=350,y=270)
    l5=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e5.place(x=350,y=310)
    l6=Label(t,text='Solved Date', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
    
    btn1=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn1.place(x=350,y=450)

    t.mainloop()

