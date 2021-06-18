from Vendita_Biglietti.Model.ListaBiglietti import ListaBiglietti


class ControlloreListaBiglietti():
    def __init__(self):
        super(ControlloreListaBiglietti, self).__init__()
        self.model = ListaBiglietti()

    # Metodo che elimina tutti gli elementi dalla lista dei biglietti
    def svuota_lista_biglietti(self):
        self.model.lista_biglietti = []

    #Metodo che ritorna la lista dei biglietti
    def get_lista_biglietti(self):
        return self.model.lista_biglietti

    # Metodo che aggiunge un biglietto alla lista dei biglietti
    def add_biglietto(self, biglietto):
        self.model.add_biglietto(biglietto)

    # Metodo che dato il codice fiscale di un cliente ritorna il cliente corrispondente.
    # Se il codice fiscale non corrisponde ad alcun cliente registrato a sistema, il metodo
    # ritorna None
    def get_cliente(self, cod_fisc):
        return self.model.get_cliente(cod_fisc)

    # Metodo che ritorna True se il cliente che ha acquistato il biglietto (parametro) possiede una tessera e ha
    # punti sufficienti per l'ottenimento dello socnto. Altrimenti ritorna False.
    def controlla_disp_sconto_tessera(self, biglietto):
        return self.model.controlla_disp_sconto_tessera(biglietto)

    # Metodo che restituisce una lista contenente un dizioario per ogni biglietto della
    # lista dei biglietti. Ogni dizionario contiene i parametro del
    # biglietto corrispondente
    def get_parametri_biglietti(self):
        return self.model.get_parametri_biglietti()

    # Metodo che ritorna un dizionario contenente una lista, con i prezzi dei singoli
    # biglietti, e il prezzo totale
    def get_prezzi(self):
        lista_prezzi = self.model.get_prezzi()
        totale = 0.0
        for prezzo in lista_prezzi:
            totale += prezzo

        return {"prezzi": lista_prezzi, "totale": totale}

    # Metodo che, per ogni biglietto, aggiorna la tessera o l'abbonamento (se utilizzati)
    # del cliente che ha acquistato il biglietto
    def aggiorna_servizi_utilizzati(self):
        self.model.aggiorna_servizi_utilizzati()

    # Metodo che prenota il posto associato ad ogni biglietto della lista.
    # Prende come parametro lo spettacolo per il quale si devono prenotare tali posti
    def prenota_posti(self, spettacolo):
        self.model.prenota_posti(spettacolo)

    # Metodo che salva su file i dati dei clienti e dei report registrati a sistema
    def save_date(self):
        self.model.save_date()