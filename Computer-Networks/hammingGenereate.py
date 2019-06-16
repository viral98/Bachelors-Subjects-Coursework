
# To find value of Parity bits.
# Has logic to find the sequence of indices to be xored for getting the parity bit value.


def hamBit(i, lim, hamming):
    p = i - 1
    q = 1
    j = i
    bit = 0
    while(j < lim):
        if(p == 0):
            j += q
            p = q
            q = 0
        # Dar mat... This is just to find the exor of that bit with the next bit
        bit = (int(hamming[j]) != bit) * 1
        j += 1
        p -= 1
        q += 1
    return str(bit)


data = input(">Enter the data bits: ")
dataLen = len(data)
hamming = ""
i = 0
j = 0
k = 0

# To find no of parity bits required.
while(True):
    if(pow(2, i) >= dataLen + i + 1):
        addBits = i
        break
    i += 1

# To place 0s in place of Parity Bits
for i in range(1, addBits + dataLen + 1):
    if(i == pow(2, k)):
        hamming = hamming + '0'
        k += 1
    else:
        hamming = hamming + data[j]
        j += 1

j = 0
k = 0

# To place right values of Parity Bits in its place
for i in range(1, addBits + dataLen + 1):
    if(i == pow(2, k)):
        # Dar mat... This is just to replace the value of charecter at index 'i'
        hamming = hamming[0:i] + hamBit(i, dataLen, hamming) + hamming[i + 1:]

print("Hamming Code for " + data + " is " + hamming)
