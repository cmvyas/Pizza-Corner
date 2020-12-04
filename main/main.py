from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql
from PIL import ImageTk,Image
import os
import sys 
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("Pizza Corner!")
root.geometry("1100x650+100+1")

root.resizable(False, False)
root.iconbitmap('images/pizza.ico')

myImg = ImageTk.PhotoImage(Image.open("images/Welcome.png"))
#my_label = Label(root, image=myImg)
#my_label.pack()

########variables 
Id_var=StringVar()
Name_var=StringVar()
Address_var=StringVar()
Type_var=StringVar()
Mobile_var=StringVar()
Email_var=StringVar()

frame = LabelFrame(root, text='Order Your Pizza!', font='Lora', padx=20, pady=20, bd=4, relief=GROOVE)
frame.place(x=70, y=60, width=390, height=310)
#####################table#########3
frame1= LabelFrame(root, text='', font='Lora', padx=20, pady=20, bd=4, relief=GROOVE)
frame1.place(x=490, y=70, width=550, height=430)

scrollY=Scrollbar(frame1,orient=VERTICAL)
scrollX=Scrollbar(frame1,orient=HORIZONTAL)
table= Treeview(frame1,columns=("Id","Name","Address","Size","Mobile","Email"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
scrollX.pack(side=BOTTOM,fill=X)
scrollY.pack(side=RIGHT,fill=Y)
scrollX.config(command=table.xview)
scrollY.config(command=table.yview)
table.heading("Id",text="ID")
table.heading("Name",text="NAME")
table.heading("Address",text="ADDRESS")
table.heading("Size",text="SIZE")
table.heading("Mobile",text="MOBILE")
table.heading("Email",text="EMAIL ")
table['show']='headings'
table.column("Id",width=50)
table.column("Name",width=100)
table.column("Address",width=150)
table.column("Size",width=100)
table.column("Mobile",width=100)
table.column("Email",width=100)
table.pack(fill=BOTH,expand=1)


frame2 = LabelFrame(root, text='Track Your Order', font='Lora', padx=50, pady=10, bd=4)
frame2.place(x=70, y=380, width=390, height=120)

frame3 = LabelFrame(root, text='Cancel Order', font='Lora', padx=50, pady=10, bd=4)
frame3.place(x=70, y=500, width=390, height=120)

frame4 = LabelFrame(root, text='Vendor Corner', font='Lora', padx=50, pady=25, bd=4)
frame4.place(x=630, y=500, width=776, height=130)



###########order
Id= Label(frame, text='Id', anchor=W).grid(row=0, column=0)
free = Label(frame, text="   ").grid(row=0, column=1)
n = Entry(frame,textvariable=Id_var)
n.grid(row=0, column=2)
freerow = Label(frame, text=' ').grid(row=1, column=0)


Name = Label(frame, text='Name', anchor=W).grid(row=2, column=0)
free = Label(frame, text="   ").grid(row=2, column=1)
n = Entry(frame,textvariable=Name_var)
n.grid(row=2, column=2)
freerow = Label(frame, text=' ').grid(row=3, column=0)

#address
Address = Label(frame, text='Address').grid(row=4, column=0)
free1 = Label(frame, text="   ").grid(row=4, column=1)
a = Entry(frame,textvariable=Id_Address)
a.grid(row=4, column=2)
freerow2 = Label(frame, text=" ").grid(row=5, column=0)



#type
PizzaType = Label(frame, text=" Type").grid(row=6, column=0)
free2 = Label(frame, text=" ")
type=ttk.Combobox(frame,textvariable=Type_var,text="Pizza Type",state='readonly')
type['values']=("Small","Medium","Large")
type.grid(row=6, column=2)
freerow4 = Label(frame, text="").grid(row=7, column=0)

#mobile
Mobile = Label(frame, text='Mobile').grid(row=8, column=0)
free3 = Label(frame, text="   ").grid(row=8, column=1)
m = Entry(frame,textvariable=Mobile_var)
m.grid(row=8, column=2)
freerow4 = Label(frame, text="").grid(row=9, column=0)

#email
Email = Label(frame, text='E-mail').grid(row=10, column=0)
free4 = Label(frame, text="").grid(row=10, column=1)
e = Entry(frame,textvariable=Email_var)
e.grid(row=10, column=2)
freerow5 = Label(frame, text="").grid(row=11, column=0)
free5 = Label(frame, text="").grid(row=12, column=0)
free5 = Label(frame, text="").grid(row=12, column=1)


#button
def insert(self):
	con=pymysql.connect(host='localhost',user='root',password="root",database="pizza")

Order_Pizza = Button(frame, text='Order', height=1, width=8, bd=4, bg='#7ea04d', activebackground='#7ea04d', command=insert).grid(row=10,column=2)

######### track
Order_Id = Label(frame2, text='Order_Id', anchor=W).grid(row=0, column=0)
free = Label(frame2, text="   ").grid(row=0, column=1)
n3 = Entry(frame2)
n3.grid(row=0, column=2)
freerow = Label(frame2, text=' ').grid(row=1, column=0)

free5 = Label(frame2, text="").grid(row=2, column=0)
free5 = Label(frame2, text="").grid(row=2, column=1)

def track():
	n6 = int(n3.get())
	status = pizza_q[n6]['Status']
	if status == 'Pending':
		response = messagebox.showinfo("track", f"Your order is pending, will be served soon")
	else:
		response = messagebox.showinfo("track", f"Your order is served")

Track_Pizza = Button(frame2, text='Track', height=1, width=12, bd=4, bg='#7ea04d', command=track, activebackground='#7ea04d').grid(row=2,column=2)

############Cancel


Order_Id = Label(frame3, text='Order_Id').grid(row=2, column=0)
free1 = Label(frame3, text="   ").grid(row=2, column=1)
a3 = Entry(frame3)
a3.grid(row=2, column=2)
freerow2 = Label(frame3, text=" ").grid(row=3, column=0)

#free5 = Label(frame3, text=" ").grid(row=4, column=0)
#free5 = Label(frame3, text="").grid(row=4, column=1)

cancel_count = 0
def cancel():
	global cancel_count
	n5 = n4.get()
	a4 = int(a3.get())
	if pizza_q[a4].get('Name') == n5:
		pizza_q.pop(a4)
	cancel_count += 1

def cancel_button():
    response = messagebox.askyesno("Cancel Order", "Do you want to cancel your Order ?")
    if response == 1:
        free5 = Label(frame3,text=" ").grid(row=5,column=0)
        free5 = Label(frame3,text="").grid(row=5,column=1)
        cancel()
        messagebox.showinfo("","Cancelled Successfully")
    else :
        free5 = Label(frame3,text=" ").grid(row=5,column=0)
        free5 = Label(frame3,text="").grid(row=5,column=1)
        messagebox.showerror("","Try Again")


Cancel_Pizza = Button(frame3, text='Cancel', height=1, width=12, bd=4, bg='#7ea04d', activebackground='#7ea04d',command=cancel_button).grid(row=4,column=2)

############ vendor
def New_Order():
	response = messagebox.showinfo("Orders", f"You have {len(pizza_q)} orders")

New_Order = Button(frame4, text='New Orders', height=2, width=14, bd=4, bg='#7ea04d', activebackground='#7ea04d', command=New_Order)

def Cancel_Order():
	response = messagebox.showinfo("Canceled Orders", f"You have {cancel_count} cancelled orders")
	
Canceled_Order = Button(frame4, text='Canceled Order ', command=Cancel_Order, height=2, width=14, bd=4, bg='#7ea04d', activebackground='#7ea04d')
def Served():
	response = messagebox.showinfo("Served","You have 0 served orders")

Served_Order = Button(frame4, text='Served Orders', height=2, width=14, bd=4, bg='#7ea04d', activebackground='#7ea04d', command=Served)

def Pending():
	response = messagebox.showinfo("Pending", f"You have {len(pizza_q)} pending orders")
	
Pending_Order = Button(frame4, text='Pending Orders', height=2, width=14, bd=4, bg='#7ea04d', activebackground='#7ea04d', command=Pending)
myLabel3 = Label(frame4, text = "         ")
myLabel4 = Label(frame4, text = "         ")
myLabel1 = Label(frame4, text = "         ")
myLabel2 = Label(frame4, text = "         ")

myLabel4.grid(row=0, column=0)
New_Order.grid(row=0, column=1)
myLabel1.grid(row=0, column=2)
Canceled_Order.grid(row=0, column=3)
myLabel2.grid(row=0, column=4)
Served_Order.grid(row=0, column=5)
myLabel3.grid(row=0, column=6)
Pending_Order.grid(row=0, column=7)

root.mainloop()
