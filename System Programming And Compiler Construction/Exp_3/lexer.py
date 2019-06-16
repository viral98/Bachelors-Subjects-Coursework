import string
OPERATORS = ['+', '-', '*', '/', '%', '^', '=', '(', ')']
KEYWORDS = ['int', 'float', 'string', 'with', 'for', 'in']
SYMBOLS = [",", ';', ':']
def lexer(file):
	identifiers,constants = [],[]
	with open(file, 'r') as f:
		for x in f:
			line = x.strip()
			i,j,n = 0,0,len(line)
			str_constant = False
			while j < n:

				if line[j] == '"':
					if str_constant:
						token = line[i:j+1]
						i = j + 1
						identifyToken(token)
					str_constant = not str_constant
					j = j + 1

				elif str_constant:
					j = j + 1
					continue

				elif line[j] in OPERATORS:
					if i == j:
						print('OPERATOR:', line[i])
						i += 1
						j = i
					else:
						identifyToken(line[i:j])
						i = j

				elif line[j] in SYMBOLS:
					if i == j:
						print('SYMBOL:', line[i])
						i += 1
						j = i
					else:
						identifyToken(line[i:j])
						i = j

				elif line[j] in string.whitespace:
					identifyToken(line[i:j])
					i = j + 1
					j = i

				else:
					j = j + 1

			identifyToken(line[i:j])
			
def identifyToken(token):
	token = token.strip()
	if len(token) > 0:
		if token[0] == token[-1] and token[0] == '"':
			print('STRING CONSTANT:', token)
		elif token.isnumeric():
			print('NUMBER CONSTANT:', token)
		elif token in KEYWORDS:
			print('KEYWORD:', token)
		else:
			print('VARIABLE:', token)
file = input('Enter the name of the file: ')
lexer(file)
"""
input.txt
int a, b1, c
a =3
b1 = "abc"
c = a + b;
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEXICAL_ANALYSER$ python3 lexer.py 
Enter the name of the file: input.txt
KEYWORD: int
VARIABLE: a
SYMBOL: ,
VARIABLE: b1
SYMBOL: ,
VARIABLE: c
VARIABLE: a
OPERATOR: =
NUMBER CONSTANT: 3
VARIABLE: b1
OPERATOR: =
STRING CONSTANT: "abc"
VARIABLE: c
OPERATOR: =
VARIABLE: a
OPERATOR: +
VARIABLE: b
SYMBOL: ;
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEXICAL_ANALYSER$
"""
