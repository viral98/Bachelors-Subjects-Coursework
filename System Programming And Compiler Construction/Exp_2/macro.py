MDT = []
MNT = {}
MDTC = 0
ALA = []
def processLine(line):
	label = None
	if ':' in line:
		label = line.split(':')[0]
		line = line.split(':')[1:]
	line = line.split(' ')
	if len(line) == 1:
		return line[0], None
	elif len(line) == 2:
		return line[0], [line[1]]
	elif len(line) == 3:
		return line[1], [line[0]]+line[2].split(',')
	else:
		return None
def pass1(inp, out):
	global ALA
	line = inp.readline()
	if line == '':
		return None
	if line[-1] == '\n':
		line = line[:-1]
	if line != 'MACRO':
		out.write(line + '\n')
		if line == 'END':
			out.close()
			print('PROCESSING OVER.')
			return
		pass1(inp, out)
	else:
		line = inp.readline()[:-1]
		macro_name, args = processLine(line)
		global MDTC, MNTC
		MNT[macro_name] = MDTC
		if args:
			ALA = args[:]
		MDT.append(line)
		MDTC = MDTC + 1		
		while True:
			line = inp.readline()[:-1]
			for arg in args:
				while arg in line:
					i = line.index(arg)
					line = line[:i] + '#' + str(ALA.index(arg)) + line[i+len(arg):]
			MDT.append(line)
			MDTC = MDTC + 1
			if line == 'MEND':
				pass1(inp, out)
				return
inp = input('Enter the input file: ')
out = input('Enter the output file: ')
inp,out = open(inp, 'r'),open(out,'w')
pass1(inp, out)
print('MDT:', MDT)
print('MNT:', MNT)
print('ALA:', ALA)
inp.close()
out.close()
