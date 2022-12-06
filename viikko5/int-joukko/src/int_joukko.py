KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self._joukko = set()

    def kuuluu(self, n):
        return n in self._joukko

    def lisaa(self, n):
        result = n not in self._joukko
        self._joukko.add(n)
        return result

    def poista(self, n):
        result = n in self._joukko
        self._joukko.remove(n)
        return result

    def mahtavuus(self):
        return len(self._joukko)

    def to_int_list(self):
        return list(self._joukko)

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        x._joukko = a._joukko | b._joukko
        return x

    @staticmethod
    def leikkaus(a, b):
        x = IntJoukko()
        x._joukko = a._joukko & b._joukko
        return x

    @staticmethod
    def erotus(a, b):
        x = IntJoukko()
        x._joukko = a._joukko - b._joukko
        return x

    def __str__(self):
        if len(self._joukko) == 0:
            return '{}'
        else:
            return str(self._joukko)
