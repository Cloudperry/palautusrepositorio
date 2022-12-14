from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return sum([ostos.lukumaara() for ostos in self._ostokset])

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        if len(self._ostokset) == 0:
            return 0
        else:
            return self._ostokset[0].tuote.hinta() * self._ostokset[0].lukumaara()

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        tuote_oli_korissa = False
        for ostos in self._ostokset:
            if ostos.tuote == lisattava:
                tuote_oli_korissa = True
                ostos.muuta_lukumaaraa(1)

        if not tuote_oli_korissa:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for i, ostos in enumerate(self._ostokset):
            if ostos.tuote == poistettava:
                if ostos.lukumaara() > 1:
                    ostos.muuta_lukumaaraa(-1)
                else:
                    self._ostokset.pop(i) # Remove operaatio olisi hitaampi :D
                break

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset.clear()

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset 
