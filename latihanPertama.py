class Hero:
    def __init__(self, name, healt, attackPower, armorNumber) -> None:
        self.nama = name
        self.healt = healt
        self.power = attackPower
        self.armor = armorNumber

    def serang(self, Musuh):
        print(self.nama + " Menyerang " + Musuh.nama)
        Musuh.bertahan(self, self.power)

    def bertahan(self, Musuh, attackPower_Musuh):
        print(self.nama + " Bertahan Serangan " + Musuh.nama)
        attackDiterima = attackPower_Musuh / self.armor
        print("Serangan Terasa : " + str(attackDiterima))
        self.healt -= attackDiterima
        print("Darah " + self.nama + "Tersisa" + str(self.healt))


akai = Hero("Akai", 100, 10, 5)
Balmod = Hero("Balmond", 150, 8, 2)

akai.serang(Balmod)
print("\n")
Balmod.serang(akai)
