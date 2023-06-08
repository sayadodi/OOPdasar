class sumation:
    def sam(self, a, b):
        hasil = a + b
        print(f"Hasil Penjumlahan - {hasil}")


class multiplication:
    def multi(self, a, b):
        hasil = a * b
        print(f"Hasil pengurangan - {hasil}")


class kalkulator(sumation, multiplication):
    def devide(self, a, b):
        hasil = a / b
        print(f"Hasil Pembagian {hasil}")


calc = kalkulator()
while True:
    print("1. Penjumlahan ")
    print("2. Perkalian ")
    print("3. Pembagian ")
    pilih = int(input("Pilih Menu"))
    if pilih == 1:
        a = int(input("Bialangan 1 "))
        b = int(input("Bialangan 2 "))
        calc.sam(a, b)
    elif pilih == 2:
        a = int(input("Bialangan 1 "))
        b = int(input("Bialangan 2 "))
        calc.multi(a, b)
    elif pilih == 3:
        a = int(input("Bialangan 1 "))
        b = int(input("Bialangan 2 "))
        calc.devide(a, b)
    else:
        print("Keluar Menu")
        break
