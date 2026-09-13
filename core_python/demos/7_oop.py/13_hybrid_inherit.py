# ## Type of Inheritance 5 : Hierarchical inheritance

#                      ---------
#                     | College |   (Base)
#                      ---------
#                         | 
#                         | inherited 
#                 ------------------
#                |  Course / Degree |  (Derived)
#                 ------------------
#                 /               \
#                /                 \
#      ------------                ------------
#     | Electronic |  (Derived)   | Mechanical |  (Derived)
#      ------------                ------------
#                  \              /
#                   \            /
#                   --------------
#                  |  Mechatronic |  (Derived)
#                   --------------


class College:
    college_name = 'K.K Wagh college of Engineering'
    college_id = 121
    
    def display(self):
        print(f'collge name = {self.college_name} \t college id = {self.college_id }')

class Course(College):
    course_name = 'B.Tech'
    course_year = 4
    def display(self):
        super().display()
        print(f'course : {self.course_name} \t year : {self.course_year}')
    
class Electronic(Course):
    def __init__(self):
        self.branch_name = 'Electronic'
        self.b_code = 'UNEC201'
        self.subjecte1 = 'E1'
        self.subjecte2 = 'E2'
    def display(self):
        super().display()
        print(f'branch : {self.branch_name} \t code : {self.b_code} \nsubject : {self.subjecte1} ,\t {self.subjecte2}')

class Mechanical(Course):
    def __init__(self):
        self.branch_name = 'Mechanical'
        self.b_code = 'UNME203'
        self.subjectm1 = 'M1'
        self.subjectm2 = 'M2'
    def display(self):
            super().display()
            print(f'branch : {self.branch_name} \t code : {self.b_code} \nsubject : {self.subjectm1} ,\t {self.subjectm2}')
    
    
class Mechatronic(Mechanical, Electronic):
    def __init__(self):
        Mechanical.__init__(self)
        Electronic.__init__(self)
        self.sub1 = self.subjectm1
        self.sub2 = self.subjecte1
        self.branch_name = 'Mechatronic'
        self.b_code = 'UNMCT101'
    def display(self):
        Course.display(self)
        print(f'branch : {self.branch_name} \t code : {self.b_code} \nsubject : {self.sub1} ,\t {self.sub2}')

                

# cl1 = College()
# cl1.display()
# c2 = Course()
# c2.display()
# el1 = Electronic()
# el1.display()
# me1 = Mechanical()
# me1.display()
mt1 = Mechatronic()
mt1.display()