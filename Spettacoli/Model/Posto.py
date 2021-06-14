from PyQt5.QtWidgets import QCheckBox, QPushButton, QSizePolicy
from Utilità.User_int_utility import User_int_utility

class Posto():
    def __init__(self, fila, posizione, premium):
        self.disponibile = True
        self.fila = fila
        self.posizione = posizione
        self.premium = premium

    # Metodo che consente la prenotazione di un posto
    def prenota(self):
        self.disponibile = False








