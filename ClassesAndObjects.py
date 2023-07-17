print('Classes and Objects')

class Dog:
    #This is the constructor of the class
    def __init__(self,name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + 'says: Bark!')

#Note that if you use legs like this anybody can change the default value using Dog.legs = 3 or something
#So the best way to define a fixed value is using a get method like so
class AnotherDog:
    _legs= 4
    def __init__(self,name):
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says: Bark!')

#Static and Instance Methods
class WordSet:
    def __init__(self):
        self.words = set()
    
    def addText(self, text):
        text = self.cleanText(text)
        for words in text.split():
            self.words.add(words)

    def cleanText(self, text):
        text = text.replace('!','').replace('.','!').replace('\'','')
        return text.lower()

#Inheritance
class Chihuahua(Dog):
    #Note that any attribute or method defined in the child`s class overwrites the parent`s class
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')

    #You can also create a method unique to this class
    def wagTail(self):
        print('Vigorous wagging!')

#When can also modify some built in classes like list()
class UniqueList(list):
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'
    
    def append(self, item):
        if item in self:
            return super().append(item) #calls the parent`s class

#Examples
print('\nClass => Dog')
myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)

print('\nWith Get Method')
myDog2 = AnotherDog('Rover')
print(myDog2.getLegs())

print('\nChanging the instance value instead of the class itself')
myDog3 = AnotherDog('Dog3')
myDog3._legs=3
print(myDog3.name)
print(myDog3.getLegs()) #Instance Variable
print(AnotherDog._legs) #Class Variable

print('\nClass => WordSet')
myWordSet = WordSet()
myWordSet.addText('Hi! I\'m trying to add sentences here!')
myWordSet.addText('Here is another line.')
print(myWordSet.words)

print('\nInheritance')
print('\nyou can change the childs method')
roxy = Chihuahua('Roxy')
roxy.speak()
myDog.speak()
roxy.wagTail()

myList= list()
secondList = UniqueList()
secondList.append(1)
secondList.append(1)
secondList.append(2)
print(secondList)
print(secondList.someProperty)