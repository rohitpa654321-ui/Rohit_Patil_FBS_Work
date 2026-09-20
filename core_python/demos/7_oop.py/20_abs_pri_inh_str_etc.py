from abc import ABC,abstractmethod
class Veichal(ABC):
    def __init__(self,name,color,price):
        self.__name=name
        self.__price=price
        self.__color=color
    @abstractmethod
    def brake(self):
        pass
    def __str__(self):
        return f"Name= {self.__name} \t Price={self.__price} \t Color={self.__color}"
class Car(Veichal):
    def __init__(self, name, color, price,sBEalt):
        super().__init__(name, color, price)
        self.__seatBelt=sBEalt
    def brake(self):
        print("This is the Drump brek of Car ")
    def __str__(self):
        return super().__str__() + f"\tSeat Belt={self.__seatBelt}"
v=Car("BMW (M-5)","grey",24000000,6)
v.brake()
print(v)
    