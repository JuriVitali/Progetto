import os
import pickle


class ListaBiglietti():
    def __init__(self):
        super(ListaBiglietti, self).__init__()
        self.lista_biglietti = []
        self.lista_clienti = []
        self.lista_report = []

        # Caricamento lista dei clienti
        if os.path.isfile('GestioneClienti/Salvataggio_lista_clienti.pickle'):
            with open('GestioneClienti/Salvataggio_lista_clienti.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)

        # Caricamento lista dei report
        if os.path.isfile('Report/Salvataggio_lista_report.pickle'):
            with open('Report/Salvataggio_lista_report.pickle', 'rb') as h:
                self.lista_report = pickle.load(h)

        # Controllo della validità di ogni abbonamento
        for cliente in self.lista_clienti:
            if cliente.abbonamento is not None and not cliente.abbonamento.verifica_validita():
                cliente.abbonamento = None

    # Metodo che aggiunge un biglietto alla lista dei biglietti
    def add_biglietto(self, biglietto):
        self.lista_biglietti.append(biglietto)

    # Metodo che dato il codice fiscale di un cliente ritorna il cliente corrispondente.
    # Se il codice fiscale non corrisponde ad alcun cliente registrato a sistema, il metodo
    # ritorna None
    def get_cliente(self, cod_fisc):
        for cliente in self.lista_clienti:
            if cliente.cod_fisc == cod_fisc:
                return cliente
        return None

    # Metodo che ritorna True se il cliente che ha acquistato il biglietto (parametro) possiede una tessera e ha
    # punti sufficienti per l'ottenimento dello socnto. Altrimenti ritorna False.
    def controlla_disp_sconto_tessera(self, biglietto):
        return biglietto.controlla_disp_sconto_tess()

    # Metodo che restituisce una lista contenente un dizioario per ogni biglietto della
    # lista dei biglietti. Ogni dizionario contiene i parametro del
    # biglietto corrispondente
    def get_parametri_biglietti(self):
        lista_param_biglietti = []
        for biglietto in self.lista_biglietti:
            lista_param_biglietti.append(biglietto.parametri)

        return lista_param_biglietti

    # Metodo che ritorna una lista in cui ogni elemento corrisponde al prezzo di un biglietto
    def get_prezzi(self):
        lista_prezzi = []
        for biglietto in self.lista_biglietti:
            lista_prezzi.append(biglietto.calcola_prezzo())

        return lista_prezzi

    # Metodo che, per ogni biglietto, aggiorna la tessera o l'abbonamento (se utilizzati)
    # del cliente che ha acquistato il biglietto
    def aggiorna_servizi_utilizzati(self):
        for biglietto in self.lista_biglietti:
            biglietto.aggiorna_servizi_utilizzati()

    # Metodo che prenota il posto associato ad ogni biglietto della lista.
    # Prende come parametro lo spettacolo per il quale si devono prenotare tali posti
    def prenota_posti(self, spettacolo):
        for biglietto in self.lista_biglietti:
            spettacolo.prenota_posto(biglietto.fila_posto, biglietto.colonna_posto)

    # Metodo che salva su file i dati dei clienti e dei report registrati a sistema
    def save_date(self):
        with open('GestioneClienti/Salvataggio_lista_clienti.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)

        with open('Report/Salvataggio_lista_report.pickle', 'wb') as handle:
            pickle.dump(self.lista_report, handle, pickle.HIGHEST_PROTOCOL)

