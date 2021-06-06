from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox

from GestioneClienti.Controllers.ControlloreListaClienti import ControlloreListaClienti
#from GestioneClienti.Views.VistaVisualizzaClienti import VistaVisualizzaClienti
from Utilità.User_int_utility import User_int_utility
#from GestioneClienti.Views.VistaRegistraCliente import VistaRegistraCliente


class VistaGestisciCliente(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaGestisciCliente, self).__init__()
        print("0")

        self.controller = ControlloreListaClienti()

        print("1")

        self.callback = callback
        self.callback()

        print("2")

        self.setWindowTitle("Gestione Clienti")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)

        print("3")

        grid_layout = QGridLayout()
        print("4")
        grid_layout.addWidget(User_int_utility.crea_push_button("Registra Cliente", self.show_new_cliente,
                                                                "Cliccare per aggiungere un cliente al sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza tutti i clienti", self.show_lista_clienti_completa,
                                              "Cliccare per visualizzare tutti i clienti inseriti nel sistema",
                                              QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        grid_layout.addItem(QSpacerItem(20, 95, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        print("5")
        grid_layout.addWidget(self.crea_box_ricerca(), 2, 0, 1, 2)
        print("6")
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum, QSizePolicy.Expanding),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20, 0, 0, 0)

        print("7")

        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Cl"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)


    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Cerca un cliente")
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
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
        layout.addWidget(User_int_utility.crea_push_button("Cerca dipendente", self.show_lista_clienti_filtrata,
                                                           "Cliccare per ricercare il cliente",
                                                           QSizePolicy.Expanding, QSizePolicy.Expanding), 0, 3, 2, 1)
        box.setLayout(layout)
        return box

    def show_new_cliente(self):
        #self.vista_registra_cliente = VistaRegistraCliente(self.controller, self.modifica_visibilita)
        #self.vista_registra_cliente.show()
        pass


        # Dopo aver verificato i campi inseriti apre la vista per la visualizzazione dei dipendenti se essi sono corretti,
        # altrimenti genera un avviso
    def show_lista_clienti_filtrata(self):
            '''avviso = self.controller.controlla_campi_ricerca(self.nome_ricerca.text(), self.cognome_ricerca.text())
            if avviso == None:
                self.vista_lista_clienti = VistaVisualizzaClienti(self.controller, self.modifica_visibilita,
                                                                        self.nome_ricerca.text(),
                                                                        self.cognome_ricerca.text())
                self.vista_lista_clienti.show()
            else:
                QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok) '''
            pass

    def show_lista_clienti_completa(self):
            #self.vista_lista_clienti = VistaVisualizzaClienti(self.controller, self.modifica_visibilita)
            #self.vista_lista_clienti.show()
            pass

    def modifica_visibilita(self):
            User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
            self.controller.save_data()
            self.callback()
