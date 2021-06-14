import os
import pickle


class ListaBiglietti():
    def __init__(self):
        super(ListaBiglietti, self).__init__()
        self.lista_biglietti = []
        self.lista_clienti = []
        self.lista_report = []

        if os.path.isfile('GestioneClienti/Salvataggio_lista_.pickle'):
            with open('Spettacoli/Salvataggio_lista_clienti.pickle', 'rb') as g:
                self.lista_clienti = pickle.load(g)

        if os.path.isfile('Spettacoli/Salvataggio_lista_report.pickle'):
            with open('Spettacoli/Salvataggio_lista_report.pickle', 'rb') as h:
                self.lista_report = pickle.load(h)

    def add_biglietto(self, biglietto):
        self.lista_biglietti.append(biglietto)



