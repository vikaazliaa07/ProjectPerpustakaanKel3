
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
