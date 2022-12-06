class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_tulos = tulos

    def paivita_edellinen(self):
        self.edellinen_tulos = self.tulos

    def miinus(self, arvo):
        self.paivita_edellinen()
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.paivita_edellinen()
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.paivita_edellinen()
        self.tulos = 0

    def kumoa(self):
        self.tulos = self.edellinen_tulos

    def aseta_arvo(self, arvo):
        self.paivita_edellinen()
        self.tulos = arvo
