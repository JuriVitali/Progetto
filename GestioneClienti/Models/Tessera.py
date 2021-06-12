from GestioneServizi.Model.ParametriServizi import ParametriServizi

class Tessera():
    def __init__(self, codice):
        super(Tessera, self).__init__()
        self.codice = codice
        self.punti = 0

    def aggiungi_punti(self, importo):
        self.punti += int(importo * 10)

    def applica_sconto(self):
        p = ParametriServizi()
        if self.punti >= p.soglia_punti_sconto_tessera:
            self.punti -= p.soglia_punti_sconto_tessera
            return True
        return False