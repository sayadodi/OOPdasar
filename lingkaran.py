class Lingkaran:
    def __init__(self, radius=0):
        self.radius = radius

    def setData(self, radius):  ##Overriding
        self.radius = radius

    def getLuas(self):  ##Overloading
        return 3.14 * self.radius * self.radius

    def info(self):
        print(f"Radius = {self.radius}")
        print(f"Luas = {self.getLuas()}")


class Tabung(Lingkaran):
    def __init__(self, radius=0, height=0):
        super().__init__(radius)
        self.height = height

    def setData(self, radius, height):
        super().setData(radius)
        self.height = height

    def getLuas(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height)

    def getVolume(self):
        return 3.14 * self.radius * self.radius * self.height

    def info(self):
        print(f"Radius \t\t {self.radius}")
        print(f"Luas Permukaan \t {self.getLuas()}")
        print(f"Tinggi \t {self.height}")
        print(f"Volume \t\t {self.getVolume()}")


ling = Lingkaran()
ling.info()
ling.setData(10)
ling.info()

tabung = Tabung()
tabung.info()
tabung.setData(10, 20)
tabung.info()
