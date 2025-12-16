class mahasiswa:
    # constructo yang dipanggil saat objek dibuat
    def __init__(self, input_nama, input_nim, input_prodi):
        # atribut instance, nilainya unik untuk setiap objek
        self.nama = input_nama
        self.nim = input_nim
        self.prodi = input_prodi
        print(f"objek mahasiswa dengan nama {self.nama} telah di buat")
        
# membuat objek dengan memberi argumen untuk constructor
otong = mahasiswa("otong surotong", "12345", "teknik informatika")
ucup = mahasiswa("ucup suucup", "67890", "sistem informasi")

# mengakses atribut dari setiap objek
print("--- data mahasiswa ---")
print(f"data mahasiwa 1: {otong.nama} - {otong.nim} - {otong.prodi}")
print(f"data mahasiwa 2: {ucup.nama} - {ucup.nim} - {ucup.prodi}")
