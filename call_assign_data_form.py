# -*- coding: utf-8 -*-
"""
Created on Sat May 14 01:57:48 2022

@author: DM
"""
import pymysql
from tkinter import Canvas,Button,Label,Entry,StringVar
import tkinter
from tkinter import ttk
from tkinter import messagebox 
from datetime import date, timedelta,datetime

import smtplib
import email.mime.multipart
import email.mime.text
import email.mime.base
import os


#INSERT
def callAssign_insert():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Insert')
    #t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_insert.ico")
   
    
   
    def insert():
    
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(e2.get())
        c=str(e3.get())
        d=str(e4.get())
        e=str(e5.get())
        f=str(e6.get())
        g=str(e7.get())
        h=str(e8.get())
        i=str(e9.get())
        j=int(e10.get())
        k=int(e11.get())
        l=int(e12.get())
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(g)==0 or len(h)==0 or len(i)==0:
              messagebox.showinfo("Save","Some entry is empty check it")
        else:
            s="insert into call_assign values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g,h,i,j,k,l)
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
            e9.delete(0,100)
            e10.delete(0,100)
            e11.delete(0,100)
            e12.delete(0,100)
            db.close()
        
    def fill_staffid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          a=[]
          s="select staffid from call_attendent_staff"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              a.append(res[0])
          return a
    def fill_custid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          cust=[]
          s="select custid from customer"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              cust.append(res[0])
          return cust
    def fill_pcatid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          b=[]
          s="select pcatid from product_category"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              b.append(res[0])
          return b
    def fill_pid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
        
         
          d=[]   
          pid="select pid from product"
          cur.execute(pid)
          data1=cur.fetchall()
          for res in data1:
              
              d.append(res[0])
      
          return d
              
             
              
    def fill_engid():
           db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
           cur=db.cursor()
           d=[]
         
           s="select eng_id from engineer"
           cur.execute(s)
           data=cur.fetchall()
           for res in data:
               d.append(res[0])
           return d
    def fill_ser_name():
            db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
            cur=db.cursor()
            e=[]
            s="select service_id from service_master "
            cur.execute(s)
            data=cur.fetchall()
            for res in data:
                e.append(res[0])
            return e
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e9.get())
        if len(x)==0:
              messagebox.showinfo("Charge","Service Id entry is empty.\n Please fill it first.")
        else:
            s="select spare_cost,service_charge,total_charge from service_master where service_id='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
                
            e10.delete(0,100)
            e11.delete(0,100)
            e12.delete(0,100)
            e10.insert(0,data[0])
            e11.insert(0,data[1])
            e12.insert(0,data[2])
            
            db.close()
    def invoice():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        b=e2.get()
        c=e9.get()
        d=e4.get()
        e=e8.get()
        
        q=[]
        custname="select cust_name from customer where custid='%s'"%(b)
        cur.execute(custname)
        data_name=cur.fetchall()
        for res in data_name:
            q.append(res[0])
            
        r=[]
        pid="select pid from service_master where service_id='%s'"%(c)
        cur.execute(pid)
        data_pid=cur.fetchall()
        for res in data_pid:
            r.append(res[0])
            
        u=[]
        model="select model from product where pid='%s'"%(d)
        cur.execute(model)
        data_model=cur.fetchall()
        for res in data_model:
            u.append(res[0])
        
        n=[]
        sername="select service_name from service_master where service_id='%s'"%(c)
        cur.execute(sername)
        data=cur.fetchall()
        for res in data:
            n.append(res[0])
       
        
        b1=datetime.now()
        s1=b1.strftime("%H:%M:%S:%p")
       
        spare=str(e10.get())
        service=str(e11.get())
        total=str(e12.get())

        f=open(callrefno+'.txt','w')
        
        f.write('Customer id: '+ b +'\n')
        f.write('Name: '+ q[0] +'\n')
        f.write('Call Reference No.: '+ e +'\n')
        f.write('Product Id: '+ r[0] +'\t\t\t'+'Product Name:'+ u[0] )
        f.write('Date: '+ s1 +'\n')
        f.write('\n=====================================================================================\n')

        f.write('Spare Name' +'\t\t\t\t\t\t' + 'AMOUNT' +'\t\t\t\t\t\t'+'\n')
        f.write(n[0] +'\t\t\t\t\t' + spare +'\t\t\t\t\t\t'+'\n')
        f.write('Service Charge' +'\t\t\t\t\t\t' + service +'\t\t\t\t\t\t'+'\n')


        f.write('\n_____________________________________________________________________________________\n')
        f.write('\n\nTOTAL: '+ total +'\n')
        f.write('\n=====================================================================================\n')
        f.write('\n\t\t\t Have a nice day.\n')

        
        f.close()
        print(f)
        z=[]
        s="select email from customer where custid='%s'"%(b)
        cur.execute(s)
        data_mail=cur.fetchall()
        for res in data_mail:
            z.append(res[0])
        


        #set sender email and password
        sender="deemis007@outlook.com"
        password='deemis@007'
        #set receivers
        receivers =z[0]
        #set attachment file
        file_name = callrefno+'.txt'
        
        #set outlook smtp server host and port
        server_host = 'SMTP-mail.outlook.com'
        server_port = 587
        #create email text content
        #create MIMEMultipart object
        main_msg = email.mime.multipart.MIMEMultipart()
        #create a MIMEText object, it is the text content of email
        text_msg = email.mime.text.MIMEText("Hello "+q[0]+" Your Service Invoice")
        #add MIMEText object to MIMEMultipart object
        main_msg.attach(text_msg)
        #create MIMEBase object
        contype = 'application/octet-stream'
        maintype, subtype = contype.split('/', 1)
        #read attachment content
        data=open(file_name,'rb')
        file_msg = email.mime.base.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read( ))
        data.close( )
        #file_msg is content of attachment
        email.encoders.encode_base64(file_msg)
        #attachment header
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition',
                            'attachment', filename = basename)
        #add attachment to MIMEMultipart object
        main_msg.attach(file_msg)
        #set email format
        main_msg['From'] = sender
        main_msg['To'] = receivers
        main_msg['Subject'] = "Hello "+q[0]+". Your Service Invoice"
        main_msg['Date'] = email.utils.formatdate( )
        #full content of email
        fullText = main_msg.as_string()
        #send email by outlook smtp
        server = smtplib.SMTP(server_host, server_port)

        server.ehlo()
        server.starttls()
        server.ehlo()    
        server.login(sender,password)

        server.sendmail(sender, receivers, fullText)
        messagebox.showinfo("Send Invoice","Successfully save and sent Invoice")
        print ("")

        server.quit() 
        db.close()
    def new():
        from customer_data_form import cust_insert
        cust_insert()
    
    def bck():
        t.destroy()
       
      # insert form       
    #call ref no
    z=datetime.now()
    callrefno=str(z.strftime("%Y%m%d%H%M%S%f"))
    call_ref=StringVar(t,value=callrefno)
    
    # date
    a=date.today()
    am=a.strftime("%d/%m/%Y")
    call_date=StringVar(t,value=am)
    b=a+timedelta(days=3)
    bm=b.strftime("%d/%m/%Y")
    end_date=StringVar(t,value=bm)
    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Insert Call Assign',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Staff Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20)
    e1.place(x=350,y=150)
    staff_data=fill_staffid()
    e1['values']=staff_data
    
    l2=Label(t,text='Customer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=ttk.Combobox(t,width=20)
    e2.place(x=350,y=190)
    cust_data=fill_custid()
    e2['values']=cust_data
    
    l3=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=ttk.Combobox(t,width=20)
    e3.place(x=350,y=230)
    pcat_data=fill_pcatid()
    e3['values']=pcat_data

    l4=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)  
    e4=ttk.Combobox(t,width=20)
    e4.place(x=350,y=270)
    pid_data=fill_pid()
    e4['values']=pid_data
   
    
    l5=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)
    e5=ttk.Combobox(t,width=20)
    e5.place(x=350,y=310)
    eng_data=fill_engid()
    e5['values']=eng_data
    l6=Label(t,text='Date of Call', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,textvariable=call_date,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
    l7=Label(t,text='End Date', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=390)
    e7=Entry(t,textvariable=end_date,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e7.place(x=350,y=390)
    l8=Label(t,text='Call Reference No.', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l8.place(x=100,y=430)
    
    e8=Entry(t,textvariable=call_ref,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e8.place(x=350,y=430)
    l9=Label(t,text='Service Name', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l9.place(x=100,y=470)
    e9=ttk.Combobox(t,width=20)
    e9.place(x=350,y=470)
    service_data=fill_ser_name()
    e9['values']=service_data
    btn=Button(t,text="Charge", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn.place(x=500,y=470)
    
    
    l10=Label(t,text='Spare Cost', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l10.place(x=100,y=510)
    e10=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e10.place(x=350,y=510)
    l11=Label(t,text='Service Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l11.place(x=100,y=550)
    e11=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e11.place(x=350,y=550)
    l12=Label(t,text='Total Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l12.place(x=100,y=590)
    e12=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e12.place(x=350,y=590)
    
    
    
    
    btn1=Button(t,text="Save", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=insert)
    btn1.place(x=150,y=650)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=250,y=650)
    
    btn3=Button(t,text="Send Invoice", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=invoice)
    btn3.place(x=400,y=650)
    
    btn4=Button(t,text="New Customer", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=new)
    btn4.place(x=600,y=650)
    
    

    t.mainloop()

#DELETE
def callAssign_delete():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Delete')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_delete.ico")
    
    def de():
       
       db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
       cur=db.cursor()
       x=str(e1.get())
       
       if len(x)==0:
             messagebox.showinfo("Delete","Some entry is empty check it")
       else:
          
           q=[]
           z="select call_ref_no from call_Assign "
           cur.execute(z)
           data=cur.fetchall()
           for res in data:
               q.append(res[0])
           if x in q:
               s="delete from  where  call_ref_no=%s"%(x)
               cur.execute(s)
               db.commit()
               messagebox.showinfo("Delete","Data Deleted")
               e1.delete(0,100)
               db.close()
           else:
               messagebox.showinfo("Delete","Call Reference No is not in Database.\n Please check again")
                
    def bck():
        t.destroy()
       
     # delete

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Delete Call Assign',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Call Reference No ', fg='black',bg='light blue', font=('Arial Rounded MT Bold',16))
    l1.place(x=100,y=150)
    e1=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',15))
    e1.place(x=350,y=150)
    
    btn1=Button(t,text="Delete", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=de)
    btn1.place(x=250,y=250)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',15),activeforeground="red",command=bck)
    btn2.place(x=450,y=250)

    t.mainloop()


# UPDATE
def callAssign_update():
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
        g=str(e7.get())
        h=str(e8.get())
        i=str(e9.get())
        j=int(e10.get())
        k=int(e11.get())
        l=int(e12.get())
        
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0:
              messagebox.showinfo("Save","Some entry is empty check it")
        else:
       
            s="update call_assign set staffid='%s',custid='%s',pcatid='%s',pid='%s',eng_id='%s',date_of_call='%s',end_date='%s',service_id='%s',spare_cost='%s',service_charge='%s',total_charge='%s' where call_ref_no='%s'"%(b,c,d,e,f,g,h,i,j,k,l,a)
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
            e9.delete(0,100)
            e10.delete(0,100)
            e11.delete(0,100)
            e12.delete(0,100)
           
            messagebox.showinfo("Update","Update done")
            db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        
        s="select staffid,custid,pcatid,pid,eng_id,date_of_call,end_date,service_id,spare_cost,service_charge,total_charge from call_assign where call_ref_no='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        
        
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        e9.delete(0,100)
        e10.delete(0,100)
        e11.delete(0,100)
        e12.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])   
        e7.insert(0,data[5])
        e8.insert(0,data[6])
        e9.insert(0,data[7])
        e10.insert(0,data[8])
        e11.insert(0,data[9])
        e12.insert(0,data[10])
        
        db.close()
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=[]
        s="select call_ref_no from call_assign" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def fill_staffid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          a=[]
          s="select staffid from call_attendent_staff"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              a.append(res[0])
          return a
    def fill_custid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          cust=[]
          s="select custid from customer"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              cust.append(res[0])
          return cust
    def fill_pcatid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
          b=[]
          s="select pcatid from product_category"
          cur.execute(s)
          data=cur.fetchall()
          for res in data:
              b.append(res[0])
          return b
    def fill_pid():
          db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
          cur=db.cursor()
        
         
          d=[]   
          pid="select pid from product"
          cur.execute(pid)
          data1=cur.fetchall()
          for res in data1:
              
              d.append(res[0])
      
          return d
              
             
              
    def fill_engid():
           db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
           cur=db.cursor()
           d=[]
         
           s="select eng_id from engineer"
           cur.execute(s)
           data=cur.fetchall()
           for res in data:
               d.append(res[0])
           return d
    def fill_ser_name():
            db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
            cur=db.cursor()
            e=[]
            s="select service_id from service_master "
            cur.execute(s)
            data=cur.fetchall()
            for res in data:
                e.append(res[0])
            return e
    def find_charge():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e9.get())
        if len(x)==0:
              messagebox.showinfo("Charge","Service Id entry is empty.\n Please fill it first.")
        else:
            s="select spare_cost,service_charge,total_charge from service_master where service_id='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
                
            e10.delete(0,100)
            e11.delete(0,100)
            e12.delete(0,100)
            e10.insert(0,data[0])
            e11.insert(0,data[1])
            e12.insert(0,data[2])
            
            db.close()
    def invoice():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        
        b=e3.get()
        c=e9.get()
        d=e5.get()
        e=e1.get()
        
        q=[]
        custname="select cust_name from customer where custid='%s'"%(b)
        cur.execute(custname)
        data_name=cur.fetchall()
        for res in data_name:
            q.append(res[0])
            
        r=[]
        pid="select pid from service_master where service_id='%s'"%(c)
        cur.execute(pid)
        data_pid=cur.fetchall()
        for res in data_pid:
            r.append(res[0])
            
        u=[]
        model="select model from product where pid='%s'"%(d)
        cur.execute(model)
        data_model=cur.fetchall()
        for res in data_model:
            u.append(res[0])
        
        n=[]
        sername="select service_name from service_master where service_id='%s'"%(c)
        cur.execute(sername)
        data=cur.fetchall()
        for res in data:
            n.append(res[0])
       
        
        b1=datetime.now()
        s1=b1.strftime("%H:%M:%S:%p")
       
        spare=str(e10.get())
        service=str(e11.get())
        total=str(e12.get())

        f=open(e1.get()+'update.txt','w')
        
        f.write('Customer id: '+ b +'\n')
        f.write('Name: '+ q[0] +'\n')
        f.write('Call Reference No.: '+ e +'\n')
        f.write('Product Id: '+ r[0] +'\t\t\t'+'Product Name:'+ u[0] )
        f.write('Date: '+ s1 +'\n')
        f.write('\n=====================================================================================\n')

        f.write('Spare Name' +'\t\t\t\t\t\t' + 'AMOUNT' +'\t\t\t\t\t\t'+'\n')
        f.write(n[0] +'\t\t\t\t\t' + spare +'\t\t\t\t\t\t'+'\n')
        f.write('Service Charge' +'\t\t\t\t\t\t' + service +'\t\t\t\t\t\t'+'\n')


        f.write('\n_____________________________________________________________________________________\n')
        f.write('\n\nTOTAL: '+ total +'\n')
        f.write('\n=====================================================================================\n')
        f.write('\n\t\t\t Have a nice day.\n')

        
        f.close()
        print(f)
        z=[]
        s="select email from customer where custid='%s'"%(b)
        cur.execute(s)
        data_mail=cur.fetchall()
        for res in data_mail:
            z.append(res[0])
        


        #set sender email and password
        sender="deemis007@outlook.com"
        password='deemis@007'
        #set receivers
        receivers =z[0]
        #set attachment file
        file_name = e1.get()+'update.txt'
        
        #set outlook smtp server host and port
        server_host = 'SMTP-mail.outlook.com'
        server_port = 587
        #create email text content
        #create MIMEMultipart object
        main_msg = email.mime.multipart.MIMEMultipart()
        #create a MIMEText object, it is the text content of email
        text_msg = email.mime.text.MIMEText("Hello "+q[0]+" Your Service Invoice")
        #add MIMEText object to MIMEMultipart object
        main_msg.attach(text_msg)
        #create MIMEBase object
        contype = 'application/octet-stream'
        maintype, subtype = contype.split('/', 1)
        #read attachment content
        data=open(file_name,'rb')
        file_msg = email.mime.base.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read( ))
        data.close( )
        #file_msg is content of attachment
        email.encoders.encode_base64(file_msg)
        #attachment header
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition',
                            'attachment', filename = basename)
        #add attachment to MIMEMultipart object
        main_msg.attach(file_msg)
        #set email format
        main_msg['From'] = sender
        main_msg['To'] = receivers
        main_msg['Subject'] = "Hello "+q[0]+". Your Service Invoice"
        main_msg['Date'] = email.utils.formatdate( )
        #full content of email
        fullText = main_msg.as_string()
        #send email by outlook smtp
        server = smtplib.SMTP(server_host, server_port)

        server.ehlo()
        server.starttls()
        server.ehlo()    
        server.login(sender,password)

        server.sendmail(sender, receivers, fullText)
        messagebox.showinfo("Send Invoice","Successfully save and sent Invoice")
        print ("")

        server.quit() 
        db.close()
    
    def bck():
        t.destroy()
       
      # Update

    # date
    a=date.today()
    am=a.strftime("%d/%m/%Y")
    call_date=StringVar(t,value=am)
    b=a+timedelta(days=3)
    bm=b.strftime("%d/%m/%Y")
    end_date=StringVar(t,value=bm)
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='Update Call Assign',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Call Reference No.', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    
    e1=ttk.Combobox(t,width=40)
    e1.place(x=350,y=150)
    data=filldata()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=650,y=150)
    l2=Label(t,text='Staff Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l2.place(x=100,y=190)
    e2=ttk.Combobox(t,width=20)
    e2.place(x=350,y=190)
    staff_data=fill_staffid()
    e2['values']=staff_data
    
    l3=Label(t,text='Customer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l3.place(x=100,y=230)
    e3=ttk.Combobox(t,width=20)
    e3.place(x=350,y=230)
    cust_data=fill_custid()
    e3['values']=cust_data
    
    l4=Label(t,text='Product Category Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l4.place(x=100,y=270)
    e4=ttk.Combobox(t,width=20)
    e4.place(x=350,y=270)
    pcat_data=fill_pcatid()
    e4['values']=pcat_data

    l5=Label(t,text='Product Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l5.place(x=100,y=310)  
    e5=ttk.Combobox(t,width=20)
    e5.place(x=350,y=310)
    pid_data=fill_pid()
    e5['values']=pid_data
   
    
    l6=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=ttk.Combobox(t,width=20)
    e6.place(x=350,y=350)
    eng_data=fill_engid()
    e6['values']=eng_data
    l7=Label(t,text='Date of Call', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=390)
    e7=Entry(t,textvariable=call_date,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e7.place(x=350,y=390)
    l8=Label(t,text='End Date', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l8.place(x=100,y=430)
    e8=Entry(t,textvariable=end_date,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e8.place(x=350,y=430)
    
    
    l9=Label(t,text='Service Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l9.place(x=100,y=470)
    e9=ttk.Combobox(t,width=20)
    e9.place(x=350,y=470)
    service_data=fill_ser_name()
    e9['values']=service_data
    btn=Button(t,text="Charge", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=find_charge)
    btn.place(x=500,y=470)
    l10=Label(t,text='Spare Cost', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l10.place(x=100,y=510)
    e10=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e10.place(x=350,y=510)
    l11=Label(t,text='Service Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l11.place(x=100,y=550)
    e11=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e11.place(x=350,y=550)
    l12=Label(t,text='Total Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l12.place(x=100,y=590)
    e12=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e12.place(x=350,y=590)
    
    
        
    btn1=Button(t,text="Update", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=updatedata)
    btn1.place(x=100,y=650)
    
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=300,y=650)
    
    btn3=Button(t,text="Send Invoice", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=invoice)
    btn3.place(x=500,y=650)

    t.mainloop()

# FIND
def callAssign_find():
    t=tkinter.Tk()
    t.geometry("800x800")
    t.title('Find')
    t.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_find.ico")
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        x=str(e1.get())
        
        s="select staffid,custid,pcatid,pid,eng_id,date_of_call,end_date,Service_id,spare_cost,service_charge,total_charge from call_assign where call_ref_no='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        
        
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        e9.delete(0,100)
        e10.delete(0,100)
        e11.delete(0,100)
        e12.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])   
        e7.insert(0,data[5])
        e8.insert(0,data[6])
        e9.insert(0,data[7])
        e10.insert(0,data[8])
        e11.insert(0,data[9])
        e12.insert(0,data[10])
        
        db.close()
    def filldata():
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
       
# find

    
    c=Canvas(t,width=800,height=800,bg='light blue')
    c.place(x=0, y=0)
    c=Canvas(t,width=500,height=40,bg='grey20')
    c.place(x=150, y=30)
    c.create_text(250,20,text='find Call Assign',font=('Copperplate Gothic Bold',20),fill='yellow green')
    l1=Label(t,text='Call Reference No', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l1.place(x=100,y=150)
    e1=ttk.Combobox(t,width=40)
    e1.place(x=350,y=150)
    data=filldata()
    e1['values']=data
    btn1=Button(t,text="Find", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
    btn1.place(x=650,y=150)
  
    l2=Label(t,text='Staff Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
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
    l6=Label(t,text='Engineer Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l6.place(x=100,y=350)
    e6=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e6.place(x=350,y=350)
    l7=Label(t,text='Date Of Call', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l7.place(x=100,y=390)
    e7=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e7.place(x=350,y=390)
    l8=Label(t,text='End Date', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l8.place(x=100,y=430)
    e8=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e8.place(x=350,y=430)
    
    l9=Label(t,text='Service Id', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l9.place(x=100,y=470)
    e9=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e9.place(x=350,y=470)
    
    l10=Label(t,text='Spare Cost', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l10.place(x=100,y=510)
    e10=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e10.place(x=350,y=510)
    l11=Label(t,text='Service Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l11.place(x=100,y=550)
    e11=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e11.place(x=350,y=550)
    l12=Label(t,text='Total Charge', fg='black',bg='light blue', font=('Arial Rounded MT Bold',15))
    l12.place(x=100,y=590)
    e12=Entry(t,width=30,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e12.place(x=350,y=590)
   
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',16),activeforeground="red",command=bck)
    btn2.place(x=300,y=630)

    t.mainloop()

callAssign_insert()