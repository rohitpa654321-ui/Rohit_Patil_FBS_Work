### Static method : @staticmethod
# Class level method independent of object creation and data

class Student:
    collegeName = 'K.K Wagh college'
    
    @staticmethod
    def greet():
        print(f'Welcome to {Student.collegeName}')
    def __int__(self, RollNo, name, marks):
        self.nmae = name
        self.rollno = RollNo
        self.marks = marks
        
    def getRollNo(self):
        return self.rollno
    def setRollNo(self,rn):
        self.rollno = rn
    
    
Student.greet()        # call using class name not depends on object creation.
# s1 = Student()             # object created.
# s1.greet()           # call using object name also but don't call using object keep it independent.
