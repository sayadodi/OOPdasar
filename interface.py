class Control:
    def pindahkan_chenel(self, chanel):
        pass
    
    def besarkan_chenel(self):
        pass
    
    def kecilkan_chanel(self):
        pass

class Tv(Control):
    def __init__(self, chanel=1, volume=0):
        self.__chanel = chanel
        self.__volume = volume
    
    def pindahkan_chenel(self, chanel):
        self.__chanel = chanel
    
    def besarkan_chenel(self):
        self.__volume += 1
    
    def kecilkan_chanel(self):
        if self.__volume > 0:
            self.__volume -= 1
        else:
            print("Maaf volume sudah yang paling kecil")
    
    def info(self):
        print("-----INFORMASI TV------")
        print(f"Chanel:\t{self.__chanel}")
        print(f"Volume:\t{self.__volume}")


politron = Tv()
while True:
    print('---MENU---')
    print('1. Ganti Chanel')
    print('2. Naikkan Volume')
    print('3. Turunkan Volume')
    print('4. Keluar')
    pilih = input('Pilih menu: ')
    
    if pilih == '1':
        new_chanel = input('Masukkan nomor chanel baru: ')
        politron.pindahkan_chenel(new_chanel)
    elif pilih == '2':
        politron.besarkan_chenel()
    elif pilih == '3':
        politron.kecilkan_chanel()
    elif pilih == '4':
        break
    else:
        print('Pilihan tidak valid. Silakan coba lagi.')

    politron.info()
