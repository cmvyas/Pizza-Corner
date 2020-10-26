from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Pizza Corner!")
root.geometry("800x540")
root.iconbitmap('images/pizza.ico')

myImg=ImageTk.PhotoImage(Image.open("images/Welcome.png"))
my_label =Label(root,image=myImg)
my_label.pack(pady=10,padx=10)

frame=LabelFrame(root,text='WELCOME!',font='Lora',padx=180,pady=50,bd=4)
frame.pack()
Order_Pizza=Button(frame, text='Order Pizza',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d')

Cancel_Order=Button(frame, text='Cancel Order ',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d')
Track_Order=Button(frame, text='Track Order ',height=2,width=14,bd=4,bg='#7ea04d',activebackground='#7ea04d')
myLabel1=Label(frame,text="  ")
myLabel2=Label(frame,text="  ")

Order_Pizza.grid(row=0, column=0)
myLabel1.grid(row=0,column=1)
Cancel_Order.grid(row=0,column=2)
myLabel2.grid(row=0,column=3)
Track_Order.grid(row=0,column=4)





root.mainloop()