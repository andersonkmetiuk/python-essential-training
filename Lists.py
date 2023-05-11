print("\t Basics \n")
myList = [1, 2, 3, 4, 5]
print(myList[3:])  # pos 3 em diante

print(myList[0:6:2])  # pos 0 a 6 com incrementos de 2

print(myList[0:6:3])  # pos 0 a 6 com incrementos de 3

print(myList[::2])  # lista toda com incrementos de 2

print("\n*----------------------*-------------------*-----------------------*\n")
print("\t Range Function \n")
# Range Function
for i in range(100):
    # print(i) #Printa os 100 valores
    print("Generated 100 values")
    break


myList = list(range(100))  # gera uma lista com 100 valores
print(myList[::5])  # lista toda com incrementos de 5
print(myList[::-5])  # lista decrescente em incrementos de 5

print("\n*----------------------*-------------------*-----------------------*\n")
print("\t Modify Lists \n")
# Modify Lists
modifyList = list(range(10))
print(modifyList)

modifyList.append(10)  # adiciona 10 na última posição
print(modifyList)

modifyList.insert(3, "a new value")  # adiciona a string na 3a pos
print(modifyList)

modifyList.remove(
    "a new value"
)  # remove a string da lista / *** se não existir vai dar erro
print(modifyList)

modifyList.pop()  # remove o último item
print(modifyList)

print("\n*----------------------*-------------------*-----------------------*\n")
print("\t Empty List \n")
# esvazia a lista
while len(modifyList):
    print(modifyList.pop())
print(modifyList)

print("\n*----------------------*-------------------*-----------------------*\n")
print("\t Copy Vs = \n")
# Diferença entre copy e igual
a = list(range(5))
b = a
c = a.copy()

a.append(6)
print("b = ", b)
print("copy c = ", c)

print("\n*----------------------*---------END---------*-----------------------*\n")
