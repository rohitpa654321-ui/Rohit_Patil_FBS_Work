### Employee class

class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        
    def __str__(self):
        return f'Employee id : {self.id} \t Employee name : {self.name} \t\t  Employee salary : {self.sal}'
