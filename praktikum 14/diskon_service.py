# diskon_service.py
import pdb

class DiskonCalkulator:
    """ Menghituing harga akhir setelah diskon"""
    
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        
        # pdb.set_trace() # <-- untuk Debugging : tempatkan di sini
        
        # --- BUG LOGIKA DISINI ---
        # presentase tidak dibagi 100, sehingga diskon 10% dihitung sebagai  1000%
        # jumlah_diskon = harga_awal * presentase_diskon
        
        # code perbaikan
        jumlah_diskon = harga_awal * persentase_diskon / 100
        
        harga_akhir = harga_awal - jumlah_diskon
        
        return harga_akhir
    
# --- UJI COBA (ini adalah test case yang akan GAGAL) ---
if __name__ == '__main__' :
    calc = DiskonCalkulator()
    # Input: 1000 - 10%. hasil yang diharapkan: 900.0
    hasil = calc.hitung_diskon(1000, 0)
    print(f"Hasil: {hasil}")
    # Output: Hasil -9000.0 (salah)