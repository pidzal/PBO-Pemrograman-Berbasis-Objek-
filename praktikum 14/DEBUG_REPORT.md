# DEBUG REPORT – Bug PPN 10%

## Deskripsi Bug
Pada fungsi `hitung_diskon`, PPN 10% ditambahkan pada harga akhir.
Namun saat debugging, ditemukan bahwa nilai PPN dihitung lebih dari satu kali.

## Langkah Debugging (pdb)

1. Menjalankan program dan masuk ke pdb:

pdb.set_trace()

2. Mengecek harga setelah diskon:

(Pdb) p harga_setelah_diskon<br>
900.0<br>

3. Mengecek nilai PPN:

(Pdb) p  ppn<br>
90.0<br>

4. Mengecek harga akhir:

(Pdb) p harga_akhir<br>
990.0<br>

5. Saat fungsi lain menambahkan PPN kembali:    

(Pdb) p harga_akhir + ppn<br>
1080.0<br>


## Kesimpulan
PPN 10% telah ditambahkan lebih dari satu kali sehingga menyebabkan harga akhir menjadi lebih besar dari seharusnya. Bug ini berasal dari penambahan PPN yang tidak terkontrol di fungsi `hitung_diskon`.