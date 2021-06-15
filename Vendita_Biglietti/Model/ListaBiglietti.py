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

    def add_biglietto(self, biglietto):
        self.lista_biglietti.append(biglietto)

    def get_cliente(self, cod_fisc):
        for cliente in self.lista_clienti:
            if cliente.cod_fisc == cod_fisc:
                return cliente
        return None


