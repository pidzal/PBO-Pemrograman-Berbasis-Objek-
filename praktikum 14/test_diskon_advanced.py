import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):

    # Tes 5: Uji nilai float (diskon 33% pada 999)
    def test_diskon_float(self):
        calc = DiskonCalculator()
        hasil = calc.hitung_diskon(999, 33)
        expected = 999 - (999 * 33 / 100)
        expected += expected * 0.10  # karena ada bug PPN

        self.assertAlmostEqual(hasil, expected, places=2)

    # Tes 6: Edge Case (harga awal 0)
    def test_edge_case_harga_nol(self):
        calc = DiskonCalculator()
        hasil = calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0)

if __name__ == "__main__":
    unittest.main()
