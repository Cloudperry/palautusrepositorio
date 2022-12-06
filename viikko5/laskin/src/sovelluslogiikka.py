class Summa:
    pass

class Erotus:
    pass

class Nollaus:
    pass

class Kumoa:
    pass

class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def kumoa(self):
        pass

    def aseta_arvo(self, arvo):
        self.tulos = arvo
