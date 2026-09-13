### Type of Inheritance 4 : Hierarchical inheritance

#                   --------
#                  | Animal |   (Base)
#                   --------
#                 /          \
#                /            \
#      ---------                ---------
#     |   Dog   |  (Derived)   |   Cat   |  (Derived)
#      ---------                ---------

class Animal:
    def __init__(self, name, color, age):
        self. name = name
        self.color = color 
        self.age = age
    
    def display(self):
        print(f'{type(self).__name__} :', end = '\t')
        # print(f'{self.__class__.__name__} :', end = '\t')
        print(f'Name = {self.name} \t Color = {self.color} \t Age = {self.age}')
        

class Dog(Animal):
    def __init__(self,name, color, age):
        super().__init__(name,color,age)

class Cat(Animal):
    def __init__(self, name, color, age):
        super().__init__(name, color, age)
        
        

d1 = Dog('Rambo', 'brown-black', 5)
d1.display()
c1 = Cat('Minu', 'brown-white', 3)
c1.display()