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

Name=Label(frame,text='Name',anchor=W).grid(row=0,column=0)
free=Label(frame,text="   ").grid(row=0,column=1)
n=Entry(frame).grid(row=0,column=2)
freerow=Label(frame,text=' ').grid(row=1,column=0)

Address=Label(frame,text='Address').grid(row=2,column=0)
free1=Label(frame,text="   ").grid(row=2,column=1)
a=Entry(frame).grid(row=2,column=2)
freerow2=Label(frame,text=" ").grid(row=3,column=0)

PizzaType=Label(frame,text="Pizza Type").grid(row=4,column=0)
free2=Label(frame,text=" ").grid(row=4,column=1)
small= Checkbutton(frame,text='Small').grid(row=4,column=2)
Medium= Checkbutton(frame,text='Medium').grid(row=4,column=3)
Large= Checkbutton(frame,text='Large').grid(row=4,column=4)
freerow3=Label(frame,text=" ").grid(row=5,column=0)

Mobile=Label(frame,text='Mobile No.').grid(row=6,column=0)
free3=Label(frame,text="   ").grid(row=6,column=1)
m=Entry(frame).grid(row=6,column=2)
freerow4=Label(frame,text="").grid(row=7,column=0)

Email=Label(frame,text='E-mail').grid(row=8,column=0)
free4=Label(frame,text="   ").grid(row=8,column=1)
e=Entry(frame).grid(row=8,column=2)
freerow5=Label(frame,text="").grid(row=9,column=0)

free5=Label(frame,text="").grid(row=10,column=0)
free5=Label(frame,text="").grid(row=10,column=1)
def order():
    response= messagebox.showinfo("Order","Your order will be served soon")

Order_Pizza=Button(frame, text='Order',height=1,width=8,bd=4,bg='#7ea04d',activebackground='#7ea04d',command=order).grid(row=10,column=2)

root.mainloop()