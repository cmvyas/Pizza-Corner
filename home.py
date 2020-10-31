from tkinter import *
from PIL import ImageTk,Image
import os
import sys 






root = Tk()
root.title("Pizza Corner!")
root.geometry("800x540+200+50")
root.resizable(False,False)
root.iconbitmap('images/pizza.ico')

myImg=ImageTk.PhotoImage(Image.open("images/Welcome.png"))
my_label =Label(root,image=myImg)
my_label.pack(pady=10,padx=10)

frame=LabelFrame(root,text='WELCOME!',font='Lora',padx=180,pady=50,bd=4)
frame.pack()

def callCustomer():
	os.system('python customer.py')

Customer=Button(frame, text='Customer',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d',command=callCustomer)


def callVendor():
	os.system('python vendor.py')
Vendor=Button(frame, text='Vendor ',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d',command=callVendor)

myLabel1=Label(frame,text="  ")
myLabel2=Label(frame,text="  ")

Customer.grid(row=0, column=0)
myLabel1.grid(row=0,column=1)
Vendor.grid(row=0,column=2)
myLabel2.grid(row=0,column=3)






root.mainloop()