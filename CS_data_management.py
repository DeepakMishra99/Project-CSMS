# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:43:51 2022

@author: DM
"""
def dm():
    
    import tkinter
    
    from tkinter import Canvas,Button,Label
    from pc_data_form import pc_insert,pc_delete,pc_update,pc_find
    from pro_data_form import pro_insert,pro_delete,pro_update,pro_find
    from sm_data_form import sm_insert,sm_delete,sm_update,sm_find
    from eng_data_form import eng_insert,eng_delete,eng_update,eng_find
    from cas_data_form import cas_insert,cas_delete,cas_update,cas_find
    from customer_data_form import cust_insert,cust_delete,cust_update,cust_find
    from call_assign_data_form import callAssign_insert,callAssign_delete,callAssign_update,callAssign_find
    from call_solved_data_form import callSolved_insert,callSolved_delete,callSolved_update,callSolved_find
    
    tk=tkinter.Tk()
    tk.geometry("1000x700")
    tk.title("Customer Service Management")
    tk.iconbitmap("E:\our_project\customer_service_mang_code\Data Management\images\icon_data.ico")
    
     # Canvas for background
    c=Canvas(tk,width=1000,height=700,bg='steelblue4')
    c.place(x=0, y=0)
   
     
     
    # Canvas for Labels
    c2=Canvas(tk,width=1000,height=50,bg='Grey40')
    c2.place(x=0, y=0)
    c2.create_text(500,30,text="Customer Service Data Management",font=('Copperplate Gothic Bold',20,'bold'),fill="steelblue1")
     
    # Canvas for Labels
    c2=Canvas(tk,width=350,height=650,bg='black')
    c2.place(x=0, y=53)
     
     
    # [Product Category]
    label_pro_cat=Label(tk,text='PRODUCT CATEGORY',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_pro_cat.place(x=40,y=80)
     

                #Insert
    btn1=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pc_insert)
    btn1.place(x=400,y=80)
     
     
                 #Delete
    btn2=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pc_delete)
    btn2.place(x=500,y=80)
     
                 #Update
    btn3=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pc_update)
    btn3.place(x=600,y=80)
     
                #Find
    btn4=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pc_find)
    btn4.place(x=700,y=80)
     
     # [Product]
    label_product=Label(tk,text='PRODUCT',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_product.place(x=40,y=120)
    
                 #Insert
    btn5=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pro_insert)
    btn5.place(x=400,y=120)
     
                 #Delete
    btn6=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pro_delete)
    btn6.place(x=500,y=120)
     
                 #Update
    btn7=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pro_update)
    btn7.place(x=600,y=120)
     
                #Find
    btn8=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=pro_find)
    btn8.place(x=700,y=120)
     
     # [Service Master]
    label_service_master=Label(tk,text='SERVICE MASTER',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_service_master.place(x=40,y=160)
     
    
                 #Insert
    btn9=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=sm_insert)
    btn9.place(x=400,y=160)
     
                 #Delete
    btn10=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=sm_delete)
    btn10.place(x=500,y=160)
     
                 #Update
    btn11=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=sm_update)
    btn11.place(x=600,y=160)
     
                #Find
    btn12=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=sm_find)
    btn12.place(x=700,y=160)
     
    # [Engineer]
    label_engineer=Label(tk,text='ENGINEER',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_engineer.place(x=40,y=200)
     
    
                 #Insert
    btn13=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=eng_insert)
    btn13.place(x=400,y=200)
     
                 #Delete
    btn14=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=eng_delete)
    btn14.place(x=500,y=200)
     
                 #Update
    btn15=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=eng_update)
    btn15.place(x=600,y=200)
     
                #Find
    btn16=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=eng_find)
    btn16.place(x=700,y=200)
     
     # [Call Attendent Staff]
    label_call_att=Label(tk,text='Call Attendent Staff',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_call_att.place(x=40,y=240)
     
   
                 #Insert
    btn17=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cas_insert)
    btn17.place(x=400,y=240)
     
                 #Delete
    btn18=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cas_delete)
    btn18.place(x=500,y=240)
     
                 #Update
    btn19=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cas_update)
    btn19.place(x=600,y=240)
     
                #Find
    btn20=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cas_find)
    btn20.place(x=700,y=240)
     
     # [Customer]
    label_customer=Label(tk,text='CUSTOMER',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_customer.place(x=40,y=280)
     
   
                 #Insert
    btn21=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cust_insert)
    btn21.place(x=400,y=280)
     
                 #Delete
    btn22=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cust_delete)
    btn22.place(x=500,y=280)
     
                 #Update
    btn23=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cust_update)
    btn23.place(x=600,y=280)
     
                #Find
    btn24=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=cust_find)
    btn24.place(x=700,y=280)
     
     # [Call Assign]
    label_call_assign=Label(tk,text='CALL ASSIGN',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_call_assign.place(x=40,y=320)
     
   
                #Insert
    btn25=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callAssign_insert)
    btn25.place(x=400,y=320)
     
                 #Delete
    btn26=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callAssign_delete)
    btn26.place(x=500,y=320)
     
                 #Update
    btn27=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callAssign_update)
    btn27.place(x=600,y=320)
     
                #Find
    btn28=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callAssign_find)
    btn28.place(x=700,y=320)
     
     # [Call Solved]
    label_call_solved=Label(tk,text='CALL SOLVED',font=('Copperplate Gothic Bold',15),fg="white",bg='black')
    label_call_solved.place(x=40,y=360)
     
   
                 #Insert
    btn29=Button(tk,text="Insert", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callSolved_insert)
    btn29.place(x=400,y=360)
     
                 #Delete
    btn30=Button(tk,text="Delete", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callSolved_delete)
    btn30.place(x=500,y=360)
     
                 #Update
    btn31=Button(tk,text="Update", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callSolved_update)
    btn31.place(x=600,y=360)
     
                #Find
    btn32=Button(tk,text="Find", fg="yellow green",bg="azure4",font=('Arial Rounded MT Bold',12),activeforeground="red",command=callSolved_find)
    btn32.place(x=700,y=360)
     
     
    tk.mainloop()

   
dm()

    
