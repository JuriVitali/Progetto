from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem

from GestioneClienti.Controllers.ControlloreCliente import ControlloreCliente
from Utilità.User_int_utility import User_int_utility

class VistaVisualizzaInfoCliente(QWidget):
    def __init__(self, cliente, callback):
        super(VistaVisualizzaInfoCliente, self).__init__()

        self.controller = ControlloreCliente(cliente)

        self.callback = callback
        self.callback()         #fa scomparire la finestra precedente


        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione info ")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)


        # aggiunta dei vari elementi che compongono la UI al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Di"), 0, 0, 1, 2)
        ext_layout.addWidget(self.crea_box_dati(), 1, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 1, 2, 1)
        ext_layout.addItem(QSpacerItem(10, 190, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0, 1, 2)
        self.setLayout(ext_layout)


    # metodo che ritorna il box dove vengono mostrate le informazioni sul dipendente
    def crea_box_dati(self):
        box = QGroupBox()
        box.setTitle("Dati di " + self.controller.get_cognome() + " " + self.controller.get_nome())
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        grid = QGridLayout()
        grid.setContentsMargins(8, 30, 8, 15)

        grid.addWidget(User_int_utility.crea_label("Nome: \nCognome: \nData di nascita: \nCodice fiscale: \nEmail: \nCodice abbonamento: \nCodice tessera: "), 0, 0)
        grid.addWidget(User_int_utility.crea_label(self.controller.get_nome() + "\n"
                                                      + self.controller.get_cognome() + "\n"
                                                      + self.controller.get_data_nascita().toString("yyyy.MM.dd") + "\n"
                                                      + self.controller.get_cod_fisc() + "\n"
                                                      + self.controller.get_email() + "\n"
                                                      + self.controller.get_cod_abb() + "\n"
                                                      + self.controller.get_cod_tess()), 0, 1)
        box.setLayout(grid)
        return box

    def closeEvent(self, event):
        self.callback()                 #fa riapparire la finestra precedente