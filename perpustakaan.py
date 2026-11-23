from buku import Buku

def muat_data(self):
        self.data_buku = {}
        try:
            file = open(self.nama_file, "r")
            for baris in file:
                baris_bersih = baris.strip()
                if baris_bersih != "":
                    potongan = baris_bersih.split("|")
                    if len(potongan) == 5:
                        kode = potongan[0]
                        judul = potongan[1]
                        penulis = potongan[2]
                        penerbit = potongan[3]
                        tahun = potongan[4]

                        buku = Buku(kode, judul, penulis, penerbit, tahun)
                        self.data_buku[kode] = buku
            file.close()
        except FileNotFoundError:
            pass

    def simpan_data(self):
        file = open(self.nama_file, "w")
        for kode in self.data_buku:
            buku_sekarang = self.data_buku[kode]
            teks_buku = buku_sekarang.ke_baris()
            file.write(teks_buku + "\n")
        file.close()

    def tambah_buku(self, buku):
            if buku.kode in self.data_buku:
                print("Gagal, kode buku sudah ada!")
                return
            self.data_buku[buku.kode] = buku
            self.simpan_data()
            print("Buku berhasil ditambahkan.")
    
    def cari_buku(self, kode):
            if kode in self.data_buku:
                print("Buku ditemukan:")
                self.data_buku[kode].tampilkan_info()
            else:
                print("Buku dengan kode", kode, "tidak ditemukan.")

    def hapus_buku(self, kode):
            if kode not in self.data_buku:
                print("Buku dengan kode", kode, "tidak ditemukan.")
                return
            self.data_buku[kode].tampilkan_info()
            jawab = input("Yakin ingin menghapus? (y/n): ")
            if jawab.lower() == "y":
                del self.data_buku[kode]
                self.simpan_data()
                print("Buku berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")

    def ubah_buku(self, kode):
            if kode not in self.data_buku:
                print("Buku dengan kode", kode, "tidak ditemukan.")
                return
            buku = self.data_buku[kode]
            print("Data saat ini:")
            buku.tampilkan_info()
            print("Isi data baru (kosongkan jika tidak diubah)")
    
            judul = input("Judul baru    : ")
            penulis = input("Penulis baru  : ")
            penerbit = input("Penerbit baru : ")
            tahun = input("Tahun baru    : ")
    
            if judul != "":
                buku.judul = judul
            if penulis != "":
                buku.penulis = penulis
            if penerbit != "":
                buku.penerbit = penerbit
            if tahun != "":
                buku.tahun = tahun
    
            self.simpan_data()
            print("Buku berhasil diperbarui.")

    def tampilkan_semua(self):
        if len(self.data_buku) == 0:
            print("Belum ada data buku.")
            return
        for kode in self.data_buku:
            self.data_buku[kode].tampilkan_info()
            print("-" * 30)
    
