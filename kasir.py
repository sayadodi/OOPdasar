print("Selamat data di aplikasi kasir")
print("Pilih menu")

a = 2000
b = 5000
c = 10000

print("a. Mie Gorengn\nb. Kentang\nc. Sabun")

totalBarang = int(input("Masukkan total barang yang akal di beli" ))
i = 1
while i <= totalBarang:
    jenisBrang = str(input("Masukkan Jenis Barang ke"))

    if jenisBrang == "a":
        totalHarga = totalBarang + a
    elif jenisBrang == "b":
        totalHarga = totalHarga + b
    else:
        totalHarga = totalHarga + c
    i += 1
print(totalHarga)
