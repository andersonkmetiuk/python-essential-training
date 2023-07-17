print('Classes and Objects')

class Dog:
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
        print(self.name + 'says: Bark!')

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

