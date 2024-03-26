import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_oikein(self):
        self.maksukortti.lataa_rahaa(1400)
        self.assertAlmostEqual(str(self.maksukortti),  "Kortilla on rahaa 24.00 euroa")

    def test_ota_rahaa_oikein(self):
        self.assertAlmostEqual(self.maksukortti.ota_rahaa(900), True)
        self.assertAlmostEqual(self.maksukortti.ota_rahaa(900), False)

    def test_saldo_euroina_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)