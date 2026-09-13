### creating Student class
# Static variable


class Student:
    
    college_name = 'K.K Wagh college'      # Static variable (constant or same for all instance of class.)
    
    def __init__(self, RollNo, name, marks):
        self.rollno = RollNo
        self.name = name
        self.marks = marks
        
    def getRollNo(self):
        return self.rollno
    def setRollNo(self,rn):
        self.rollno = rn
        
    def getName(self):
        return self.name
    def setName(self,nm):
        self.name = nm
    
    def getmarks(self):
        return self.marks
    def setmarks(self,mk):
        self.marks = mk
    
    def display(self):
        print(f"Roll no= {self.rollno} \t Name= {self.name} \nMarks={self.marks} \t Collage Name={Student.college_name} ")
        

s1=Student(101,"Virat",36)
s2=Student(101,"Sachi",45)
s1.display()
# print(s1.college_name)
print(Student.college_name)
Student.college_name = 'G.H Raisoni college'
print(Student.college_name)