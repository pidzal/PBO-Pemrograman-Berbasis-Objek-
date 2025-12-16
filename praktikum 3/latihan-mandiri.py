class Karyawan:
    def __init__(self, nama, id_karyawan, gaji):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji = gaji

    def get_nama(self):
        return self.__nama

    def get_id(self):
        return self.__id_karyawan

    def get_gaji(self):
        return self.__gaji

    def set_nama(self, nama_baru):
        if nama_baru != "":  
            self.__nama = nama_baru
        else:
            print("Error: Nama tidak boleh kosong!")

    def set_gaji(self, gaji_baru):
        if gaji_baru > 0:  
            self.__gaji = gaji_baru
        else:
            print("Error: Gaji harus lebih besar dari 0!")

    def info(self):
        print(f"Nama       : {self.__nama}")
        print(f"ID Karyawan: {self.__id_karyawan}")
        print(f"Gaji       : {self.__gaji}")


k1 = Karyawan("Budi", "K001", 5000000)

print("=== Data Awal Karyawan ===")
k1.info()

print("\n--- Simulasi: Ubah gaji menjadi negatif ---")
k1.set_gaji(-5000000)  
k1.info()

print("\n--- Simulasi: Ubah nama menjadi kosong ---")
k1.set_nama("")  
k1.info()

print("\n--- Simulasi: Ubah gaji menjadi positif valid ---")
k1.set_gaji(6000000)  
k1.info()
