class nama:
    # classvariable
    tahun = 0

    def __init__(self, InputNama, inpuUmur) -> None:
        # instace variable
        self.name = InputNama
        self.umur = inpuUmur
        nama.tahun += 1
        print("saya adalah " + InputNama)


nama1 = nama("Dodi", 19)
print(nama.tahun)
nama2 = nama("tegar", 19)
print(nama.tahun)
