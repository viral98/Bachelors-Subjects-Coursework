from tkinter import *
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
#button_1=Button(root,text="print my name",command=printName)
button_1=Button(root,text="print my name")
button_1.bind('<Button-1>',printName)  
button_1.grid()


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

