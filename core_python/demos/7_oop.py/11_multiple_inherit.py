### Type of Inheritance 3 : Multiple inheritance

#      ------------                ------------
#     | Electronic |  (Base)      | Mechanical |  (Base)
#      ------------                ------------
#                   \            /
#                    \          /
#                      ---------
#                     |   Dog   |  (Derived)
#                      ---------


class Mec :
    print('Mec')
    def display(self):
        print('I am from Mec')
        
class Ent:
    def __init__(self, lab):
        self.lab = lab
        print('ENTC')
    def display(self):
        print('I am from ENTC')

class Mectronix(Mec,Ent):
    def __init__(self,abc,lab):
        super().__init__(lab)
        self.abc = abc
        print(self.abc)
        
m = Mectronix(lab = 'Vivekanand Lab', abc = 'Yes')
m.display
print(m.lab)