# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:20:44 2022

@author:
"""

import tkinter
from tkinter import *


def aboutus():
    t=tkinter.Tk()
    t.geometry('1200x700')
    t.title('ABOUT US')
    c=Canvas(t,width=1200,height=700, bg='OliveDrab4')
    c.pack(padx=0,pady=0)
    c1=Canvas(c,width=1200,height=700, bg='OliveDrab3',highlightthickness=0)
    c1.pack(padx=20,pady=20)
    c2=Canvas(c1,width=1200,height=700, bg='OliveDrab2',highlightthickness=0)
    c2.pack(padx=20,pady=20)
    top_frame = Frame(c2, width=1200, height=400)
    top_frame.pack(side='top', padx=0, pady=0, expand=True)
    
    c3=Canvas(top_frame,width=1200,height=700, bg='OliveDrab1',highlightthickness=0)
    c3.pack(padx=0,pady=0)
    c3.create_text(500,50,text="About Us",font=("Copperplate Gothic Bold",30,'bold','underline'),justify='center',fill="white")
    
    c3.create_text(500 ,150,text='''The “Customer Service Management System” is a desktop based application. It is based on
                   Customer Relationship Management (CRM) approach.
                   
                   Customer Service Management is how a company runs its customer service operation and 
                   enable consistently great service experiences that drive customer loyalty. It includes
                   everything from training new service representative, to optimizing support processes, 
                   to measuring service success.''',font=('Arial' ,13,'bold'),justify='center')
    
    
    c3.create_text(500,250,text="Team Members ",font=("Copperplate Gothic Bold",25,'underline'),justify='center',fill="white")
    c3.create_text(150,300,text="DEEPAK MISHRA ",font=("Copperplate Gothic Bold",16))
    c3.create_text(550,300,text="HARSHITA GAUTAM ",font=("Copperplate Gothic Bold",16))
    c3.create_text(950,300,text="CHARU PATHAK ",font=("Copperplate Gothic Bold",16))
    
    
    
    c3.create_text(150,350,text="9058776650",font=("Copperplate Gothic Bold",12))
    c3.create_text(550,350,text="9068647111",font=("Copperplate Gothic Bold",12))
    c3.create_text(950,350,text="8979212087 ",font=("Copperplate Gothic Bold",12))
    
    c3.create_text(150,400,text="deera1910@gmail.com",font=("Arial",12,'bold'))
    c3.create_text(550,400,text="harshitagautam497@gmail.com",font=("Arial",12,'bold'))
    c3.create_text(950,400,text="pvtptk05@gmail.com",font=("Arial",12,'bold'))
    
    t.mainloop()