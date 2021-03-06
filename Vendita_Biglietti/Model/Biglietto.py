from PyQt5.QtCore import QDate

from GestioneServizi.Model.ParametriServizi import ParametriServizi
from Utilità.Parametri import Parametri


class Biglietto():
    def __init__(self, titolo_film, data_spett, ora_inizio_spett, sala, fila_posto, colonna_posto, cliente):
        super(Biglietto, self).__init__()
        self.titolo_film = titolo_film
        self.data_spett = data_spett
        self.ora_inizio_spett = ora_inizio_spett
        self.sala = sala
        self.fila_posto = fila_posto
        self.colonna_posto = colonna_posto
        self.cliente = cliente

        self.prezzo = 0.0
        self.parametri = {
            "premium": False,
            "weekend": False,
            "under 14": False,
            "utilizza abb": False,
            "sconto tess": False
        }

        self.controlla_poltrona()
        self.controlla_eta()
        self.controlla_giorno_settimanale()

    # Metodo che controlla se la poltrona associata al biglietto è premium e aggiorna di conseguenza
    # il dizionario contenente i parametri per determinare il prezzo del biglietto
    def controlla_poltrona(self):
        p = Parametri()
        if self.sala == p.sale[0] and self.fila_posto in p.file_vip_sala_1:
            self.parametri["premium"] = True
        elif self.sala == p.sale[1] and self.fila_posto in p.file_vip_sala_2:
            self.parametri["premium"] = True
        elif self.sala == p.sale[2] and self.fila_posto in p.file_vip_sala_3:
            self.parametri["premium"] = True
        elif self.sala == p.sale[3] and self.fila_posto in p.file_vip_sala_4:
            self.parametri["premium"] = True

    # Metodo che determina l'età del cliente che ha acquistato il biglietto e aggiorna di conseguenza
    # il dizionario contenente i parametri per determinare il prezzo del biglietto
    def controlla_eta(self):
        if self.cliente.get_eta() < 14:
            self.parametri["under 14"] = True

    # Metodo che determina il giorno della settimana e aggiorna di conseguenza
    # il dizionario contenente i parametri per determinare il prezzo del biglietto
    def controlla_giorno_settimanale(self):
        giorno_settimana = QDate.currentDate().dayOfWeek()
        if giorno_settimana == 6 or giorno_settimana == 7:
            self.parametri["weekend"] = True

    # Metodo che ritorna True se il cliente che ha acquistato il biglietto possiede una tessera e ha
    # punti sufficienti per l'ottenimento dello socnto. Altrimenti ritorna False.
    def controlla_disp_sconto_tess(self):
        return self.cliente.tessera.controlla_disp_sconto()

    # Metodo che ritorna il prezzo del biglietto dopo averlo calcolato tenendo in considerazione
    # i parametri del biglietto e le corrispondenti tariffe
    def calcola_prezzo(self):
        if not self.parametri["utilizza abb"]:
            p = ParametriServizi()
            prezzo = p.tariffa_base_biglietto

            if self.parametri["premium"]:
                prezzo += p.magg_premium_biglietto

            if self.parametri["weekend"]:
                prezzo += p.magg_weekend_biglietto

            if self.parametri["under 14"]:
                prezzo -= p.sconto_under_14_biglietto

            if self.cliente.tessera is not None and self.controlla_disp_sconto_tess():
                prezzo -= p.sconto_tessera
                self.parametri["sconto tess"] = True

            self.prezzo = prezzo

        return self.prezzo

    # Metodo che aggiorna la tessera o l'abbonamento (se utilizzati) del cliente che ha acquistato il biglietto
    def aggiorna_servizi_utilizzati(self):
        if self.parametri["utilizza abb"]:
            self.cliente.abbonamento.effetua_ingresso()
        elif self.cliente.tessera is not None:
            if self.parametri["sconto tess"]:
                self.cliente.tessera.applica_sconto()

            self.cliente.tessera.aggiungi_punti(self.prezzo)