import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        assert self.kori.hinta() == 0
        assert self.kori.ostokset() == []

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        assert self.kori.tavaroita_korissa() == 1

    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 4)
        self.kori.lisaa_tuote(maito)
        assert self.kori.hinta() == 4

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        peruna = Tuote("Peruna", 1)
        self.kori.lisaa_tuote(peruna)
        assert self.kori.tavaroita_korissa() == 2

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        assert self.kori.tavaroita_korissa() == 2

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_2x_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        assert self.kori.hinta() == 6

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        assert len(ostokset) == 1

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        assert ostos.tuote.nimi == maito.nimi and ostos.lukumaara() == 1

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_2_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        peruna = Tuote("Peruna", 1)
        self.kori.lisaa_tuote(peruna)
        assert len(self.kori.ostokset()) == 2
