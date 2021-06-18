from GestioneServizi.Model.ParametriServizi import ParametriServizi

class Tessera():
    def __init__(self, codice):
        super(Tessera, self).__init__()
        self.codice = codice
        self.punti = 0

    # Metodo che aggiunge punti alla tessera pari a 10 volte l'importo in euro (parametro)
    def aggiungi_punti(self, importo):
        p = ParametriServizi()
        self.punti += int(importo * p.punti_per_euro)

    # Metodo che controlla se è disponibile uno sconto per il possessore della tessera
    # e in caso afferemativo restituisce True.
    # In caso negativo restituisce False
    def controlla_disp_sconto(self):
        p = ParametriServizi()
        if self.punti >= p.soglia_punti_sconto_tessera:
            return True
        return False

    #Metodo che sottrae dalla tessera i punti necessari per avere lo sconto
    def applica_sconto(self):
        p = ParametriServizi()
        self.punti -= p.soglia_punti_sconto_tessera