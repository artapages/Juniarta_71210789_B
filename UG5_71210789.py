class Karyawan:
    _nama = ''
    _umur = ''
    _jenisKelamin = None
    _upahPerHari = None

#Constructor
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur

#Getter
    def getNama (self):
        return self._nama

    def getUmur (self):
        return self._umur
    
    def getJenisKelamin (self):
        return self._jenisKelamin
    
    def getUpahPerHari (self):
        return self._upahPerHari

#Setter    
    def setNama (self, nama):
        self._nama = nama
    
    def setUmur (self, umur):
        self._umur = umur
    
    def setJenisKelamin (self, jenisKelamin):
        self._jenisKelamin = jenisKelamin
    
    def setUpahPerHari (self, upahPerHari):
        self._upahPerHari = upahPerHari

#Print Info
    def printInfo (self):
        print('========= INFO =========')
        print('Nama             :', self._nama)
        print('Umur             :', self._umur)
        print('Jenis Kelamin    :', self._jenisKelamin)
        print('Upah per Hari    :', self._upahPerHari)

#Hitung Gaji Bulanan
    def hitungGajiBulanan (self, bulanan):
        if self._upahPerHari == None:
            print('ERROR! Upah per Hari belum di inputkan')
        else:
            print('Gaji Bulan ini : Rp', self._upahPerHari * bulanan)
    
if __name__ == "__main__":
    orang1 = Karyawan("Haniif", 90)
    orang1.printInfo()

    orang2 = Karyawan("Sindu", 190)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerHari(30000)
    orang2.printInfo()

    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)
