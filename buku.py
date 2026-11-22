class Buku:
    def __init__(self, kode, judul, penulis, penerbit, tahun):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun = tahun

    def tampilkan_info(self):
        print("Kode Buku :", self.kode)
        print("Judul     :", self.judul)
        print("Penulis   :", self.penulis)
        print("Penerbit  :", self.penerbit)
        print("Tahun     :", self.tahun)

    def ke_baris(self):
        return (self.kode + "|" + self.judul + "|" + self.penulis + "|"
                + self.penerbit + "|" + self.tahun)