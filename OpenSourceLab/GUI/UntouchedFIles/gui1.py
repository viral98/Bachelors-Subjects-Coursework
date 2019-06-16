'''import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()
'''




##############################################################
from tkinter import *
import tkinter
from tkinter import messagebox

root = Tk()
topframe = Frame(root)
topframe.place(bordermode=OUTSIDE, height=200, width=500)

var = StringVar()
l=Label(topframe, textvariable=var,relief=RAISED,width=20)
var.set("Hey!? How are you doing?")
l.pack()


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(bottomframe, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(bottomframe, text="green", fg="green")
greenbutton.pack( side = RIGHT )

bluebutton = Button(bottomframe, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)


def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(root, text ="Hello", command = helloCallBack)


B.place(bordermode=OUTSIDE, height=100, width=100)
root.mainloop()








