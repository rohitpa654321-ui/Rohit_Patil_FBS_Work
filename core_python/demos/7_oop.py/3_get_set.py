# Getter : used method returning or access data or value from class
# Setter : used method as update(set) or change values

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
        print(f"Emp salary= {self.sal}")
    def display(self):
        print(f"ID={self.id} \t name= {self.name} \t sal={self.sal}")
    # Emp class Ends here...

# Main Task --->

e1=Emp(101,"RajVardhan",121222)
e2=Emp(102,"Tanuja",9089)
e3=Emp(103,"Vidya",33332)
e4=Emp(104,"Rohit",7890)
print(e3.getSal())
e2.setSal(23413)
e2.display()
print(e4.getName())
e4.setName("Rohit")
print(e4.getName())