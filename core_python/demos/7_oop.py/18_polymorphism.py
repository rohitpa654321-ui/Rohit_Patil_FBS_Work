# Polymorphism : as same message given to genralized things for same behavior, but implemented differently...

# Here calSal is same message but implemented differently by different object...

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
        finalSal = self.__sal
        print(f'Emp salary= {finalSal}')
    def __str__(self):
        return f'Id={self.__id}\t Name={self .__name}\tsal={self .__sal}'
    def display(self):
        print(f"ID={self.__id} \t name= {self.__name} \t sal={self.__sal}")
# Emp class Ends Here ....

class Hr(Emp):
    def __init__(self, id, name, sal, com):
        super().__init__(id,name,sal)
        self.__com = com
    def getCom(self):
        return self.__com
    def setCom(self,com):
        self.__com=com
    def getName(self):
        return self.__name
    def setName(self,nm):
        self.__name = nm
    def display(self):
        print(f"Com={self.__com}",end = ' ')
        return super().display()
    def calSal(self):                               # if calSal method remove from HR class then call from Base class
        finalSal=self.getSal() + self.__com 
        print(f'Final salary of HR is {finalSal}')             
    def __str__(self):
        return super().__str__() + f'commission  = {self.__com}'
    
    def __del__(self):
        print('Distructor is called...')   # automatically call after operation done
    
# main Task -- >
h1=Hr(121,"Smriti",212121,34300)
e1=Emp(101,"RajVardhan",121222)
e2=Emp(102,"Tanuja",9089)
e3=Emp(103,"Vīdya",33332)
e4=Emp(104,"Aadinth",7890)
# print(e3.getSal())
# e2.setSal(23413)
# e2.display()
# h1.display() 
h1.calSal()