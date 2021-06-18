import os
import pickle


class ListaBiglietti():
    def __init__(self):
        super(ListaBiglietti, self).__init__()
        self.lista_biglietti = []
        self.lista_clienti = []
        self.lista_report = []

        if os.path.isfile('GestioneClienti/Salvataggio_lista_clienti.pickle'):    # caricamento dei dati
            with open('GestioneClienti/Salvataggio_lista_clienti.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)

        if os.path.isfile('Spettacoli/Salvataggio_lista_report.pickle'):
            with open('Spettacoli/Salvataggio_lista_report.pickle', 'rb') as h:
                self.lista_report = pickle.load(h)

        # Controllo della validità di ogni abbonamento
        for cliente in self.lista_clienti:
            if cliente.abbonamento is not None and not cliente.abbonamento.verifica_validita():
                cliente.abbonamento = None

    def add_biglietto(self, biglietto):
        self.lista_biglietti.append(biglietto)

    def get_cliente(self, cod_fisc):
        for cliente in self.lista_clienti:
            if cliente.cod_fisc == cod_fisc:
                return cliente
        return None

    def controlla_disp_sconto_tessera(self, biglietto):
        return biglietto.controlla_disp_sconto_tess()

    def get_parametri_biglietti(self):
        lista_param_biglietti = []
        for biglietto in self.lista_biglietti:
            lista_param_biglietti.append(biglietto.parametri)

        return lista_param_biglietti

    def get_prezzi(self):
        lista_prezzi = []
        for biglietto in self.lista_biglietti:
            lista_prezzi.append(biglietto.calcola_prezzo())

        return lista_prezzi

    def aggiorna_servizi_utilizzati(self):
        for biglietto in self.lista_biglietti:
            biglietto.aggiorna_servizi_utilizzati()

    def prenota_posti(self, spettacolo):
        for biglietto in self.lista_biglietti:
            spettacolo.prenota_posto(biglietto.fila_posto, biglietto.colonna_posto)

    def save_date(self):
        with open('GestioneClienti/Salvataggio_lista_clienti.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)



