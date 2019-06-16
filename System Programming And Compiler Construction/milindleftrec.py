text=open("leftrec.txt")
final={}
varcount=66 #to use for new variables
for line in text:
    print(line)

    ##Go through the code, convert it into chunks
    line=line.replace("\n","")
    parts=line.split('->')
    lhs=parts[0].strip()
    rhs=parts[1]
    rhsparts=rhs.split("|")
    for count,x in enumerate(rhsparts):
        rhsparts[count]=rhsparts[count].strip()

    ##Go through chunks and make sure, RHS!=LHS
    final[lhs]=[]
    final[chr(varcount)]=[]
    for part in rhsparts:
        if part.find(lhs)==0:
            final[chr(varcount)].append(part[1:]+chr(varcount))
        else:
            final[lhs].append(part+chr(varcount))
    final[chr(varcount)].append("e")
    varcount=varcount+1

print(final)
