from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox

from Utilità.User_int_utility import User_int_utility

class VistaRilasciaAbbonamento(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaRilasciaAbbonamento, self).__init__()

        #self.controller = controller

        self.callback = callback
        self.callback()

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Rilascio Tessera")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)           #sposta la finestra al centro dello schermo

        # Creazione di un layout a griglia interno contenente i vari widget e l'immagine
        grid_layout = QGridLayout()
        grid_layout.addItem(QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Minimum), 1, 0, 1, 2)
        grid_layout.addWidget(self.crea_box_ricerca(), 0, 0)
        grid_layout.addWidget(self.crea_box_descrizione_tess(), 2, 0)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/cliente_back.png"), QSizePolicy.Minimum, QSizePolicy.Minimum),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20, 0, 0, 0)

        # aggiunta dei due layout al layout esterno
        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Ab"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)

    # metodo che crea il box contenente i widget per la ricerca di un cliente in base al nome e al cognome
    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Rilascio Abbonamento")
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

        self.nome_ricerca = User_int_utility.crea_casella_testo("Inserire il codice fiscale del cliente")
        self.cognome_ricerca = User_int_utility.crea_casella_testo("Inserire il codice dell'abbonamento'")

        layout.addWidget(User_int_utility.crea_label("Codice fiscale del cliente"), 0, 0)
        layout.addWidget(User_int_utility.crea_label("Codice dell'abbonamento"), 1, 0)
        layout.addWidget(self.nome_ricerca, 0, 1)
        layout.addWidget(self.cognome_ricerca, 1, 1)
        layout.addItem(QSpacerItem(60, 10, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2, 2, 1)
        layout.addWidget(User_int_utility.crea_push_button("Conferma", self.rilascia_tessera,
                                                           "Cliccare per rilasciare l'abbonamento'",
                                                           QSizePolicy.Expanding, QSizePolicy.Expanding), 0, 3, 2, 1)
        box.setLayout(layout)
        return box

    def rilascia_tessera(self):
        pass

    def crea_box_descrizione_tess(self):
        box = QGroupBox()
        box.setTitle("Funzionamento Abbonamento ")
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        grid = QGridLayout()
        grid.setContentsMargins(8, 30, 8, 15)

        grid.addWidget(User_int_utility.crea_label("L’abbonamento prevede, a fronte del pagamento di una certa somma (decisa dall’amministratore) "
                                                   "\nal momento del rilascio, la possibilità di usufruire di un certo numero di ingressi entro la data di "
                                                   "\nscadenza (l’abbonamento non consente di prenotare poltrone premium)."
                                                   "\nUn cliente ha la possibilità di registrarsi fornendo i propri dati anagrafici"),0, 0)
        box.setLayout(grid)
        return box

    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        #self.controller.save_data()              #salvataggio dei dati
        self.callback()                          #fa riapparire la finestra precedente
