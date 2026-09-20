### Access specifiers : control the visibility & accessibility of class members
# Public : self.variable = value
# Protected : self._variable = value
# Private : self.__variable = value

class Student:
    def __init__(self, roll , name, marks):
        self.rollNo = roll     # Public
        self._name = name      # Protected
        self.__marks = marks   # Private
    def display(self):
        print(f'Roll No = {self.rollNo} \t Name = {self._name} \t Marks = {self.__marks}',end ='\t')
        
class  Enstudent(Student):
    def __init__(self,roll,name,marks,cgpa):
        super().__init__(roll,name,marks)
        self.__cgpa = cgpa
    
    def display(self):
        super().display()
        print(f'CGPA = {self.__cgpa}')
        
        
        
e1 = Enstudent(22, 'Rohit', 87, 9.3 )
e1.display()                              # all members accessed by method
print(e1.rollNo)
print(e1._name)
# print(e1.__marks)     # will give AttributeError, because it is private can't be access directly
