# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 04:08:49 2022

@author: DM
"""
import tkinter
from tkinter import Canvas,Button
from PIL import ImageTk,Image
from login import login
from feedback import ins_feedback
from aboutus import aboutus
from CS_data_management import dm
from analysis import analysis


tkt=tkinter.Tk()
tkt.geometry("1600x750")
tkt.title('CSM')
canvas=Canvas(tkt,width=1600,height=750)
canvas.place(x=0, y=0)
image=Image.open(r"E:\our_project\customer_service_mang_code\images\708746.jpg")
image=image.resize((1600,750),Image.ANTIALIAS)
my_image=ImageTk.PhotoImage(image)
canvas1=Canvas(tkt,width=1600,height=750)
canvas1.place(x=0, y=0)
canvas1.create_image(0,0,image=my_image,anchor="nw")
canvas1.create_text(700,700,text="© Copyright Customer Service Management System 2022.",font=("Copperplate Gothic Bold",10),fill="black")

#Header
image1=Image.open(r"E:\our_project\customer_service_mang_code\images\back.jpg")
image1=image1.resize((1280,500),Image.ANTIALIAS)
my_image1=ImageTk.PhotoImage(image1)
canvas2=Canvas(tkt,width=1280,height=100)
canvas2.place(x=40, y=30)
canvas2.create_image(0,0,image=my_image1,anchor="nw")
canvas2.create_text(650,50,text="Customer Service Management System",font=("Copperplate Gothic Bold",30),fill="white")


# ABOUT US
img2=Image.open(r"E:\our_project\customer_service_mang_code\images\aboutus.png")
img2=img2.resize((80,80),Image.ANTIALIAS)
my_img2=ImageTk.PhotoImage(img2)
label2=Button(text="  About Us  ",image=my_img2,bg='white',compound='top',font=('Arial Rounded MT Bold',16),fg='royalblue4',bd=5,command=aboutus)
label2.place(x=100,y=250)

      # DATA MANAGEMENT
img3=Image.open(r"E:\our_project\customer_service_mang_code\images\data.png")
img3=img3.resize((60,60),Image.ANTIALIAS)
my_img3=ImageTk.PhotoImage(img3)
label3=Button(text="Data \n Management",image=my_img3,bg='white',compound='top',font=('Arial Rounded MT Bold',15),fg='royalblue4',bd=5,command=dm)
label3.place(x=320,y=250)

        # ANALYSIS
img4=Image.open(r"E:\our_project\customer_service_mang_code\images\analysis.png")
img4=img4.resize((80,80),Image.ANTIALIAS)
my_img4=ImageTk.PhotoImage(img4)
label4=Button(text="   Analysis   ",image=my_img4,bg='white',compound='top',font=('Arial Rounded MT Bold',16),fg='royalblue4',bd=5,command=analysis)
label4.place(x=570,y=250)

          #SIGNIN/SIGNUP
img5=Image.open(r"E:\our_project\customer_service_mang_code\images\login.png")
img5=img5.resize((80,80),Image.ANTIALIAS)
my_img5=ImageTk.PhotoImage(img5)
label5=Button(text="Signin/Signup",image=my_img5,bg='white',compound='top',font=('Arial Rounded MT Bold',14),fg='royalblue4',bd=5,command=login)
label5.place(x=790,y=250)

           # FEEDBACK
img6=Image.open(r"E:\our_project\customer_service_mang_code\images\feedback.png")
img6=img6.resize((80,80),Image.ANTIALIAS)
my_img6=ImageTk.PhotoImage(img6)
label6=Button(text="  Feedback  ",image=my_img6,bg='white',compound='top',font=('Arial Rounded MT Bold',16),fg='royalblue4',bd=5,command=ins_feedback)
label6.place(x=1020,y=250)


tkt.mainloop()