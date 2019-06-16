import os.path
#assumption in input is that only terminals will be at the end
text = open("leftfactinput.txt")
final = {}
varcount = 66

for line in text:

    line=line.replace("\n","")
    parts=line.split('->')
    lhs=parts[0].strip()
    rhs=parts[1]
    rhsparts=rhs.split("|")
    for count,x in enumerate(rhsparts):
        rhsparts[count]=rhsparts[count].strip()
    #print(lhs,rhs)
    rhsparts=rhs.split("|")

    for count,x in enumerate(rhsparts):
        rhsparts[count]=rhsparts[count].strip()
    #Everything till here is same as LR


    notcommon=[]
    common=""
    while(common==""):
        common=os.path.commonprefix(rhsparts)
        if(common==""):
            notcommon.append(rhsparts[-1])
            rhsparts=rhsparts[0:-1]

    print("Not common", notcommon)
    print("Rhs Parts" , rhsparts)
    print("Common ",common)
    commonlen=len(common)
    temp=[]
    final[lhs]=[notcommon,common+chr(varcount)]
    print("Final ",final)
    
    final[chr(varcount)]=[]
    for x in rhsparts:
        x=x[commonlen:]
        print(x)
        if(x==""):
            final[chr(varcount)].append("e")
        else:
            final[chr(varcount)].append(x)

    print("Final post loop ",final)
