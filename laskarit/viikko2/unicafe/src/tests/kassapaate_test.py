import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(450)

    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luotu_paate_toimii_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100000)
        self.assertEqual(self.kassapaate.edulliset , 0)
        self.assertEqual(self.kassapaate.maukkaat , 0)

    def test_syo_edullisesti_kateisella_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100240)
        self.assertEqual(self.kassapaate.edulliset , 1)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100240)
        self.assertEqual(self.kassapaate.edulliset , 1)
        

    def test_syo_maukkaasti_kateisella_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100400)
        self.assertEqual(self.kassapaate.maukkaat , 1)
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100400)
        self.assertEqual(self.kassapaate.maukkaat , 1)
        

    def test_syo_edullisesti_kortilla_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100000)
        self.assertEqual(self.kassapaate.edulliset , 1)
        self.assertEqual(self.maksukortti.saldo, 210)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100000)
        self.assertEqual(self.kassapaate.edulliset , 1)
        self.assertEqual(self.maksukortti.saldo, 210)

    def test_syo_maukkaasti_kortilla_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100000)
        self.assertEqual(self.kassapaate.maukkaat , 1)
        self.assertEqual(self.maksukortti.saldo, 50)
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo, 50)

    def test_lataa_rahaa_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 950)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 950)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kassassa_rahaa_euroina_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        