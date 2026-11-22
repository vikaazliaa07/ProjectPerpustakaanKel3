
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
