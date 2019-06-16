class Error(Exception):
	pass
class ValueTooSmall(Error):
	pass
class ValueTooBig(Error):
	pass

baseNumber = 23
while (True):
	try:
		print("")
		value = int(input("Try Entering a value"))
		if (value > baseNumber):
			raise ValueTooBig
		elif (value < baseNumber):
			raise ValueTooSmall
	except ValueTooSmall:
		print("Try entering a bigger number")
	except ValueTooBig:
		print("Try entering a smaller value")
	else:
		print("purrrrrrfect")