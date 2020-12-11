from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql
from PIL import ImageTk,Image
import os
import sys 
from tkinter import messagebox
from PIL import ImageTk,Image

class pizza:
	def __init__(self,root):
		self.root=root
		self.root=Tk()
		self.root.title("Pizza Corner!")
		self.root.geometry("1100x650+100+1")
		self.root.resizable(False, False)
		self.root.iconbitmap('images/pizza.ico')
		myImg = ImageTk.PhotoImage(Image.open("images/Welcome.png"))
		#### variables
		self.Id_var=StringVar()
		self.Name_var=StringVar()
		self.Address_var=StringVar()
		self.Type_var=StringVar()
		self.Mobile_var=StringVar()
		self.Email_var=StringVar()
		frame = LabelFrame(self.root, text='Order Your Pizza!', font='Lora', padx=20, pady=20, bd=4, relief=GROOVE)
		frame.place(x=70, y=60, width=390, height=310)
		#####################table#########3
		frame1= LabelFrame(self.root, text='', font='Lora', padx=20, pady=20, bd=4, relief=GROOVE)
		frame1.place(x=490, y=70, width=550, height=430)

		scrollY=Scrollbar(frame1,orient=VERTICAL)
		scrollX=Scrollbar(frame1,orient=HORIZONTAL)
		self.table= Treeview(frame1,columns=("Id","Name","Address","Size","Mobile","Email"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
		scrollX.pack(side=BOTTOM,fill=X)
		scrollY.pack(side=RIGHT,fill=Y)
		scrollX.config(command=self.table.xview)
		scrollY.config(command=self.table.yview)
		self.table.heading("Id",text="ID")
		self.table.heading("Name",text="NAME")
		self.table.heading("Address",text="ADDRESS")
		self.table.heading("Size",text="SIZE")
		self.table.heading("Mobile",text="MOBILE")
		self.table.heading("Email",text="EMAIL ")
		self.table['show']='headings'
		self.table.column("Id",width=50)
		self.table.column("Name",width=100)
		self.table.column("Address",width=150)
		self.table.column("Size",width=100)
		self.table.column("Mobile",width=100)
		self.table.column("Email",width=100)
		self.table.pack(fill=BOTH,expand=1)
		self.fetchh()


		frame2 = LabelFrame(self.root, text='Track Your Order', font='Lora', padx=50, pady=10, bd=4)
		frame2.place(x=70, y=380, width=390, height=120)

		frame3 = LabelFrame(self.root, text='Cancel Order', font='Lora', padx=50, pady=10, bd=4)
		frame3.place(x=70, y=500, width=390, height=120)

		frame4 = LabelFrame(self.root, text='Vendor Corner', font='Lora', padx=50, pady=25, bd=4)
		frame4.place(x=630, y=500, width=776, height=130)

		###########order
		Id= Label(frame, text='Id', anchor=W).grid(row=0, column=0)
		free = Label(frame, text="   ").grid(row=0, column=1)
		n = Entry(frame,textvariable=self.Id_var)
		n.grid(row=0, column=2)
		freerow = Label(frame, text=' ').grid(row=1, column=0)
		Name = Label(frame, text='Name', anchor=W).grid(row=2, column=0)
		free = Label(frame, text="   ").grid(row=2, column=1)
		n = Entry(frame,textvariable=self.Name_var)
		n.grid(row=2, column=2)
		freerow = Label(frame, text=' ').grid(row=3, column=0)
		#address
		Address = Label(frame, text='Address').grid(row=4, column=0)
		free1 = Label(frame, text="   ").grid(row=4, column=1)
		a=Entry(frame,textvariable=self.Address_var)
		a.grid(row=4, column=2)
		freerow2 = Label(frame, text=" ").grid(row=5, column=0)
		PizzaType = Label(frame, text=" Type").grid(row=6, column=0)
		free2 = Label(frame, text=" ")
		type=ttk.Combobox(frame,textvariable=self.Type_var,text="Pizza Type",state='readonly')
		type['values']=("Small","Medium","Large")
		type.grid(row=6, column=2)
		freerow4 = Label(frame, text="").grid(row=7, column=0)
		Mobile = Label(frame, text='Mobile').grid(row=8, column=0)
		free3 = Label(frame, text="   ").grid(row=8, column=1)
		m = Entry(frame,textvariable=self.Mobile_var)
		m.grid(row=8, column=2)
		freerow4 = Label(frame, text="").grid(row=9, column=0)

		Email = Label(frame, text='E-mail').grid(row=10, column=0)
		free4 = Label(frame, text="").grid(row=10, column=1)
		e = Entry(frame,textvariable=self.Email_var)
		e.grid(row=10, column=2)
		freerow5 = Label(frame, text="").grid(row=11, column=0)
		free5 = Label(frame, text="").grid(row=12, column=0)
		free5 = Label(frame, text="").grid(row=12, column=1)
		Order_Pizza = Button(frame, text='Order', height=1, width=8, bd=4, bg='#7ea04d', activebackground='#7ea04d', command=self.insert).grid(row=10,column=2)

		#############track
		Order_Id = Label(frame2, text='Order_Id', anchor=W).grid(row=0, column=0)
		free = Label(frame2, text="   ").grid(row=0, column=1)
		n3 = Entry(frame2)
		n3.grid(row=0, column=2)
		freerow = Label(frame2, text=' ').grid(row=1, column=0)

		free5 = Label(frame2, text="").grid(row=2, column=0)
		free5 = Label(frame2, text="").grid(row=2, column=1)
		Track_Pizza = Button(frame2, text='Track', height=1, width=12, bd=4, bg='#7ea04d', command=track, activebackground='#7ea04d').grid(row=2,column=2)

		############Cancel
		Order_Id = Label(frame3, text='Order_Id').grid(row=2, column=0)
		free1 = Label(frame3, text="   ").grid(row=2, column=1)
		a3 = Entry(frame3)
		a3.grid(row=2, column=2)
		freerow2 = Label(frame3, text=" ").grid(row=3, column=0)
		Cancel_Pizza = Button(frame3, text='Cancel', height=1, width=12, bd=4, bg='#7ea04d', activebackground='#7ea04d',command=cancel_button).grid(row=4,column=2)
	

	def insert(self):
		con=pymysql.connect(host='localhost',user='root',password="",database="pizzza")
		cur=con.cursor()
		cur.execute("insert into customerorder values(%s,%s,%s,%s,%s,%s)",(self.Id_var.get(),self.Name_var.get(),self.Address_var.get(),self.Type_var.get(),self.Mobile_var.get(),self.Email_var.get()))
		con.commit()
		self.fetchh()
		self.clear()
		con.close()

	def fetchh(self):
		con=pymysql.connect(host='localhost',user='root',password="",database="pizzza")
		cur=con.cursor()
		cur.execute("select * from customerorder ")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.table.delete(*self.table.get_children())
			for row in rows:
				self.table.insert('',END,values=row)
			con.commit()
		con.close()

	def clear(self):
		self.Id_var.set("")
		self.Name_var.set("")
		self.Address_var.set("")
		self.Type_var.set("")
		self.Mobile_var.set("")
		self.Email_var.set("")




       
######### track

def track():
	n6 = int(n3.get())
	status = pizza_q[n6]['Status']
	if status == 'Pending':
		response = messagebox.showinfo("track", f"Your order is pending, will be served soon")
	else:
		response = messagebox.showinfo("track", f"Your order is served")


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





root=Tk()
ob=pizza(root)
root.mainloop()
