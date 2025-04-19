import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import tkinter.font as f

root = Tk()
root.geometry("350x200")
root.title("calender")
root.config(background = "turquoise")

title = Label(root,text = "Calender",font = f.Font(size = 30))
title.place(x = 90,y = 0)

label1 = Label(root,text = "enter the year",font = ("Arial",15))
label1.place(x = 105, y = 55)

yearbox = Entry(root)
yearbox.place(x = 30, y = 80,width = 270)

root.mainloop()