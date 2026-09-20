### using dunder function add to user define...

class Time:
    def __init__(self,Hr,Min,Sec):
        self.Hr = Hr
        self.Min = Min
        self.Sec = Sec
    def __add__(self, other):
        tsec = 0
        tmin = 0
        thr = 0
        tsec = (self.Sec +other.Sec)%60
        rem = (self.Sec +other.Sec) // 60
        tmin = (self.Min + other.Min) % 60
        rem = (self.Min + other.Min) // 60
        thr = (self.Hr + other.Hr)
        return Time(thr ,tmin , tsec)
       
        # hR = self.Hr + other.Hr
        # mIn=self.Min+other.Min
        # sEc=self.Sec + other.Sec
        # return Time(hR,mIn,sEc)
    
    def __str__(self):
        return f'Time = {self.Hr} : {self.Min} : {self.Sec}'
    
t1 = Time(1,2,33)
# print(t1)

t2 = Time(2,21,43)
print(t1 + t2)

