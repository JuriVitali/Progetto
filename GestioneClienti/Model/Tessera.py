from GestioneServizi.Model.ParametriServizi import ParametriServizi

class Tessera():
    def __init__(self, codice):
        super(Tessera, self).__init__()
        self.codice = codice
        self.punti = 0

    # Metodo che aggiunge punti alla tessera pari a 10 volte l'importo in euro (parametro)
    def aggiungi_punti(self, importo):
        self.punti += int(importo * 10)

    # Metodo che controlla se è disponibile uno sconto per il possessore della tessera
    # e in caso afferemativo sottrae i punti necessari e restituisce True.
    # In caso negativo restituisce False
    def applica_sconto(self):
        p = ParametriServizi()
        if self.punti >= p.soglia_punti_sconto_tessera:
            self.punti -= p.soglia_punti_sconto_tessera
            return True
        return False