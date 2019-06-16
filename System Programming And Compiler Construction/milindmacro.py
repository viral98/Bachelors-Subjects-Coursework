f_input= open("macro_input.txt")
flag=0
mdt = []
mnt= []
pala = []
cala = []
mdtindex=0
for line in f_input:
    if(flag==1):
        mdt.append(line)
    if("MEND" in line):
        flag=0
    split=line.split(" ")

    for count,x in enumerate(split):
        if(x!='MACRO'):
            break
        else:
            mnt.append(split[count+1])
            argsplit=split[count+2].split(",")
            print(argsplit)
            for y in argsplit:
                pala.append([y,split[count+1]])
            flag=1

print(mnt)
print(pala)
print(mdt)
