### Creating class
# common attributes
# constructor : __init__(self):
# first parameter always self.
# method display() define (function)
# creating objeect with parameters
# calling methods from class and access values

class Emp:
    comp_name = 'GPS'
    depart = 'IT'
    
    def __init__(self, id, name, sal ):
        self.name = name
        self.id = id
        self.sal = sal
    
    def display(self):
        print((f'Company = {self.comp_name} \t\t Department = {self.depart} \nID = {self.name} \t Name = {self.name} \n Sal = {self.sal} '))
        
        
e1 = Emp(101,"Rohit patil", 1400000)
e1.display()   # If I use print() here it will return in last None, print in print function calls
