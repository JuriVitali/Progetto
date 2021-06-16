from PyQt5.QtWidgets import QWidget, QGridLayout

from Utilità.User_int_utility import User_int_utility

class VistaInserimentoDatiBiglietti(QWidget):
    def __init__(self, spettacolo, controller, callback):
        super(VistaInserimentoDatiBiglietti, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()

        self.spettacolo = spettacolo

        self.setWindowTitle("Inserimento dei dati dei biglietti")
        self.setGeometry(0, 0, 1300, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

