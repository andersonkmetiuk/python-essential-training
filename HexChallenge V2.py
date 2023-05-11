hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def HexToDec(hexNum):
#for version
    #Verify
    for char in hexNum:
        if char not in hexNumbers:
            return None

    resultDec=0
    i=len(hexNum)
    i-=1

    for char in hexNum:
        resultDec += (hexNumbers[char])*(16**i)
        #print('Hex num  = ',hexNumbers[char], '\n16**i = ',16**i)
        i-=1


    return resultDec

print('A = ', HexToDec('A')) #10
print('0 = ', HexToDec('0')) #0
print('1B = ', HexToDec('1B')) #27
print('3C0 = ', HexToDec('3C0')) #960
print('A6G = ', HexToDec('A6G')) #None
print('ZZTOP = ', HexToDec('ZZTOP')) #None