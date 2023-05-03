#Factorial Challenge
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

def factorial(num):
    if isinstance(num,float) or isinstance(num,str): #floats or strings
        return None
    if num == 0:
        return 1
    if num >= 1:
        return num * factorial(num-1)
    else:
        return None

#Test Cases
print('5! = ', factorial(5), '\n') #120
print('6! = ', factorial(6), '\n') #720
print('0! = ', factorial(0), '\n') #1
print('-2! = ', factorial(-2), '\n') #return None
print('1.2! = ', factorial(1.2), '\n') #return None
print('spam! = ', factorial('spam spam spam'), '\n')  #return None
print('1! = ', factorial(1), '\n') #1

