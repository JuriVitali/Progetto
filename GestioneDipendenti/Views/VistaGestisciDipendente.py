from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem

from GestioneDipendenti.Controllers.ControlloreGestisciDipendenti import ControlloreGestisciDipendenti
from Utilità.User_int_utility import User_int_utility


class VistaGestisciDipendente(QWidget):
    def __init__(self, parent=None):
        super(VistaGestisciDipendente, self).__init__()
        self.controller = ControlloreGestisciDipendenti()

        self.setWindowTitle("Gestione Dipendenti")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(User_int_utility.geometry[0], User_int_utility.geometry[1], 50, 50)

        grid_layout = QGridLayout()
        grid_layout.addWidget(User_int_utility.crea_push_button("Registra dipendente", self.show_new_dipendente,
                                                                "Cliccare per aggiungere un dipendente al sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza tutti i dipendenti", self.show_lista_dipendenti,
                                                                "Cliccare per visualizzare tutti i dipendenti inseriti nel sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        grid_layout.addItem(QSpacerItem(20, 95, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        grid_layout.addWidget(self.crea_box_ricerca(), 2, 0, 1, 2)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum, QSizePolicy.Expanding),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20,28,0, 20)

        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Di"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)


    def show_new_dipendente(self):
        pass

    def show_lista_dipendenti(self, nome=None, cognome=None):
        pass

    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Cerca un dipendente")
        box.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        box.setStyleSheet("QGroupBox"
                          "{"
                          "background-color: #222;"
                          "border-radius: 8px"
                          "}"
                          "QGroupBox::title"
                          "{"
                          "background-color: " + User_int_utility.tertiary_color + ";"
                          "border-radius: 4px"
                          "}"
                          )
        layout = QGridLayout()

        self.nome_ricerca = User_int_utility.crea_casella_testo()
        self.cognome_ricerca = User_int_utility.crea_casella_testo()

        layout.addWidget(User_int_utility.crea_label("Nome"), 0, 0)
        layout.addWidget(User_int_utility.crea_label("Cognome"), 1, 0)
        layout.addWidget(self.nome_ricerca, 0, 1)
        layout.addWidget(self.cognome_ricerca, 1, 1)
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2, 2, 1)
        layout.addWidget(User_int_utility.crea_push_button("Cerca dipendente", self.show_lista_dipendenti,
                                              "Cliccare per ricercare il dipendente",
                                              QSizePolicy.Expanding, QSizePolicy.Expanding), 0, 3, 2, 1)
        box.setLayout(layout)
        return box

    def closeEvent(self, event):
        pass
        #self.controller.save_data()