###  exaple 3 of inheritance

class Farmer:
    def __init__(self, farmerId, name, land):
        self.farmerId = farmerId
        self.name = name
        self.land = land

    def display(self):
        print(f"Farmer ID : {self.farmerId} \t Name : {self.name} \t Land : {self.land} Acres")


class OrganicFarmer(Farmer):
    def __init__(self, farmerId, name, land, certificate):
        super().__init__(farmerId, name, land)
        self.certificate = certificate

    def display(self):
        print(f"Certificate : {self.certificate}")
        super().display()


f = OrganicFarmer(200521,"Rajan", 8, "India Organic")
f.display()