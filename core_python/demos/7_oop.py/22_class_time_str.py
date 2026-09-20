### class to print time with using Str method...

class Time:
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec
        
    def __str__(self):
        return f'Time = {self.hr}:{self.min}:{self.sec}'
    
t1 = Time(3,21,43)

print(t1.__str__())
