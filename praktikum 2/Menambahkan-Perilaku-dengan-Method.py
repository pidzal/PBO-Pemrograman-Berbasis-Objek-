class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def sapa(self):
        print(f"Halo! Nama saya {self.nama}. Senang berkenalan!")

    # Method kedua: menampilkan informasi lengkap
    def tampilkan_info(self):
        print("— Informasi Mahasiswa —")
        print(f"Nama  : {self.nama}")
        print(f"NIM   : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print("------------------------")


# --- Bagian Utama Program ---
# Membuat objek
otong = Mahasiswa("Otong Surotong", "12345", "Teknik Informatika")
ucup = Mahasiswa("Ucup Surucup", "67890", "Sistem Informasi")

# Memanggil method dari masing-masing objek
print("\n--- Interaksi dengan Objek ---")
otong.sapa()
ucup.sapa()

print("\n--- Meminta Objek Menampilkan Datanya ---")
otong.tampilkan_info()
ucup.tampilkan_info()
