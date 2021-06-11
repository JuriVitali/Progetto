from PyQt5.QtWidgets import QCheckBox
from Utilità.User_int_utility import User_int_utility

class Posto():
    def __init__(self, fila, posizione, premium):
        self.disponibile = True
        self.fila = fila
        self.posizione = posizione
        self.premium = premium
        self.box = QCheckBox()

    # Metodo che consente la prenotazione di un posto
    def prenota(self):
        self.disponibile = False
        self.button.setDisabled(True)

    # Metodo che restituisce un dizionario contenente la fila e la posizione del posto
    def get_posto(self):
        return {"Fila": self.fila, "Posizione": self.posizione}

    # metodo che applica alla checkbox del posto uno stile che varia a seconda
    # se un posto è standard o premium
    def applica_stile_check_box(self):
        if self.premium == True:
            self.box.setStyleSheet("QCheckBox {"
                                   "border: 2px solid " + User_int_utility.tertiary_color + ";"
                                   "background-color : " + User_int_utility.tertiary_color + ";"
                                   "border-radius: 1px;"
                                   "}"
                                   "QCheckBox::indicator"
                                   "{"
                                   "height: 14px;"
                                   "width: 14px;"
                                   "}"
                                   "QCheckBox::indicator:hover"
                                   "{"
                                   "background-color : " + User_int_utility.primary_color + ";"
                                   "}")
        else:
            self.box.setStyleSheet("QCheckBox {"
                                   "border-radius: 1px;"
                                   "border: 2px solid " + User_int_utility.secondary_color + ";"
                                   "background-color : " + User_int_utility.secondary_color + ";"
                                   "}"
                                   "QCheckBox::indicator"
                                   "{"
                                   "height: 14px;"
                                   "width: 14px;"
                                   "}"
                                   "QCheckBox::indicator:hover"
                                   "{"
                                   "background-color : " + User_int_utility.primary_color + ";"
                                   "}")



