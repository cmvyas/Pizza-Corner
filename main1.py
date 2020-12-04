from tkinter import *
from PIL import ImageTk,Image
import os
import sys 
from tkinter import messagebox
from PIL import ImageTk,Image
class Pizzaa:
	def __init__(self,root):
        self.root=root
	    self.root.title("Pizza Corner")
        self.root.geometry("1100x650+100+1")
        self.root.resizable(False, False)
        self.root.iconbitmap('images/pizza.ico')

    myImg = ImageTk.PhotoImage(Image.open("images/Welcome.png"))
    
root = Tk()
ob=Pizzaa(root)
root.mainloop()