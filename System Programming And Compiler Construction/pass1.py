f = open("code.txt")
data = f.readlines()
pot_list = ["Start","Using","DC","DS","End"]
symbol = []
POT = []
MOT = []
Lit = []
lc = 0
for i in data:
	i = i[:-1]
	temp = i.split(" ")
	print(temp)
	if temp[0]!="Null":
		p = []
	p.append(temmp[0])
	p.append(lc)
	symbol.append(p)
	if temp