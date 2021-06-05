from PyQt5.QtWidgets import QPushButton, QSizePolicy, QCheckBox
from Utilità.User_int_utility import User_int_utility

class Posto():
    def __init__(self, fila, posizione, vip):
        self.disponibile = True
        self.fila = fila
        self.posizione = posizione
        self.vip = vip
        self.box = QCheckBox()

    def prenota(self):
        self.disponibile = False
        self.button.setDisabled(True)

    def get_posto(self):
        return {"Fila": self.fila, "Posizione": self.posizione}

    def applica_stile_check_box(self):
        if self.vip == True:
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



