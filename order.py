from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title("Pizza Corner!")
root.geometry("800x540+200+50")
root.iconbitmap('images/pizza.ico')

myImg=ImageTk.PhotoImage(Image.open("images/Welcome.png"))
my_label =Label(root,image=myImg)
my_label.pack(pady=2,padx=2)

frame=LabelFrame(root,text='Order Your Pizza',font='Lora',padx=98,pady=12,bd=4)
frame.pack()
#name
Name=Label(frame,text='Name',anchor=W).grid(row=0,column=0)
free=Label(frame,text="   ").grid(row=0,column=1)
name=StringVar()
n=Entry(frame,textvariable="name").grid(row=0,column=2)
freerow=Label(frame,text=' ').grid(row=1,column=0)
#address
Address=Label(frame,text='Address').grid(row=2,column=0)
free1=Label(frame,text="   ").grid(row=2,column=1)
address=StringVar()
a=Entry(frame,textvariable='address').grid(row=2,column=2)
freerow2=Label(frame,text=" ").grid(row=3,column=0)
#type
PizzaType=Label(frame,text="Pizza Type").grid(row=4,column=0)
free2=Label(frame,text=" ").grid(row=4,column=1)
p_type=StringVar()
small= Radiobutton(frame,text='Small',variable= p_type,value="Small").grid(row=4,column=2)
Medium= Radiobutton(frame,text='Medium',variable=p_type,value="Medium").grid(row=4,column=3)
Large= Radiobutton(frame,text='Large',variable=p_type,value="Large").grid(row=4,column=4)
freerow3=Label(frame,text=" ").grid(row=5,column=0)
#mobile
Mobile=Label(frame,text='Mobile No.').grid(row=6,column=0)
free3=Label(frame,text="   ").grid(row=6,column=1)
mobile=StringVar()
m=Entry(frame,textvariable="mobile").grid(row=6,column=2)
freerow4=Label(frame,text="").grid(row=7,column=0)
#email
Email=Label(frame,text='E-mail').grid(row=8,column=0)
free4=Label(frame,text="").grid(row=8,column=1)
email=StringVar()
e=Entry(frame,textvariable='email').grid(row=8,column=2)
freerow5=Label(frame,text="").grid(row=9,column=0)
free5=Label(frame,text="").grid(row=10,column=0)
free5=Label(frame,text="").grid(row=10,column=1)
#button
def order():
    response= messagebox.showinfo("Order","Your order will be served soon")

Order_Pizza=Button(frame, text='Order',height=1,width=8,bd=4,bg='#7ea04d',activebackground='#7ea04d',command=order).grid(row=10,column=2)

root.mainloop()