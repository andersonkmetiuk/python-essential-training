import math

def performOperation(num1,num2,operation='sum'): #sum is a default value for operation argument
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1*num2

def opMathLib(*args,operation='sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(args)

print('Functions')
print('performOperation')
print('Sum')
print(performOperation(2,3,'sum'))
print(performOperation(2,3))
print('Multiply')
print(performOperation(2,3,'multiply'))
print('opMathLib')
print(opMathLib(1,2,3,6,7,8,operation='sum'))


#To return local variables you use locals() function
# and to return global variables you could use globals()
# With Lambda functions you can write simple one line functions like (lambda x: x+3)(5) and it will return the result like:
print('Lambda Function')
print((lambda x: x+3)(5))