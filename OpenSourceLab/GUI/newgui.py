from tkinter import *
import sqlite3
conn = sqlite3.connect('employee.db')
c= conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS login( name TEXT, password TEXT) """)
root=Tk()
label_1=Label(root,text="Name")
label_2=Label(root,text="Password")
entry_1=Entry(root)
entry_2=Entry(root)
label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
c1=Checkbutton(root,text="keep me logged in")
c1.grid(columnspan=2)

def printName(event):
	passw = entry_2.get()
	uname = entry_1.get()
	print(passw)
	print(uname)
	c.execute(""" SELECT name FROM login WHERE name = ? and password= ? """, (uname,passw))
	c.execute(""" SELECT * FROM login """)
	#print(c.fetchall())
	res=c.fetchall()
	print(res)
	flag=1
	for x in c.fetchall():
		if x == uname:
			print(x)
			print("User logged in")
			flag=0
	if flag==1:
		print("Invalid")
	'''if (uname!=res[0]):
		print("User does not exist")
	else:
		print("Logged in, user")
		print(entry_1.get())
	'''
		
#button_1=Button(root,text="print my name",command=printName)
button_1=Button(root,text="print my name")
button_1.bind('<Button-1>',printName)  
button_1.grid()


def doNothing():
	c.execute(""" SELECT * FROM login """)
	print(c.fetchall())

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

def registerUser(event):
	c.execute(""" INSERT INTO login VALUES ('{}','{}') """.format(entry_r1.get(),entry_r2.get()))
	conn.commit()

#Registeration
label_r0=Label(root,text="New User? Register here!")
label_r1=Label(root,text="Name")
label_r2=Label(root,text="Password")
entry_r1=Entry(root)
entry_r2=Entry(root)
label_r1.grid(row=6,sticky=E)
label_r0.grid(row=5,column=1)
label_r2.grid(row=7,sticky=E)
entry_r1.grid(row=6,column=1)
entry_r2.grid(row=7,column=1)
button_2=Button(root,text="Register")
button_2.bind('<Button-1>',registerUser)  
button_2.grid()
root.mainloop()

