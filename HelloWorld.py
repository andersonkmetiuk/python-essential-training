#First Program 6/04/2023
print('\t *First Program*\n\n\t Hello World \n')

#IF - a Identação é muito importante
a=True
b=True
c=True

if a:
    print('\n\t *If Structures* \n')
    print('A - its true')
    print('also print this')
    if b:
        print('B - both are true')
        if c:
            print('C - all three are true')
else:
    print('it is false')
print('always print this')

#LOOPS
print('\n\t *Loops* \n')

#FOR
print('For')
a=[1, 2, 3, 4, 5]
for item in a:
    print(item)

#WHILE
print('\nWhile')
a=0
while a<5:
    print(a)
    a = a + 1 

#FUNCTIONS
print('\n\t *Functions* \n')

#F1
def multiplyByThree(val):
    return 3*val

print('F1 =', multiplyByThree(5),'\n')

#F2
def multiplyVar(val1,val2):
    return val1*val2

print('F2 =', multiplyVar(3,5),'\n')

#F3

c=[1,2,3]

def appendFour(myList):
    myList.append(4)

appendFour(c)
print('F3 =', c,'\n')
