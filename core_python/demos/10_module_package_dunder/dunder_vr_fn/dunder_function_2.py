### Dunder functions 

class Student:

# __init__()
    def __init__(self, name, age, players, numbers):
        self.name = name
        self.age = age
        self.players = players
        self.numbers = numbers
        
# __str__()
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"


# __len__()
    def __len__(self):
        return len(self.players)

# __getitem__()
    def __getitem__(self, index):
        return self.numbers[index]
    
# __setitem__()
    def __setitem__(self, index, value):
        self.numbers[index] = value
        
        
#  a.__add__(b)
#  a.__sub__(b)
#  a.__mul__(b)
#  a.__truediv__(b)
#  a.__eq__(b)
#  a.__lt__(b)
#  a.__gt__(b)
#  a.__floordiv__(b)
#  a.__mod__(b)
#  a.__pow__(b)
#  a.__contains__(b)
