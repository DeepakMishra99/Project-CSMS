# -*- coding: utf-8 -*-
"""
Created on Sat May 28 03:46:45 2022

@author: DM
"""
import pymysql
import tkinter 
from tkinter import Label,Canvas,Spinbox,Radiobutton,IntVar,Entry,Button,messagebox
def ins_feedback():
    t=tkinter.Tk()
    t.geometry("900x800")
    t.title(" Feedback page ")
    
    def insert():
    
        db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
        cur=db.cursor()
        a=str(e1.get())
        b=str(s1.get())
        c=str(x.get())
        d=str(y.get())
        e=str(z.get())
        f=str(p.get())
        g=str(q.get())
        h=str(r.get())
        if len(a)==0 or len(b)==0:
              messagebox.showinfo("Save Feedback","Call Refetrence No. and overall is compulsary")
        else:
            
        
            s="insert into feedback values('%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g,h)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Save","Data saved")
            e1.delete(0,100)
            s1.delete(0,100)
            x.delete(0,100)
            y.delete(0,100)
            z.delete(0,100)
            p.delete(0,100)
            q.delete(0,100)
            r.delete(0,100)
            db.close()
    def bck():
        t.destroy()
    
    
    c1=Canvas(t,width=900,height=800,bg='LightPink3')
    c1.place(x=0, y=0)
    l1=Label(c1,text=" Customer Satisfaction Survey  ",font=('Copperplate Gothic Bold',25,'bold'),bg='#Ffbe00')
    l1.place(x=160,y=10)
    l2=Label(c1,text=" Call Reference No. : ",font=('Arial',15,'bold'),bg='LightPink3')
    l2.place(x=50,y=80)
    e1=Entry(t,width=40,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
    e1.place(x=300,y=80)
   
    l3=Label(t,text=" GIVE US YOUR FEEDBACK ",font=('Stylus',15,'bold','underline'),bg='LightPink3')
    l3.place(x=10,y=150)
    l4=Label(t,text="Overall,how satisfied or dissatisfied are you with our company ?(Out of 10) ",font=('Arial',12,'bold'),fg='red4',bg='LightPink3')
    l4.place(x=10,y=190)
    s1=Spinbox(t,from_=0,to=10,width=80, font=('Arial Rounded MT Bold',10))
    s1.pack()
    s1.place(x=10,y=220,height=20) 
    
    l5=Label(t,text="Using the Scale below ,please rate your level of agreement with each of the following statements.",font=('Arial',12,'bold','underline'),bg='LightPink3')
    l5.place(x=10,y=240)
    
    
    l6=Label(t,text="Response to my query was prompt",font=('Arial',11,'bold'),bg='LightPink3')
    l6.place(x=10,y=310)
    
    l7=Label(t,text="Strongly disagree",font=('Arial',11,'bold'),bg='LightPink3')
    l7.place(x=300,y=280)
     
    
    l8=Label(t,text=" Disagree",font=('Arial',11,'bold'),bg='LightPink3')
    l8.place(x=450,y=280)
    
    
    l9=Label(t,text="Neutral",font=('Arial',11,'bold'),bg='LightPink3')
    l9.place(x=550,y=280)
    
    
    l10=Label(t,text="Agree",font=('Arial',11,'bold'),bg='LightPink3')
    l10.place(x=645,y=280)
    
    
    l11=Label(t,text="Strongly agree",font=('Arial',11,'bold'),bg='LightPink3')
    l11.place(x=725,y=280)
    
    x=IntVar()
    r1=Radiobutton(t,variable=x,value=0,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r2=Radiobutton(t,variable=x,value=1,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r3=Radiobutton(t,variable=x,value=2,bg='MediumPurple1',fg='red4',font=(10),width=8)
    r4=Radiobutton(t,variable=x,value=3,bg='MediumPurple4',fg='red4',font=(10),width=7)
    r5=Radiobutton(t,variable=x,value=4,bg='MediumPurple1',fg='red4',font=(10),width=10)
    
    r1.place(x=300,y=310)
    r2.place(x=420,y=310)
    r3.place(x=530,y=310)
    r4.place(x=630,y=310)
    r5.place(x=720,y=310)
    
    l12=Label(t,text="Work was done in the time estimated ",font=('Arial',11,'bold'),bg='LightPink3')
    l12.place(x=10,y=370)
    
    
    y=IntVar()
    r1=Radiobutton(t,variable=y,value=0,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r2=Radiobutton(t,variable=y,value=1,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r3=Radiobutton(t,variable=y,value=2,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r4=Radiobutton(t,variable=y,value=3,bg='MediumPurple1',fg='red4',font=(10),width=7)
    r5=Radiobutton(t,variable=y,value=4,bg='MediumPurple4',fg='red4',font=(10),width=10)
    
    r1.place(x=300,y=370)
    r2.place(x=420,y=370)
    r3.place(x=530,y=370)
    r4.place(x=630,y=370)
    r5.place(x=720,y=370)
    
    l13=Label(t,text='''Work was done in the reasonable
    amount of time ''',font=('Arial',11,'bold'),bg='LightPink3')
    l13.place(x=10,y=430)
    
    
    z=IntVar()
    r1=Radiobutton(t,variable=z,value=0,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r2=Radiobutton(t,variable=z,value=1,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r3=Radiobutton(t,variable=z,value=2,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r4=Radiobutton(t,variable=z,value=3,bg='MediumPurple4',fg='red4',font=(10),width=7)
    r5=Radiobutton(t,variable=z,value=4,bg='MediumPurple1',fg='red4',font=(10),width=10)
    
    r1.place(x=300,y=430)
    r2.place(x=420,y=430)
    r3.place(x=530,y=430)
    r4.place(x=630,y=430)
    r5.place(x=720,y=430)
    
    
    l13=Label(t,text="Staff were quick and effiecent ",font=('Arial',11,'bold'),bg='LightPink3')
    l13.place(x=10,y=500)
    
    
    p=IntVar()
    r1=Radiobutton(t,variable=p,value=0,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r2=Radiobutton(t,variable=p,value=1,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r3=Radiobutton(t,variable=p,value=2,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r4=Radiobutton(t,variable=p,value=3,bg='MediumPurple1',fg='red4',font=(10),width=7)
    r5=Radiobutton(t,variable=p,value=4,bg='MediumPurple4',fg='red4',font=(10),width=10)
    
    r1.place(x=300,y=500)
    r2.place(x=420,y=500)
    r3.place(x=530,y=500)
    r4.place(x=630,y=500)
    r5.place(x=720,y=500)
    
    
    l14=Label(t,text='''Staff were courteous and listened
    to me ''',font=('Arial',11,'bold'),bg='LightPink3')
    l14.place(x=10,y=570)
    
    
    q=IntVar()
    r1=Radiobutton(t,variable=q,value=0,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r2=Radiobutton(t,variable=q,value=1,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r3=Radiobutton(t,variable=q,value=2,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r4=Radiobutton(t,variable=q,value=3,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r5=Radiobutton(t,variable=q,value=4,bg='MediumPurple1',fg='red4',font=(10),width=10)
    
    r1.place(x=300,y=570)
    r2.place(x=420,y=570)
    r3.place(x=530,y=570)
    r4.place(x=630,y=570)
    r5.place(x=720,y=570)
    
    
    l15=Label(t,text="My home was treated respectfuly ",font=('Arial',11,'bold'),bg='LightPink3')
    l15.place(x=10,y=640)
    
    
    r=IntVar()
    r1=Radiobutton(t,variable=r,value=0,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r2=Radiobutton(t,variable=r,value=1,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r3=Radiobutton(t,variable=r,value=2,bg='MediumPurple4',fg='red4',font=(10),width=10)
    r4=Radiobutton(t,variable=r,value=3,bg='MediumPurple1',fg='red4',font=(10),width=10)
    r5=Radiobutton(t,variable=r,value=4,bg='MediumPurple4',fg='red4',font=(10),width=10)
    
    r1.place(x=300,y=640)
    r2.place(x=420,y=640)
    r3.place(x=530,y=640)
    r4.place(x=630,y=640)
    r5.place(x=720,y=640)
    
    btn1=Button(t,text="Save Feedback", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',12),activeforeground="red",command=insert)
    btn1.place(x=200,y=700)
    btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',12),activeforeground="red",command=bck)
    btn2.place(x=600,y=700)
    t.mainloop()

def find_feedback():
     t=tkinter.Tk()
     t.geometry("900x800")
     t.title(" Feedback page ")
     def finddata():
         db=pymysql.connect(host='localhost',user='root',password='manager',database='CRM')
         cur=db.cursor()
         x=str(e1.get())
         if len(x)==0:
               messagebox.showinfo("Find","Call Ref No. Entry is empty. \n Please fill first.")
         else:
         
             s="select overall,r,w1,w2,s1,s2,m from feedback where call_ref_no='%s'"%(x)
             cur.execute(s)
             data=cur.fetchall()
             
             s1.delete(0,100)
             x.delete(0,100)
             y.delete(0,100)
             z.delete(0,100)
             p.delete(0,100)
             q.delete(0,100)
             r.delete(0,100)
             s1.insert(0,data[0])
             x.insert(0,data[1])
             y.insert(0,data[2])
             z.insert(0,data[3])
             p.insert(0,data[4])   
             q.insert(0,data[5])
             r.insert(0,data[6])
             db.close()
    
     def bck():
        t.destroy()
   
   
     c1=Canvas(t,width=900,height=800,bg='LightPink3')
     c1.place(x=0, y=0)
     l1=Label(c1,text=" Customer Satisfaction Survey  ",font=('Copperplate Gothic Bold',25,'bold'),bg='#Ffbe00')
     l1.place(x=160,y=10)
     l2=Label(c1,text=" Call Reference No. : ",font=('Arial',15,'bold'),bg='LightPink3')
     l2.place(x=50,y=80)
     e1=Entry(t,width=40,bd=2,relief='groove', font=('Arial Rounded MT Bold',14))
     e1.place(x=300,y=80)
  
     l3=Label(t,text=" GIVE US YOUR FEEDBACK ",font=('Stylus',15,'bold','underline'),bg='LightPink3')
     l3.place(x=10,y=150)
     l4=Label(t,text="Overall,how satisfied or dissatisfied are you with our company ?(Out of 10) ",font=('Arial',12,'bold'),fg='red4',bg='LightPink3')
     l4.place(x=10,y=190)
     s1=Spinbox(t,from_=0,to=10,width=80, font=('Arial Rounded MT Bold',10))
     s1.pack()
     s1.place(x=10,y=220,height=20) 
   
     l5=Label(t,text="Using the Scale below ,please rate your level of agreement with each of the following statements.",font=('Arial',12,'bold','underline'),bg='LightPink3')
     l5.place(x=10,y=240)
   
   
     l6=Label(t,text="Response to my query was prompt",font=('Arial',11,'bold'),bg='LightPink3')
     l6.place(x=10,y=310)
   
     l7=Label(t,text="Strongly disagree",font=('Arial',11,'bold'),bg='LightPink3')
     l7.place(x=300,y=280)
    
   
     l8=Label(t,text=" Disagree",font=('Arial',11,'bold'),bg='LightPink3')
     l8.place(x=450,y=280)
   
   
     l9=Label(t,text="Neutral",font=('Arial',11,'bold'),bg='LightPink3')
     l9.place(x=550,y=280)
   
   
     l10=Label(t,text="Agree",font=('Arial',11,'bold'),bg='LightPink3')
     l10.place(x=645,y=280)
   
   
     l11=Label(t,text="Strongly agree",font=('Arial',11,'bold'),bg='LightPink3')
     l11.place(x=725,y=280)
   
     x=IntVar()
     r1=Radiobutton(t,variable=x,value=0,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r2=Radiobutton(t,variable=x,value=1,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r3=Radiobutton(t,variable=x,value=2,bg='MediumPurple1',fg='red4',font=(10),width=8)
     r4=Radiobutton(t,variable=x,value=3,bg='MediumPurple4',fg='red4',font=(10),width=7)
     r5=Radiobutton(t,variable=x,value=4,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r1.place(x=300,y=310)
     r2.place(x=420,y=310)
     r3.place(x=530,y=310)
     r4.place(x=630,y=310)
     r5.place(x=720,y=310)
     
     l12=Label(t,text="Work was done in the time estimated ",font=('Arial',11,'bold'),bg='LightPink3')
     l12.place(x=10,y=370)
     
     
     y=IntVar()
     r1=Radiobutton(t,variable=y,value=0,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r2=Radiobutton(t,variable=y,value=1,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r3=Radiobutton(t,variable=y,value=2,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r4=Radiobutton(t,variable=y,value=3,bg='MediumPurple1',fg='red4',font=(10),width=7)
     r5=Radiobutton(t,variable=y,value=4,bg='MediumPurple4',fg='red4',font=(10),width=10)
     
     r1.place(x=300,y=370)
     r2.place(x=420,y=370)
     r3.place(x=530,y=370)
     r4.place(x=630,y=370)
     r5.place(x=720,y=370)
     
     l13=Label(t,text='''Work was done in the reasonable
     amount of time ''',font=('Arial',11,'bold'),bg='LightPink3')
     l13.place(x=10,y=430)
     
     
     z=IntVar()
     r1=Radiobutton(t,variable=z,value=0,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r2=Radiobutton(t,variable=z,value=1,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r3=Radiobutton(t,variable=z,value=2,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r4=Radiobutton(t,variable=z,value=3,bg='MediumPurple4',fg='red4',font=(10),width=7)
     r5=Radiobutton(t,variable=z,value=4,bg='MediumPurple1',fg='red4',font=(10),width=10)
     
     r1.place(x=300,y=430)
     r2.place(x=420,y=430)
     r3.place(x=530,y=430)
     r4.place(x=630,y=430)
     r5.place(x=720,y=430)
     
     
     l13=Label(t,text="Staff were quick and effiecent ",font=('Arial',11,'bold'),bg='LightPink3')
     l13.place(x=10,y=500)
     
     
     p=IntVar()
     r1=Radiobutton(t,variable=p,value=0,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r2=Radiobutton(t,variable=p,value=1,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r3=Radiobutton(t,variable=p,value=2,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r4=Radiobutton(t,variable=p,value=3,bg='MediumPurple1',fg='red4',font=(10),width=7)
     r5=Radiobutton(t,variable=p,value=4,bg='MediumPurple4',fg='red4',font=(10),width=10)
     
     r1.place(x=300,y=500)
     r2.place(x=420,y=500)
     r3.place(x=530,y=500)
     r4.place(x=630,y=500)
     r5.place(x=720,y=500)
     
     
     l14=Label(t,text='''Staff were courteous and listened
     to me ''',font=('Arial',11,'bold'),bg='LightPink3')
     l14.place(x=10,y=570)
     
     
     q=IntVar()
     r1=Radiobutton(t,variable=q,value=0,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r2=Radiobutton(t,variable=q,value=1,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r3=Radiobutton(t,variable=q,value=2,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r4=Radiobutton(t,variable=q,value=3,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r5=Radiobutton(t,variable=q,value=4,bg='MediumPurple1',fg='red4',font=(10),width=10)
     
     r1.place(x=300,y=570)
     r2.place(x=420,y=570)
     r3.place(x=530,y=570)
     r4.place(x=630,y=570)
     r5.place(x=720,y=570)
     
     
     l15=Label(t,text="My home was treated respectfuly ",font=('Arial',11,'bold'),bg='LightPink3')
     l15.place(x=10,y=640)
     
     
     r=IntVar()
     r1=Radiobutton(t,variable=r,value=0,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r2=Radiobutton(t,variable=r,value=1,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r3=Radiobutton(t,variable=r,value=2,bg='MediumPurple4',fg='red4',font=(10),width=10)
     r4=Radiobutton(t,variable=r,value=3,bg='MediumPurple1',fg='red4',font=(10),width=10)
     r5=Radiobutton(t,variable=r,value=4,bg='MediumPurple4',fg='red4',font=(10),width=10)
     
     r1.place(x=300,y=640)
     r2.place(x=420,y=640)
     r3.place(x=530,y=640)
     r4.place(x=630,y=640)
     r5.place(x=720,y=640)
     
     btn1=Button(t,text="Find Feedback", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',10),activeforeground="red",command=finddata)
     btn1.place(x=750,y=80)
     btn2=Button(t,text="Back", fg="white",bg="DarkOliveGreen",font=('Arial Rounded MT Bold',12),activeforeground="red",command=bck)
     btn2.place(x=400,y=700)
     t.mainloop()
