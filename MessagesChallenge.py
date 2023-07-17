"""
Create a class "SaveMessages" that extends the Messenger class that does the following things:

- Add any messages it receives to a list, along with the time the message was received
- Use the provided "getCurrentTime" function so that the received message time is a string
- Contains a method called "printMessages" that prints all collected messages when it's called.

You might also consider clearing the message list when "printMessages" is called. 
"""
from datetime import datetime


def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        # Must be implemented by extending classes
        pass


class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []
        
    def receive(self, message):
        self.messages.append({'message': message, 'time': getCurrentTime()})
        
    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        self.messages = []

# Run this cell after you've written your solution
listener = SaveMessages()

sender = Messenger([listener])

sender.send('Hello, there! This is the first message')

# Run this cell after you've written your solution
sender.send('Oh hi! This is the second message!')

# Run this cell after you've written your solution
sender.send('Hola! This is the third and final message!')

listener.printMessages()