from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget,QFormLayout, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox, QHBoxLayout

from Utilità.User_int_utility import User_int_utility
from GestioneServizi.Views.VistaModifica import VistaModifica

class VistaGestisciServizi(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaGestisciServizi, self).__init__()

        #self.controller = controller

        self.callback = callback
        self.callback()

        self.setWindowTitle("Gestione Servizi")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        self.list_view = User_int_utility.crea_list_view()
        #self.update_ui()

        butt_layout = QHBoxLayout()

        butt_layout.addWidget(User_int_utility.crea_push_button("Biglietto", self.show_biglietto,
                                                                "Cliccare per visualizzare le informazioni relative al biglietto",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding))
        butt_layout.addWidget(User_int_utility.crea_push_button("Tessera", self.show_biglietto,
                                                                "Cliccare per visualizzare le informazioni relative al biglietto",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding))
        butt_layout.addWidget(User_int_utility.crea_push_button("Abbonamento", self.show_biglietto,
                                                                "Cliccare per visualizzare le informazioni relative al biglietto",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding))

        butt2_layout =QHBoxLayout()

        butt2_layout.addWidget(User_int_utility.crea_push_button("Modifica", self.modifica,
                                                                "Cliccare per modificare il valore selezionato",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding))

        box_biglietto = self.crea_box_biglietto()

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Cl"), 0, 0, 1, 2)
        #ext_layout.addWidget(box_biglietto, 2, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 1, 2, 1)
        ext_layout.addLayout(butt_layout, 1, 0)
        ext_layout.addWidget(self.list_view, 2, 0)
        ext_layout.addLayout(butt2_layout, 3, 0)
        self.setLayout(ext_layout)

    def show_biglietto(self):
        pass

    def modifica(self):
        self.vista_modifica = VistaModifica()
        self.vista_modifica.show()

    def crea_box_biglietto(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box.setTitle("Se si desidera rilasciare al cliente una tessera e/o un abbonamento inserire i rispettivi codici ")
        form = QFormLayout()
        form.setContentsMargins(8, 30, 8, 8)

        self.cod_abb = User_int_utility.crea_casella_testo("Inserire il codice abbonamento")
        self.cod_tess = User_int_utility.crea_casella_testo("Inserire il codice tessera")

        form.addRow(User_int_utility.crea_label("Codice abbonamento"), self.cod_abb)
        form.addRow(User_int_utility.crea_label("Codice tessera"), self.cod_tess)

        box.setLayout(form)
        return box

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        #self.controller.save_data()
        self.callback()