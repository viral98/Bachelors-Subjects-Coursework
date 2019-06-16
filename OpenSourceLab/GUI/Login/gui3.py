from tkinter import *
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("login.db")
c2=conn.cursor()
root=Tk()
label_1=Label(root,text="Name")
label_2=Label(root,text="Password")
entry_1=Entry(root)
entry_2=Entry(root)
label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
c=Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)



def printName(event):
    print("hello")

def LoginMessagebox():
   messagebox.showinfo( "Login successful", "Login successful")


def registerWindow():
	# create child window
	win = Toplevel()
	# display message
	message = "Enter Details"
	Label(win, text=message).grid()
	label_3=Label(win,text='Username: ')
	label_4=Label(win,text='Password: ')
	entry_3=Entry(win)
	entry_4=Entry(win)
	label_3.grid(row=1,sticky=E)
	label_4.grid(row=2,sticky=E)
	entry_3.grid(row=1,column=1)
	entry_4.grid(row=2,column=1)
	def insert():
		uname=entry_3.get()
		password=entry_4.get()
		c2.execute("insert into users values(?,?)",(uname,password))
		print(c2.fetchall())
		conn.commit()
		messagebox.showinfo( "Registration successful", "Registration successful")
	button_3=Button(win,text="Register",command=insert)
	button_3.grid()
	# quit child window and return to root window
	# the button is optional here, simply use the corner x of the child window
	Button(win, text='OK', command=win.destroy).grid()



def checkDetails(event):
	uname=entry_1.get()
	password=entry_2.get()
	c2.execute("select username from users where username=? and password=?",(uname,password))
	res=c2.fetchall()
	if(uname==res[0][0]):
		LoginMessagebox()
		#messageWindow()
	else:
		print("Login unsuccessful")
#button_1=Button(root,text="print my name",command=printName)
button_1=Button(root,text="Login")
button_1.bind('<Button-1>',checkDetails)  
button_1.grid()
button_2=Button(root,text="Register",command=registerWindow)

button_2.grid()

def doNothing():
    print("ok I wont")

mymenu=Menu(root)
root.config(menu=mymenu)  #to configure menu


submenu=Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New project",command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit",command=doNothing)

editmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="redo",command=doNothing)

root.mainloop()

