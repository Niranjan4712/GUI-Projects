#Tkinter checkbox
#syntax=CheckButton(parent,attribute)
import tkinter
from tkinter import *
j=tkinter.Tk()
j.geometry("600x600+10+90")
j.title('Check button')

check1=Checkbutton(j,text='Python')
check1.place(x=10,y=30)

mainloop()