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

class Perpustakaan:
    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.data_buku = {}
        self.muat_data()

    def muat_data(self):
        self.data_buku = {}
        try:
            file = open(self.nama_file, "r")
            for baris in file:
                baris = baris.strip()
                if baris == "":
                    continue
                bagian = baris.split("|")
                if len(bagian) == 5:
                    buku = Buku(bagian[0], bagian[1], bagian[2],
                                bagian[3], bagian[4])
                    self.data_buku[buku.kode] = buku
            file.close()
        except FileNotFoundError:
            pass

    def simpan_data(self):
        file = open(self.nama_file, "w")
        for kode in self.data_buku:
            file.write(self.data_buku[kode].ke_baris() + "\n")
        file.close()
