from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem

from GestioneClienti.Controllers.ControlloreCliente import ControlloreCliente
from Utilità.User_int_utility import User_int_utility

class VistaModifica(QWidget):
    def __init__(self):
        super(VistaModifica, self).__init__()

        #self.controller = controller

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Modifica")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 325, 110)
        self.setMinimumSize(325, 110)
        self.setMaximumSize(325, 110)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        # aggiunta dei vari elementi che compongono la UI al layout esterno
        ext_layout.addWidget(self.crea_box_dati(), 1, 0)
        ext_layout.addWidget(User_int_utility.crea_push_button("Conferma", self.aggiorna_servizio,
                                                           "Cliccare per confermare la modifica",
                                                           QSizePolicy.Expanding, QSizePolicy.Expanding), 2 , 0)
        self.setLayout(ext_layout)

    # metodo che ritorna il box dove vengono mostrate le informazioni sul dipendente
    def crea_box_dati(self):
        box = QGroupBox()
        box.setTitle("Modifica Dati ")
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        grid = QGridLayout()
        grid.setContentsMargins(8, 30, 8, 15)

        grid.addWidget(User_int_utility.crea_label("Immetti nuovo valore: "), 0, 0)
        grid.addWidget(User_int_utility.crea_casella_testo(), 0, 1)

        box.setLayout(grid)
        return box

    def aggiorna_servizio(self):
        pass
