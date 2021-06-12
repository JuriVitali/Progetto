from GestioneServizi.Model.ParametriServizi import ParametriServizi

class ControlloreParametriServizi():
    def __init__(self):
        super(ControlloreParametriServizi, self).__init__()
        self.model = ParametriServizi()

    def get_tariffa_base_biglietto(self):
        return self.model.tariffa_base_biglietto

    def get_magg_premium_biglietto(self):
        return self.model.magg_premium_biglietto

    def get_magg_weekend_biglietto(self):
        return self.model.magg_weekend_biglietto

    def get_sconto_under_14_biglietto(self):
        return self.model.sconto_under_14_biglietto

    def get_prezzo_tessera(self):
        return self.model.prezzo_tessera

    def get_soglia_punti_sconto_tessera(self):
        return self.model.soglia_punti_sconto_tessera

    def get_sconto_tessera(self):
        return self.model.sconto_tessera

    def get_punti_per_euro(self):
        return self.model.punti_per_euro

    def get_prezzo_abbonamento(self):
        return self.model.prezzo_abbonamento

    def get_ingressi_consentiti_abb(self):
        return self.model.ingressi_consentiti_abb

    def get_durata_abb(self):
        return self.model.durata_abb

    def set_parametri_biglietto(self, lista_nuovi_parametri):
        self.model.tariffa_base_biglietto = lista_nuovi_parametri[0]
        self.model.magg_premium_biglietto = lista_nuovi_parametri[1]
        self.model.magg_weekend_biglietto = lista_nuovi_parametri[2]
        self.model.sconto_under_14_biglietto = lista_nuovi_parametri[3]

    def set_parametri_tessera(self, lista_nuovi_parametri):
        self.model.prezzo_tessera = lista_nuovi_parametri[0]
        self.model.soglia_punti_sconto_tessera = lista_nuovi_parametri[1]
        self.model.sconto_tessera = lista_nuovi_parametri[2]

    def set_parametri_abbonamento(self, lista_nuovi_parametri):
        self.model.prezzo_abbonamento = lista_nuovi_parametri[0]
        self.model.ingressi_consentiti_abb = lista_nuovi_parametri[1]
        self.model.durata_abb = lista_nuovi_parametri[2]

    def save_data(self):
        self.model.save_data()