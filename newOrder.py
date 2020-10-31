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

frame=LabelFrame(root,text='Orders',font='Lora',padx=360,pady=120,bd=4)
frame.pack()




myLabel1=Label(frame,text="  ")
myLabel1.grid(row=0,column=1)


root.mainloop()