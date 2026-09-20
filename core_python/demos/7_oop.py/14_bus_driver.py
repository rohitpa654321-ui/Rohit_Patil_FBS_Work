### Inheritance with bus driver...

class BusDriver:
    def __init__(self,nm,sal,bNo):
        self.__name = nm
        self.__sal = sal
        self.__bNo = bNo
# def display(self):
# print(f"Id={self ._ bNo}\t Name={self .__ name}\tsal={self ._ sal}")

    def __str__(self):
        return f"Id={self.__bNo}\t Name={self.__name}\tsal={self.__sal}"

class ElectricBDriver(BusDriver) :
    def __init__(self,nm,sal,bNo,exp):
        super() .__init__(nm, sal, bNo)
        self .__exp=exp
    def __str__(self):
        return super() .__str__()+f"\tExprience= {self.__exp}"


busD=BusDriver("sam",121222,321)
ebd=ElectricBDriver("VIkas",222222,"e34",4)
a=10
print(a)
print(busD)
print(ebd)
# busD.display()