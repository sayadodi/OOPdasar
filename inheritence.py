class Lingkaran:
    def __init__(self, jari_jari) -> None:
        self.jariJari = jari_jari

    def getLuas(self):
        phi = 3.14
        if self.jariJari % 7 == 0:
            phi = 22 / 7
        return phi * self.jariJari * self.jariJari


class Tabung(Lingkaran):
    def __init__(self, jari_jari, tinggi) -> None:
        super().__init__(jari_jari)
        self.tinggi = tinggi

    def getVolume(self):
        return self.getLuas() * self.tinggi


ban = Lingkaran(10)
print("Luas ban Tersebut Adalah " + str(ban.getLuas()))

drum = Tabung(10, 20)
print("Luas Drum Adalah = " + drum.getLuas())
print("Volume drum adalah = " + drum.getVolume())
