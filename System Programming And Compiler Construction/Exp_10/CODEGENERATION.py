import re
reg,output_code = {},[]
def allocateRegister(op):
    if op in reg.values():
        for key, value in reg.items():
            if op == value:
                return key
    else:
        reg_name = "R" + str(len(reg)) 
        reg[reg_name] = op 
        output_code.append("MOV "+op+","+reg_name)
        return reg_name
"""HARDCODE INPUT ELSE KEEP THE BLUE COMMENT LINE AND REMOVE THE NEXT --AQID KHATKHATAY"""
input_code = list(line.strip() for line in open("cginput.txt"))
#input_code=['t=a-b', 'u=a-c', 'v=t+u', 'd=v+u']
for line in input_code:
    line = re.split("([\=\+\-\*\/])", line) 
    LHS, eq, op1, op, op2 = line
    op1,op2= allocateRegister(op1),allocateRegister(op2)
    if op.strip() == "+":
        output_line = "ADD "+str(op1)+","+str(op2)
        reg[op2] = LHS  
    elif op.strip() == "-":
        output_line = "SUB " + str(op1) + "," + str(op2)
        reg[op2] = LHS
    elif op.strip() == "*":
        output_line = "MUL " + op1 + "," + op2
        reg[op2] = LHS
    elif op.strip() == "/":
        output_line = "DIV " + op1 + "," + op2
        registers[op2] = LHS
    output_code.append(output_line)
for line in output_code:
	print(line)
"""cginput.txt
t=a-b
u=a-c
v=t+u
d=v+u
"""
