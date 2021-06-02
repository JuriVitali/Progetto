from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox

from GestioneDipendenti.Controllers.ControlloreListaDipendenti import ControlloreListaDipendenti
from GestioneDipendenti.Views.VistaVisualizzaDipendenti import VistaVisualizzaDipendenti
from Utilità.User_int_utility import User_int_utility
from GestioneDipendenti.Views.VistaRegistraDipendente import VistaRegistraDipendente


class VistaGestisciDipendente(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaGestisciDipendente, self).__init__()

        self.controller = ControlloreListaDipendenti()

        self.callback = callback
        self.callback()

        self.setWindowTitle("Gestione Dipendenti")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)

        grid_layout = QGridLayout()
        grid_layout.addWidget(User_int_utility.crea_push_button("Registra dipendente", self.show_new_dipendente,
                                                                "Cliccare per aggiungere un dipendente al sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza tutti i dipendenti", self.show_lista_dipendenti_completa,
                                                                "Cliccare per visualizzare tutti i dipendenti inseriti nel sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        grid_layout.addItem(QSpacerItem(20, 95, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        grid_layout.addWidget(self.crea_box_ricerca(), 2, 0, 1, 2)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum, QSizePolicy.Expanding),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20, 0, 0, 0)

        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Di"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)


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

        self.nome_ricerca = User_int_utility.crea_casella_testo("Inserire il nome")
        self.cognome_ricerca = User_int_utility.crea_casella_testo("Inserire il cognome")

        layout.addWidget(User_int_utility.crea_label("Nome"), 0, 0)
        layout.addWidget(User_int_utility.crea_label("Cognome"), 1, 0)
        layout.addWidget(self.nome_ricerca, 0, 1)
        layout.addWidget(self.cognome_ricerca, 1, 1)
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2, 2, 1)
        layout.addWidget(User_int_utility.crea_push_button("Cerca dipendente", self.show_lista_dipendenti_filtrata,
                                              "Cliccare per ricercare il dipendente",
                                              QSizePolicy.Expanding, QSizePolicy.Expanding), 0, 3, 2, 1)
        box.setLayout(layout)
        return box

    def show_new_dipendente(self):
        self.vista_registra_dipendente = VistaRegistraDipendente(self.controller, self.modifica_visibilita)
        self.vista_registra_dipendente.show()

    #Dopo aver verificato i campi inseriti apre la vista per la visualizzazione dei dipendenti se essi sono corretti,
    #altrimenti genera un avviso
    def show_lista_dipendenti_filtrata(self):
        avviso = self.controller.controlla_campi_ricerca(self.nome_ricerca.text(), self.cognome_ricerca.text())
        if avviso == None:
            self.vista_lista_dipendenti = VistaVisualizzaDipendenti(self.controller,self.modifica_visibilita,
                                                                    self.nome_ricerca.text(), self.cognome_ricerca.text())
            self.vista_lista_dipendenti.show()
        else:
            QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)

    def show_lista_dipendenti_completa(self):
        self.vista_lista_dipendenti = VistaVisualizzaDipendenti(self.controller, self.modifica_visibilita)
        self.vista_lista_dipendenti.show()

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data()
        self.callback()