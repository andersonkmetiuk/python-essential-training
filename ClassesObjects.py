#Classes and Objects 6/04/2023

#Uppercase letters for Classes
class Dog:
    #initialization
    def __init__(self,name):
        self.name =  name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

#Create instances
my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()

