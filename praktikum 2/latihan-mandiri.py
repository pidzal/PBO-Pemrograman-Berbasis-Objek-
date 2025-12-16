class Buku:
    # Constructor
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False  

    def tampilkan_info(self):
        status = "Dipinjam" if self.status_pinjam else "Tersedia"
        print("--- Informasi Buku ---")
        print(f"Judul        : {self.judul}")
        print(f"Penulis      : {self.penulis}")
        print(f"Tahun Terbit : {self.tahun_terbit}")
        print(f"Status       : {status}")
        print("----------------------\n")

    def pinjam_buku(self):
        if not self.status_pinjam:
            self.status_pinjam = True
            print(f"Buku '{self.judul}' telah dipinjam.\n")
        else:
            print(f"Buku '{self.judul}' sedang tidak tersedia.\n")

    def kembalikan_buku(self):
        if self.status_pinjam:
            self.status_pinjam = False
            print(f"Buku '{self.judul}' telah dikembalikan.\n")
        else:
            print(f"Buku '{self.judul}' memang sudah tersedia.\n")

# Membuat objek buku
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980)

print("=== Status Awal Buku ===")
buku1.tampilkan_info()
buku2.tampilkan_info()

print("=== Peminjaman Buku ===")
buku1.pinjam_buku()
buku1.tampilkan_info()

print("=== Pengembalian Buku ===")
buku1.kembalikan_buku()
buku1.tampilkan_info()
