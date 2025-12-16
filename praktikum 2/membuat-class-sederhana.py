# mendefinisikan sebuah class yang bernama 'mahasiwa'
class mahasiswa:
    pass # 'pass' berarti class ini untuk sementara tidak memiliki apa apa

# membuat (instantiate) objek dari class mahasiwa
# proses ini disebut instansiasi
mahasiswa_1 = mahasiswa()
mahasiswa_2 = mahasiswa()

# mencetak alamat memori dari kedua objek   
# ini membuktikan bahwa keduanya objek yang berbeda
print("alamat memori mahasiswa_1:", id(mahasiswa_1))
print("alamat memori mahasiswa_2:", id(mahasiswa_2))