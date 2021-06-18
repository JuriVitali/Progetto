from Vendita_Biglietti.Model.ListaBiglietti import ListaBiglietti


class ControlloreListaBiglietti():
    def __init__(self):
        super(ControlloreListaBiglietti, self).__init__()
        self.model = ListaBiglietti()

    def svuota_lista_biglietti(self):
        self.model.lista_biglietti = []

    def get_lista_biglietti(self):
        return self.model.lista_biglietti

    def add_biglietto(self, biglietto):
        self.model.add_biglietto(biglietto)

    def get_cliente(self, cod_fisc):
        return self.model.get_cliente(cod_fisc)

    def controlla_disp_sconto_tessera(self, biglietto):
        return self.model.controlla_disp_sconto_tessera(biglietto)

    def get_parametri_biglietti(self):
        return self.model.get_parametri_biglietti()

    def get_prezzi(self):
        lista_prezzi = self.model.get_prezzi()
        totale = 0.0
        for prezzo in lista_prezzi:
            totale += prezzo

        return {"prezzi": lista_prezzi, "totale": totale}

    def aggiorna_servizi_utilizzati(self):
        self.model.aggiorna_servizi_utilizzati()

    def prenota_posti(self, spettacolo):
        self.model.prenota_posti(spettacolo)

    def save_date(self):
        self.model.save_date()