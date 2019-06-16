print("Input the data bits")
a2 = int(input("Enter a2"))
a4 = int(input("Enter a4"))
a5 = int(input("Enter a5"))
a6 = int(input("Enter a6"))
a0 = a2 ^ a4 ^ a6
a1 = a2 ^ a5 ^ a6
a3 = a4 ^ a5 ^ a6
print(a0,a1,a2,a3,a4,a5,a6)

print("Enter recieved bits")
d0 = int(input("Enter d0"))
d1 = int(input("Enter d1"))
d2 = int(input("Enter d2"))
d3 = int(input("Enter d3"))
d4 = int(input("Enter d4"))
d5 = int(input("Enter d5"))
d6 = int(input("Enter d6"))

c1 = d0 ^ d2 ^ d4 ^ d6
c2 = d1 ^ d2 ^ d5 ^ d6
c3 = d3 ^ d4 ^ d5 ^ d6

c = c3*4 + c2*2 + c1
if c==0:
    print("No errors")
