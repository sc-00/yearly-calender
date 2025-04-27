from tkinter import *
import tkinter.font as f
import calendar

root = Tk()
root.geometry("350x200")
root.title("calender")
root.config(background = "turquoise")

def showcalendar():
    newwindow = Tk()
    newwindow.config(background = "wheat")
    newwindow.title("Calendar")
    getyear = int(yearbox.get())
    calendarcontent = calendar.calendar(getyear)
    calendarshow = Label(newwindow,text = calendarcontent)
    calendarshow.grid(row = 5, column = 1,padx = 20)
    newwindow.mainloop

title = Label(root,text = "Calendar",font = f.Font(size = 30))
title.place(x = 90,y = 0)

label1 = Label(root,text = "enter the year",font = ("Arial",15))
label1.place(x = 105, y = 50)

yearbox = Entry(root)
yearbox.place(x = 30, y = 80,width = 270)

calendarappear = Button(root,text = "Show Calendar",command = showcalendar,font = ("Arial",10))
calendarappear.place(x = 120, y = 110)

exitb = Button(root, text = "Exit",font = ("Arial",10),command = root.destroy)
exitb.place(x = 125,y = 140)

root.mainloop()