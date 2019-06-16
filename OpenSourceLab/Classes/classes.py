import datetime
class Emp:
	raiseSalary = 1.5
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
	def printStuff(self):
		print("My name is : ",self.name)
		print("I earn :Rs",self.salary)
	def raiseMySalary(self):
		self.salary = self.salary * self.raiseSalary
		self.printStuff()
	@classmethod
	def showRaise(cls,newAmount):
		print("The global raise is :",cls.raiseSalary)
		cls.raiseSalary = newAmount
		print("Salary raise amount has been changed to ",cls.raiseSalary)
	@staticmethod
	def is_date_weekday(todayDate):
			check = todayDate.weekday()
			return check

class developer(Emp):
	def __init__(self,name,salary,language):
		self.name=name
		self.salary=salary
		self.language=language
	def printMyDeveloper(self):
		self.printStuff()
		print("My language of choice is: ",self.language)

class manager(Emp):
	def __init__(self,name,salary,list):
		super().__init__(name,salary)
		self.employeesUnderMe = list

	def printMyManager(self):
		self.printStuff()
		print("Employees working under me are ",self.employeesUnderMe)



x = float(input("Enter a common raise for everyone"))
Emp.showRaise(x)

todayDate = datetime.date(2018,2,5)
value = Emp.is_date_weekday(todayDate)
if (value==5 or value==6):
	print("It is a weekend")
else:
	print("It is a weekday")


x = int(input("Enter the type of employee 1. Developer 2. Manager"))
xName = input("Enter employee name")
xSalary = int(input("Enter salary"))
if(x==1):
	xLanguage = input("Enter the preferred language")
	myNewDev = developer(xName,xSalary,xLanguage)
	myNewDev.printMyDeveloper()
else:
	print("Enter the employees who work under you (Type quit to stop)")
	empList = []
	check = input()
	while(check!='quit'):
		empList.append(check)
		check = input()

	myNewManager = manager(xName,xSalary,empList)
	myNewManager.printMyManager()
