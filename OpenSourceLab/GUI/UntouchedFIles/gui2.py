from tkinter import *
import tkinter
from tkinter import messagebox

root = Tk()
topframe = Frame(root)
topframe.grid()

bottomframe = Frame(root)
bottomframe.grid()

redbutton = Button(topframe, text="Red", fg="red")
redbutton.grid()

greenbutton = Button(bottomframe, text="green", fg="green")
greenbutton.grid()

bluebutton = Button(bottomframe, text="Blue", fg="blue")
bluebutton.grid()

blackbutton = Button(topframe, text="Black", fg="black")
blackbutton.grid()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(topframe, text ="Hello", command = helloCallBack)

B.grid()
#B.place(bordermode=OUTSIDE, height=10, width=10)
root.mainloop()
