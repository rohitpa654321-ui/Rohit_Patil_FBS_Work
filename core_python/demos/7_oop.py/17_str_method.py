### __str__() method :  display object in readable formate --> string representattion 
# called automatically when use print(object)  or  str(object)  .

class BusDriver:
    def __init__(self, name, sal, id):
        self.__name = name
        self.__sal = sal
        self.__id = id
    
    def display(self):
        print(f"Id={self.__id}\t Name={self .__name}\tsal={self .__sal}")
        
    def __str__(self):
        return f'Id={self.__id}\t Name={self .__name}\tsal={self .__sal}'
    
class ElecctricBDriver(BusDriver):
    def __init__(self,id, nm , sal, exp):
        super().__init__(id, nm, sal)
        self.__exp = exp
    def __str__(self):
        return super().__str__() + f'\t Exprience = {self.__exp}'
    
     
busD = BusDriver('Mandip',25000,1990)
busD.display()                          # using method display
print(busD)                             # using object name
print(str(busD))                        # using str(objectName) by printing

ebd = ElecctricBDriver('Dann', 24000, 1312, '3 years' )
print(ebd)