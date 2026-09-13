### creating methods getter and setter 
# getter as returning value (read or get) of attribute.
# get_attribute(self):

# setter as method used to update(set) vaule of attribute.
# provide controlled modification of data (helps to maintain data integrity).
# set_attrinbute(self, value):


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
        print(f'emp salary={self.sal}')         

    def display(self):
        print(f'Id={self.id}\t name={self.name}\t sal={self.sal}')   

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
e4.setSal(120000)
e4.display()

