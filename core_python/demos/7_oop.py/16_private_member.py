### private members..
# Declare using double underscore (__).
# ex :  self.__variable = value  # define

class Emp:
    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal
        
    def getId(self):
        return self.__id   

    def setId(self,id):
        self.__id=id

    def getName(self):
        return self.__name   

    def setName(self,nm):
        self.__name=nm

    def getSal(self):
        return self.__sal

    def setSal(self,sal):
        self.__sal=sal

    def calSal(self):
        print(f'emp salary={self.__sal}')         

    def display(self):
        print(f'Id={self.__id}\t name={self.__name}\t sal={self.__sal}')   

# objects
e1 = Emp(101,'sachin',50000)
e2 = Emp(102,'virat',50000)
e3 = Emp(103,'rohan',50000)
e4 = Emp(104,'karan',50000)

print(e1.getId())
e2.setSal(60000)
e2.display()
print(e4.getName())

e4.setName('rohit')
e4.display()
# print(e4.__name)      # Give attributeError, Because not directly access if private member.
