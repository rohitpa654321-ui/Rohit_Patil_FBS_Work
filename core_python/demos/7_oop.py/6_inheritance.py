### Inheritance 

class Student:
    collegeName = 'K.K Wagh college'
    __studentcount = 0
    
    def __init__(self, RollNo, name, marks):
        self.rollno = RollNo
        self.name = name
        self.marks = marks
        Student.__studentcount +=1
    
    def getCount():
        return Student.__studentcount
        
    def getRollNo(self):
        return self.rollno
    def setRollNo(self,rn):
        self.rollno = rn
        
    def display(self):
        print(f'Roll No={self.rollno}\t Name={self.name}\t Marks={self.marks}')   
    
# This is Derived class inherites from Base class Student
class PlacedStudent(Student):
    
    def __init__(self, RollNo, name, marks, sal):
        super().__init__(RollNo,name,marks)
        self.sal = sal
        
    def display(self):
        super().display();print(f'Salary = {self.sal}')   

    
s1 = PlacedStudent(12, 'Ronit',98,140000)
s2 = Student(22,'ranjeet',60400)
s3 = Student(24,'ranjit', 55000)

print(Student.getCount())
s1.display()