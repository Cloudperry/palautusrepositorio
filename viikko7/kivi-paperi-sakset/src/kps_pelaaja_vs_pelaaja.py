from kps_kayttoliittyma import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")
