# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 04:08:49 2022

@author: DM
"""
def dash():
    import pymysql
    import tkinter
    from tkinter import Label,Frame,Canvas,Button
    
    from eng_data_form import eng_update
    from feedback import find_feedback
    from tkinter import ttk,Scrollbar,messagebox
   

    
    t=tkinter.Tk()
    t.geometry("1600x750")

    t.title('Engineer')
    def update():
        eng_update()
    def logout():
        messagebox.showinfo("Logout","Click OK to Logout Successfully.")
        t.destroy()
    
    top_frame = Frame(t, width=1600, height=80)
    top_frame.pack(side='top', fill='both', padx=10, pady=5, expand=True)
     
    bottom_frame = Frame(t, width=1000, height=700,bg='royalblue4')
    bottom_frame.pack(side='bottom', fill='both', padx=10, pady=5, expand=True)
     
   
    
    # top frame
    c=Canvas(top_frame,width=1500,height=150,bg="royalblue4")
    c.pack(side='top', padx=1, pady=1)
    
    
    email="E051"
    db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
    cur=db.cursor()
    
    w=[]
    s="select eng_name from engineer where eng_id='%s'" %(email)
    cur.execute(s)
    data=cur.fetchone()
    for res in data:
        w.append(res[0])
        
    x=[]
    s="select eng_name from engineer where eng_id='%s'" %(email)
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
        x.append(res[0])
        
    y=[]
    s="select email from engineer where eng_id='%s'" %(email)
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
        y.append(res[0])
        
    z=[]
    s="select phone from engineer where eng_id='%s'" %(email)
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
        z.append(res[0])
        
    c1=Canvas(c,width=80,height=80,bg='royalblue4')
    c1.place(x=10,y=10)
    c1.create_text(40,40,text=w,font=('Arial Rounded MT Bold',50,'bold'),fill='white',)
    
    l1=Label(c,text='Engineer Id:', fg='red',bg='royalblue4', font=('Arial Rounded MT Bold',18,'bold'))
    l1.place(x=100,y=4)
    l2=Label(c,text=email, fg='white',bg='royalblue4', font=('Arial Rounded MT Bold',18,'bold'))
    l2.place(x=320,y=4)
    
    l3=Label(c,text='Engineer Name:', fg='red',bg='royalblue4', font=('Arial Rounded MT Bold',18,'bold'))
    l3.place(x=100,y=50)
    l4=Label(c,text=x[0], fg='white',bg='royalblue4', font=('Arial Rounded MT Bold',18,'bold'))
    l4.place(x=320,y=50)
    
    l5=Label(c,text=y[0], fg='white',bg='royalblue4', font=('Arial Rounded MT Bold',15,'bold'))
    l5.place(x=1000,y=4)
    l6=Label(c,text="+91"+z[0], fg='white',bg='royalblue4', font=('Arial Rounded MT Bold',14,'bold'))
    l6.place(x=1000,y=31)
    
    btn1=Button(c,text="Update", fg="green4",bg="white",font=('Arial Rounded MT Bold',12),activeforeground="red",command=update)
    btn1.place(x=1000,y=80)
    btn2=Button(c,text="Logout", fg="green4",bg="white",font=('Arial Rounded MT Bold',12),activeforeground="red",command=logout)
    btn2.place(x=1200,y=80)
    
    # bottom frame
    c3=Canvas(bottom_frame,width=1000,height=750,bg="royalblue1")
    c3.pack(side='left', padx=10, pady=10)
    c4=Canvas(c3,width=300,height=50,bg="white")
    c4.pack(anchor='center',padx=10,pady=10)
    c4.create_text(150,25,text="Work Status", font=('Arial Rounded MT Bold',20,'bold'),fill='tomato1')
    btn3=Button(c3,text="Check Customer Feedback", fg="green4",bg="white",font=('Arial Rounded MT Bold',12),activeforeground="red",command=find_feedback)
    btn3.pack(padx=30,pady=30)
    btn3.place(x=1050,y=10)
    c5=Label(c3,width=600,height=700,bg="royalblue4")
    c5.pack(anchor='center',padx=10,pady=100)
    mytree=ttk.Treeview(c5,height=700)
    
    #add style
    style=ttk.Style()
    # pick a theme
    style.theme_use('default')
    
    # pick a theme
    style.configure("Treeview",background="#D3D3D3",foreground="black",
                    rowheight=25,fieldbackground="D3D3D3",font=('arial',10,'bold'))
    style.configure("Treeview.Heading",background="royalblue4",foreground="white",
                    rowheight=25,fieldbackground="red",font=('arial',10,'bold'))
    #change selected color
    style.map('Treeview',background=[('selected',"#347083")])
    #treeview frame
    treeframe=Frame(c5,width=600,height=500)
    treeframe.pack()
    
    #treeview horizontal scrollbar
    treescrolly=Scrollbar(treeframe)
    treescrolly.pack(side='right',fill='y')
    
    #treeview vertical scrollbar
    treescrollx=Scrollbar(treeframe,orient='horizontal')    
    treescrollx.pack(side='bottom',fill='x')
    # create treeview
    mytree=ttk.Treeview(treeframe,yscrollcommand=treescrolly.set,selectmode="extended")
    mytree=ttk.Treeview(treeframe,xscrollcommand=treescrollx.set,selectmode="extended")
    mytree.pack()
    
    # configure scrollbar
    treescrolly.config(command=mytree.yview)
    treescrollx.config(command=mytree.xview)
    
    #define column
    mytree['columns']=("Call Ref No","Cust ID","Product ID","Service ID","CallDate",
                       "End Date","Product Name","Service Name","Cust Name","Cust Add.",
                       "Cust Phone","Total Cost")
    #fformate column
    mytree.column("#0",width=120, stretch='no')
    mytree.column("Call Ref No",width=120, anchor='c')
    mytree.column("Cust ID",width=120, anchor='c')
    mytree.column("Product ID",width=120, anchor='c')
    mytree.column("Service ID",width=120, anchor='c')
    mytree.column("CallDate",width=120, anchor='c')
    mytree.column("End Date",width=120, anchor='c')
    mytree.column("Product Name",width=120, anchor='c')
    mytree.column("Service Name",width=120, anchor='c')
    mytree.column("Cust Name",width=120, anchor='c')
    mytree.column("Cust Add.",width=120, anchor='c')
    mytree.column("Cust Phone",width=120, anchor='c')
    mytree.column("Total Cost",width=120, anchor='c')
    
    # heading
    mytree.heading("#0",text='Serial No.', anchor='c')
    mytree.heading("Call Ref No",text='Call Ref No', anchor='c')
    mytree.heading("Cust ID",text='Cust ID', anchor='c')
    mytree.heading("Product ID",text='Product ID', anchor='c')
    mytree.heading("Service ID",text='Service ID', anchor='c')
    mytree.heading("CallDate",text='CallDate', anchor='c')
    mytree.heading("End Date",text='End Date', anchor='c')
    mytree.heading("Product Name",text='Product Name', anchor='c')
    mytree.heading("Service Name",text='Service Name', anchor='c')
    mytree.heading("Cust Name",text='Cust Name', anchor='c')
    mytree.heading("Cust Add.",text='Cust Add.', anchor='c')
    mytree.heading("Cust Phone",text='Cust Phone', anchor='c')
    mytree.heading("Total Cost",text='Total Cost', anchor='c')
    
   
   # data
    
    db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
    cur=db.cursor()
    tabledata=[]
    s="select call_ref_no,custid,pid,service_id,date_of_call,end_date from call_Assign where eng_id='%s'"%(email)
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
       tabledata.append(res[0])
       tabledata.append(res[1])
       tabledata.append(res[2])
       tabledata.append(res[3])
       tabledata.append(res[4])
       tabledata.append(res[5])
       
       s1="select model from product where pid='%s'"%(tabledata[2])
       cur.execute(s1)
       data2=cur.fetchall()
       for res in data2:
          tabledata.append(res[0])
          
       servicedetail="select service_name from service_master where service_id='%s'"%(tabledata[3])
       cur.execute(servicedetail)
       data1=cur.fetchall()
       for res in data1:
           tabledata.append(res[0])
           
       customerdetail="select cust_name,address,phone from customer where custid='%s'"%(tabledata[1])
       cur.execute(customerdetail)
       data=cur.fetchall()
       for res in data:
          tabledata.append(res[0])
          tabledata.append(res[1])
          tabledata.append(res[2])
    

       chargedetail="select total_charge from call_Assign where call_ref_no='%s'"%(tabledata[0])
       cur.execute(chargedetail)
       data=cur.fetchall()
       for res in data:
          tabledata.append(res[0])
          
          
    totalrow=[]
    s="select count(*) from call_Assign where eng_id='%s'" %(email)
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
         totalrow.append(res[0])
    for res in range(totalrow[0]):
        data_row=[tabledata]
        print(data_row)
    
   
    
    
    # create striped row tags
    mytree.tag_configure('oddrow',background="white")
    mytree.tag_configure('evenrow',background="lightblue")
    #add data
    global count
    count=0
    for ra in data_row:
        if count%2==0:
            mytree.insert(parent='',index='end',iid=count,text=count+1,values=(ra[0],ra[1],ra[2],ra[3],ra[4],ra[5],ra[6],ra[7],ra[8],ra[9],ra[10],ra[11]),tags=('evenrow',))
            mytree.pack(pady=20)
            count+=1
        else:
            mytree.insert(parent='',index='end',iid=count,text=count+1,values=(ra[0],ra[1],ra[2],ra[3],ra[4],ra[5],ra[6],ra[7],ra[8],ra[9],ra[10],ra[11]),tags=('oddrow',))
            mytree.pack(pady=20)
            count+=1
                  

   
    totalcall=[]
    s="select count(*) from call_Assign where eng_id='%s'" %(email)
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
         totalcall.append(res[0])
    l5=Label(c3,text="Total Calls:", fg='white',bg='royalblue1', font=('Arial Rounded MT Bold',15,'bold'))
    l5.place(x=50,y=100)
    l6=Label(c3,text=totalcall[0], fg='white',bg='royalblue1', font=('Arial Rounded MT Bold',15,'bold'))
    l6.place(x=200,y=100)
    
    callsolve=[]
    s="select count(*) from call_Solved where eng_id='%s'" %(email)
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
         callsolve.append(res[0])
    l7=Label(c3,text="Solved Calls:", fg='white',bg='royalblue1', font=('Arial Rounded MT Bold',15,'bold'))
    l7.place(x=500,y=100)
    l8=Label(c3,text=callsolve[0], fg='white',bg='royalblue1', font=('Arial Rounded MT Bold',15,'bold'))
    l8.place(x=700,y=100)
    
    db.close()
    
    t.mainloop()
dash()