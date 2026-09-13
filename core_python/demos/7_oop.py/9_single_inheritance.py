### Type of Inheritance 1 : Single level inheritance
#               --------
#              | Animal |   (Base)
#               --------
#                  | 
#                  | inherited 
#               --------
#              |   Dog  |  (Derived)
#               --------

class Animal:
    def __init__(self, name, color, age):
        self. name = name
        self.color = color 
        self.age = age
    
    def display(self):
        print(f'Name = {self.name} \t Color = {self.color} \t Age = {self.age}')
        

class Dog(Animal):
    def __init__(self,name, color, age):
        print('Dog :', end = '\t')
        super().__init__(name,color,age)
    

d1 = Dog('Rambo', 'brown-black', 5)
d1.display()
