class nama:
    jumla_nama = 0

    def __init__(self, inputName, inputUmur, inputHoby) -> None:
        self.nama = inputName
        self.umur = inputUmur
        self.hobi = inputHoby
        nama.jumla_nama += 1

    # methods tanpa returs
    def siapa(self):
        print("Namaku adalah " + self.nama)

    # methods dengan argumen
    def tambahUmur(self, tambah):
        self.umur += tambah

    # methods dengan return
    def gethoby(self):
        return self.hobi

    def getnama(self):
        return self.nama


nama1 = nama("Dodi", 19, "Memancing")
nama2 = nama("Tegar", 20, "Main Bola")

# nama1.siapa()
nama1.tambahUmur(10)
print(nama1.getnama())
print(nama1.gethoby())
print("Umur saya " + str(nama1.umur))
