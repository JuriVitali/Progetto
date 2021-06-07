from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem

from GestioneClienti.Controllers.ControlloreCliente import ControlloreCliente
from Utilità.User_int_utility import User_int_utility

class VistaVisualizzaTessera(QWidget):
    def __init__(self, cliente, callback):
        super(VistaVisualizzaTessera, self).__init__()

        self.controller = ControlloreCliente(cliente)

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione info tessera")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 325, 150)
        self.setMinimumSize(325,150)
        self.setMaximumSize(325, 150)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        # aggiunta dei vari elementi che compongono la UI al layout esterno
        ext_layout.addWidget(self.crea_box_dati(), 1, 0)
        self.setLayout(ext_layout)

    # metodo che ritorna il box dove vengono mostrate le informazioni sul dipendente
    def crea_box_dati(self):
        box = QGroupBox()
        box.setTitle("Dati di " + self.controller.get_cognome() + " " + self.controller.get_nome())
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        grid = QGridLayout()
        grid.setContentsMargins(8, 30, 8, 15)

        grid.addWidget(User_int_utility.crea_label("Codice tessera: \nPunti accumulati: "), 0, 0)
        grid.addWidget(User_int_utility.crea_label(self.controller.get_cod_tess() + "\n"+ "-"), 0, 1)

        box.setLayout(grid)
        return box

    def closeEvent(self, event):
        self.close()