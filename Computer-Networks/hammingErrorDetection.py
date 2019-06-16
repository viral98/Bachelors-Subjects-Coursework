
def checkForErrorBits(key, lim, code):
    index = key
    p = key - 1
    q = 1
    j = key
    bit = 0
    while(j < lim):
        if(p == 0):
            j += q
            p = q
            q = 0
        # Dar mat... This is just to find the exor of that bit with the next bit
        bit = (int(code[j]) != bit) * 1
        j += 1
        p -= 1
        q += 1
    if(int(code[index - 1]) == bit):
        return '0'
    else:
        return '1'


code = input(">Enter the hamming code received: ")
codeLen = len(code)
parityBits = {}
k = 0

for i in range(1, codeLen):
    if(i == pow(2, k)):
        parityBits[i] = code[i - 1]
        k += 1

binaryErrorCode = ""
for key in parityBits:
    parityBits[key] = checkForErrorBits(key, codeLen, code)
    binaryErrorCode = binaryErrorCode + parityBits[key]

errorIndex = int(binaryErrorCode, 2)

if(errorIndex == 0):
    print("No Errors Detected.")
else:
    correctedCode = code[0:errorIndex - 1] + \
        str((not int(code[errorIndex - 1])) * 1) + code[errorIndex:]
    print("In code: " + code + "\nError Detected at Index " + str(errorIndex))
    print("Corrected Code: " + correctedCode)
