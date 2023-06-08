class Pahlawan:
    def __init__(self, nama, attack) -> None:
        self.nama = nama
        self.serang = attack

    def ShowInfo(self):
        print(
            "Pahlawan Tersebut Adalah",
            self.nama,
            "Dia Mempunyai Serangan Sebesar ",
            self.serang,
        )


class Serangan(Pahlawan):
    def __init__(self, nama) -> None:
        super().__init__(nama, 100)
        super().ShowInfo()


Gatot = Serangan("Gatot Kaca")
