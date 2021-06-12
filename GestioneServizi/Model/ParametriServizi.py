import pickle
import os

class ParametriServizi():

    def __init__(self):
        super(ParametriServizi, self).__init__()

        if os.path.isfile('GestioneServizi/Salvataggio_parametri_servizi.pickle'):           #caricamento dei dati
            with open('GestioneServizi/Salvataggio_parametri_servizi.pickle', 'rb') as f:
                lista_parametri = pickle.load(f)

                self.tariffa_base_biglietto = lista_parametri[0]
                self.magg_premium_biglietto = lista_parametri[1]
                self.magg_weekend_biglietto = lista_parametri[2]
                self.sconto_under_14_biglietto = lista_parametri[3]

                self.prezzo_tessera = lista_parametri[4]
                self.soglia_punti_sconto_tessera = lista_parametri[5]
                self.sconto_tessera = lista_parametri[6]
                self.punti_per_euro = lista_parametri[7]

                self.prezzo_abbonamento = lista_parametri[8]
                self.ingressi_consentiti_abb = lista_parametri[9]
                self.durata_abb = lista_parametri[10]

        else:
            self.tariffa_base_biglietto = 7.50
            self.magg_premium_biglietto = 1.00
            self.magg_weekend_biglietto = 0.70
            self.sconto_under_14_biglietto = 1.50

            self.prezzo_tessera = 6.00
            self.soglia_punti_sconto_tessera = 320
            self.sconto_tessera = 3.50
            self.punti_per_euro = 10

            self.prezzo_abbonamento = 25.00
            self.ingressi_consentiti_abb = 5
            self.durata_abb = 40  # durata dell'abbonamento in giorni


    def save_data(self):
        lista_parametri = [self.tariffa_base_biglietto,
                           self.magg_premium_biglietto,
                           self.magg_weekend_biglietto,
                           self.sconto_under_14_biglietto,
                           self.prezzo_tessera,
                           self.soglia_punti_sconto_tessera,
                           self.sconto_tessera,
                           self.punti_per_euro,
                           self.prezzo_abbonamento,
                           self.ingressi_consentiti_abb,
                           self.durata_abb]
        with open('GestioneServizi/Salvataggio_parametri_servizi.pickle', 'wb') as handle:
            pickle.dump(lista_parametri, handle, pickle.HIGHEST_PROTOCOL)