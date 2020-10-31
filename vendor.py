from tkinter import *
from PIL import ImageTk,Image
import os
import sys 

root = Tk()
root.title("Vendor")
root.geometry("800x540+200+50")
root.resizable(False,False)
root.iconbitmap('images/pizza.ico')

myImg=ImageTk.PhotoImage(Image.open("images/Welcome.png"))
my_label =Label(root,image=myImg)
my_label.pack(pady=10,padx=10)

frame=LabelFrame(root,text='Pizza-Corner!',font='Lora',padx=100,pady=50,bd=4)
frame.pack()

#def connectOrder():
#	os.system('python order.py')

New_Order=Button(frame, text='New Order',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d')


#def cancelOrder():
#	os.system('python cancel.py')
Canceled_Order=Button(frame, text='Canceled Order ',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d')

#def trackOrder():
#	os.system('python Track.py')
Served_Order=Button(frame, text='Served Order ',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d')
myLabel1=Label(frame,text="  ")
myLabel2=Label(frame,text="  ")

Pending_Order=Button(frame, text='Pending Order ',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d')
myLabel3=Label(frame,text="  ")






New_Order.grid(row=0, column=0)
myLabel1.grid(row=0,column=1)
Canceled_Order.grid(row=0,column=2)
myLabel2.grid(row=0,column=3)
Served_Order.grid(row=0,column=4)
myLabel3.grid(row=0,column=5)
Pending_Order.grid(row=0,column=6)




root.mainloop()