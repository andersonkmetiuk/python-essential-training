hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def HexToDec(hexNum):
#while version
    #Verify
    for char in hexNum:
        if char not in hexNumbers:
            return None
        
    a=len(hexNum)
    resultDec=0
    b=0
    c=a-1

    while a>0:
        resultDec += (hexNumbers[hexNum[c]])*(16**b)
        #print('Hex num ',b,' = ',hexNum[c], '\n16**b = ',16**b)
        a-=1
        b+=1
        c-=1

    return resultDec

print('A = ', HexToDec('A')) #10
print('0 = ', HexToDec('0')) #0
print('1B = ', HexToDec('1B')) #27
print('3C0 = ', HexToDec('3C0')) #960
print('A6G = ', HexToDec('A6G')) #None
print('ZZTOP = ', HexToDec('ZZTOP')) #None