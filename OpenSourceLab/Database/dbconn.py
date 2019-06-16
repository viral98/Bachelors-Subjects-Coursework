import sqlite3
conn = sqlite3.connect('employee.db')
c= conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS employee( first TEXT, last TEXT, pay INTEGER ) """)
#c.execute(""" INSERT INTO employee VALUES ('Viral', 'Tagdiwala', 1200000) """)
choice=1
while(choice<5):
	pass
	choice = int(input("Enter 1)INSERT 2)UPDATE 3)DELETE 4)DISPLAY 5)EXIT"))
	if(choice==1):
		first = input("Enter first name")
		last = input("Enter last name")
		pay = int(input("Enter his pay scale"))
		c.execute(""" INSERT INTO employee VALUES ('{}','{}','{}') """.format(first,last,pay))
		c.execute(""" SELECT * FROM employee """)
		print(c.fetchall())
	elif(choice==2):
		name = input("Enter the name")
		payscale = int(input("Enter his updated payscale"))
		c.execute(""" UPDATE employee SET pay = ? WHERE first = ? """,(payscale,name))
		c.execute(""" SELECT * FROM employee """)
		print(c.fetchall())
	elif(choice==3):
		name = input("Enter the name")
		c.execute(""" DELETE FROM employee WHERE first = :name """,{'name': name})
		c.execute(""" SELECT * FROM employee """)
		print(c.fetchall())
	elif(choice==4):
		c.execute(""" SELECT * FROM employee """)
		print(c.fetchall())


conn.commit()
conn.close()