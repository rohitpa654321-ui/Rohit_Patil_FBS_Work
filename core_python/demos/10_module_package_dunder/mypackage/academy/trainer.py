class Trainer:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
    
    def __str__(self):
        return f"Id={self.id}\t Name={self.name} \t Sal={self.sal}"