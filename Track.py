from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Pizza Corner!")
root.geometry("800x540")
root.iconbitmap('images/pizza.ico')

myImg=ImageTk.PhotoImage(Image.open("images/Welcome.png"))
my_label =Label(root,image=myImg)
my_label.pack(pady=20,padx=2)

frame=LabelFrame(root,text='Track Order',font='Lora',padx=80,pady=20,bd=4)
frame.pack()

Order_Id=Label(frame,text='Order_Id',anchor=W).grid(row=0,column=0)
free=Label(frame,text="   ").grid(row=0,column=1)
n=Entry(frame).grid(row=0,column=2)
freerow=Label(frame,text=' ').grid(row=1,column=0)




free5=Label(frame,text="").grid(row=2,column=0)
free5=Label(frame,text="").grid(row=2,column=1)


Cancel_Pizza=Button(frame, text='Track',height=1,width=12,bd=4,bg='#7ea04d',activebackground='#7ea04d').grid(row=2,column=2)


root.mainloop()