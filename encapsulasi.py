class Nama:
    def __init__(self, name, umur, nohp) -> None:
        self.__nama = name
        self.__umur = umur
        self.__hp = nohp

    # getter
    def GetName(self):
        return self.__nama

    def GetNohp(self):
        return self.__hp

    # setter
    def UbahNomer(self, UbahHp):
        self.__hp -= UbahHp

    def UbahNama(self, UbahNama):
        self.__nama = UbahNama


# Awal
Dodi = Nama("Dodi", 19, 3)
# print(Dodi.__dict__)
# Lanjut
# print(Dodi.__nama())
print(Dodi.GetName())
print(Dodi.GetNohp())
Dodi.UbahNomer(2)
Dodi.UbahNama("Saya")
print(Dodi.GetNohp())
print(Dodi.GetName())
