from GestioneServizi.Model.ParametriServizi import ParametriServizi


class Biglietto():
    def __init__(self, titolo_film, data_spett, ora_inizio_spett, sala, fila_posto, colonna_posto, cliente):
        super(Biglietto, self).__init__()
        self.titolo_film = titolo_film
        self.data_spett = data_spett
        self.ora_inizio_spett = ora_inizio_spett
        self.sala = sala
        self.fila_posto = fila_posto
        self.colonna_posto = colonna_posto
        self.cliente = cliente

        self.prezzo = 0.0
        self.poltrona_premium = False
        self.weekend = False
        self.under_14 = False


    def calcola_prezzo(self):
        p = ParametriServizi()
        prezzo = p.tariffa_base_biglietto

        if self.poltrona_premium:
            prezzo += p.magg_premium_biglietto
        if self.weekend:
            prezzo += p.magg_weekend_biglietto
        if self.under_14:
            prezzo -= p.sconto_under_14_biglietto

        self.prezzo = prezzo