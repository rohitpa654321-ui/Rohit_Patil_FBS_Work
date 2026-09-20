### Abstact class and methood implementation

#     ↱  Module name  
#     |          ↱  Abstract Base Class
from abc import ABC, abstractmethod

class Animal (ABC):
    
    @abstractmethod          
    def sound(self):            # This method is abstactmethod (cannot define / write any code).
        # print('dog barks')    
        pass                    # using to avoid intendation Error.
    
    def eat(self):
        print('Animal is eating...')
    
class Dog(Animal):
    
    def sound(self):
        print('Dog barks.')


# object creation
# a1 = Animal()          # give TypeError because abstract class which is NOT instantiated
d1 = Dog()
# a1.eat()               #  Type error object (a1) NOT created
d1.eat()
d1.sound()