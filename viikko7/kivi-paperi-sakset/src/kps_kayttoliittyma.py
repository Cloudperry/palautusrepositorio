from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()

            if not (self.tuomari._onko_ok_siirto(ekan_siirto) and
                    self.tuomari._onko_ok_siirto(tokan_siirto)):
                break

            self._aseta_ekan_siirto(ekan_siirto)

            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        return "k"

    def _aseta_ekan_siirto(self, siirto): # Tällä tekoälyt laittaa muistiin pelaajan siirrot
        pass
