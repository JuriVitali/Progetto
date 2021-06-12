from PyQt5.QtCore import QDate

from GestioneServizi.Model.ParametriServizi import ParametriServizi

class Abbonamento():
    def __init__(self, codice):
        super(Abbonamento, self).__init__()
        self.codice = codice
        p = ParametriServizi()
        self.ingressi_disponibili = p.ingressi_consentiti_abb
        self.data_scadenza = QDate.currentDate().addDays(p.durata_abb)

    def effetua_ingresso(self):
        self.ingressi_disponibili -= 1

    def verifica_validita(self):
        if self.ingressi_disponibili > 0 and self.data_scadenza >= QDate.currentDate():
            return True
        return False