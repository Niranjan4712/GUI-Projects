import tkinter##Regular button widgets
from tkinter import *
j=tkinter.Tk()
j.title("widgets")
j.geometry("300x500+90+90")
btn=Button(j,text='press',bg='black',fg='red')
btn.place(x=5,y=9)

j.mainloop()
#syntax
#btn=Button(parent,attributes)