# class menu
class Menu:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    def info(self):
        return f"{self._nama} - Rp{self._harga}"

# child class dari menu
class MenuMinuman(Menu):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self._ukuran = ukuran

    def info(self):  # overriding
        return f"{self._nama} ({self._ukuran}) - Rp{self._harga}"

# class pesanan
class Pesanan:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.menu_dipesan = []
        self.status = "Belum diproses"

    def tambah_menu(self, menu):
        self.menu_dipesan.append(menu)
        print(f"{self.pelanggan.nama} memesan {menu._nama}")

    def ubah_status(self, status):
        self.status = status
        print(f"Status pesanan {self.pelanggan.nama}: {self.status}")

    def tampil(self):
        print(f"\nPesanan {self.pelanggan.nama}:")
        for m in self.menu_dipesan:
            print("-", m.info())
        total = sum(m._harga for m in self.menu_dipesan)
        print(f"Total: Rp{total}")
        print(f"Status: {self.status}")

# class pelanggan
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = Pesanan(self)

    def pesan(self, menu):
        self.pesanan.tambah_menu(menu)

    def konfirmasi(self):
        self.pesanan.ubah_status("Dikonfirmasi")

    def lihat(self):
        self.pesanan.tampil()


# Simulasi
menu1 = Menu("Nasi Goreng", 20000)
minuman = MenuMinuman("Es Teh", 5000, "Besar")

andi = Pelanggan("Andi")
andi.pesan(menu1)
andi.pesan(minuman)
andi.konfirmasi()
andi.lihat()
