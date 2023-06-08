class Nama:
    jumlah = 0

    def __init__(self, nama, umur, hoby) -> None:
        self.name = nama
        self.umur = umur
        self.hobi = hoby

        # Variable instance private
        self.__private = "Private"
        # Variable instance protected
        self._protected = "protected"


nama1 = Nama("Dodi", 19, "Memancing")
print(nama1.__dict__)
print(nama1._protected)
