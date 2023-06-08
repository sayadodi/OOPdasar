class Persegi:
    def __init__(self, panjang=0):
        self.panjang = panjang

    def setPoint(self, panjang=0):  ##Overriding
        self.panjang = panjang

    def ambilLuas(self):  ##Overloading
        return self.panjang**2

    def info(self):
        print(f"Panjang = {self.panjang}")
        print(f"Luas = {self.ambilLuas()}")


class Persegi_panjang(Persegi):
    def __init__(self, panjang=0, lebar=0) -> None:
        self.panjang = panjang
        self.lebar = lebar

    def setPoint(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def ambilLuas(self):
        return self.panjang * self.lebar

    def info(self):
        print(f"Panjang \t {self.panjang}")
        print(f"Lebar \t {self.lebar}")

