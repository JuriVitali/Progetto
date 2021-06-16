from PyQt5.QtCore import QDate

from GestioneServizi.Model.ParametriServizi import ParametriServizi

class Abbonamento():
    def __init__(self, codice):
        super(Abbonamento, self).__init__()
        self.codice = codice
        p = ParametriServizi()
        self.ingressi_disponibili = p.ingressi_consentiti_abb
        self.data_scadenza = QDate.currentDate().addDays(p.durata_abb)

    # Metodo che diminuisce di 1 il numero di ingresso a disposizione con l'abbonamento
    def effetua_ingresso(self):
        self.ingressi_disponibili -= 1

    # Metodo che verifica se l'abbonamento è valido, cioè se non è scaduto e se consente ancora almeno
    # un ingresso
    def verifica_validita(self):
        if self.ingressi_disponibili > 0 and self.data_scadenza >= QDate.currentDate():
            return True
        return False