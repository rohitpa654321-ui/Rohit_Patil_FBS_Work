### 

from abc import ABC, abstractmethod

class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id
    def getName(self):
        return self.name
    def setName(self,nm):
        self.name=nm
    def getSal(self):
        return self.sal
    def setSal(self,sal):
        self.sal=sal   
    def calSal(self):
        print(f'Emp salary= {self.sal}')
    def display(self):
        print(f"ID={self.id} \t name= {self.name} \t sal={self.sal}")
# Emp class Ends Here ....

class Hr(Emp):
    def __init__(self, id, name, sal, com):
        self.com = com 
    def getCom(self):
        return self.com
    def setCom(self,com):
        self.com=com
    def display(self):
        return super().display()+ f'\tCom={self.com}'



# main Task -- >
h1=Hr(121,"Smriti",212121,34300)
e1=Emp(101,"RajVardhan",121222)
e2=Emp(102,"Tanuja",9089)
e3=Emp(103,"Vīdya",33332)
e4=Emp(104,"Aadinth",7890)
print(e3.getSal())
e2.setSal(23413)
e2.display()