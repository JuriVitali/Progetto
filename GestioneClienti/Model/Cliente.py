from PyQt5.QtCore import QDate

from GestioneClienti.Model.Abbonamento import Abbonamento
from GestioneClienti.Model.Tessera import Tessera

class Cliente():
    def __init__(self, nome, cognome, data_nascita, cod_fisc, telefono, email):
        super(Cliente, self).__init__()
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.cod_fisc = cod_fisc
        self.telefono = telefono        #numero di telefono
        self.email = email
        self.abbonamento = None
        self.tessera = None

    # Metodo che assegna un nuovo abbonamento avente come codice codice_abb (parametro)
    # al cliente
    def assegna_abbonamento(self, codice_abb):
        self.abbonamento = Abbonamento(codice_abb)

    # Metodo che assegna una nuova tessera avente come codice codice_tess (parametro)
    # al cliente
    def assegna_tessera(self, codice_tess):
        self.tessera = Tessera(codice_tess)

    # metodo che restituisce l'età del cliente
    def get_eta(self):
        data_corrente = QDate.currentDate()
        anni_diff = data_corrente.year() - self.data_nascita.year()

        if data_corrente.month() < self.data_nascita.month():
            return anni_diff - 1
        if data_corrente.month() > self.data_nascita.month():
            return anni_diff

        if data_corrente.day() < self.data_nascita.day():
            return anni_diff - 1
        return anni_diff