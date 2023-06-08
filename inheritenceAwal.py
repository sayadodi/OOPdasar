class Orang:
    def __init__(self, nama, asal) -> None:
        self.nama = nama
        self.asal = asal

    def info(self):
        print("Perkenalkan Nama Saya", self.nama, "Saya Berasal Dari", self.asal)


class Pelajar(Orang):
    def __init__(self, nama, asal, tempatSekolah) -> None:
        super().__init__(nama, asal)
        self.tmpsekolah = tempatSekolah


class Perkerja(Orang):
    def __init__(self, nama, asal, tempatKerja) -> None:
        super().__init__(nama, asal)
        self.tmpKerja = tempatKerja


Dodi = Orang("Dodi", "Alastengah")
Rina = Pelajar("Rina", "Sumberan", "Smkn 2 Kraksaan")
Mifta = Perkerja("Miftah", "Pandean", "Pt PJB Paiton")

Dodi.info()
Rina.info()
print("Asal Sekolah Saya Adalah", Rina.tmpsekolah)
Mifta.info()
print("Asal Perkerjan Saya Adalah", Mifta.tmpKerja)
