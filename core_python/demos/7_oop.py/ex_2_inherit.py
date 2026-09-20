### example 4 of inheritance

class Satellite:

    def __init__(self, satId, name, orbit):
        self.satId = satId
        self.name = name
        self.orbit = orbit

    def getSatId(self):
        return self.satId
    def setSatId(self, sid):
        self.satId = sid

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getOrbit(self):
        return self.orbit
    def setOrbit(self, orbit):
        self.orbit = orbit

    def display(self):
        print(f"Satellite ID : {self.satId} \t Name : {self.name} \t Orbit : {self.orbit}")


class WeatherSatellite(Satellite):

    def __init__(self, satId, name, orbit, coverage):
        super().__init__(satId, name, orbit)
        self.coverage = coverage

    def display(self):
        print(f"Coverage : {self.coverage}")
        return super().display()


s1 = WeatherSatellite(12.01, "INSAT-3D", "Geo", "India")
s2 = Satellite(12.013, "GSAT-7", "LEO")

WeatherSatellite.display(s1)
print()
Satellite.display(s2)