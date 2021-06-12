from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox

from Utilità.User_int_utility import User_int_utility

class VistaRilasciaTessera(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaRilasciaTessera, self).__init__()

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
        #grid_layout.addItem(QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Minimum), 1, 0, 1, 2)
        grid_layout.addWidget(self.crea_box_ricerca(), 0, 0)
        grid_layout.addWidget(self.crea_box_descrizione_tess(), 1, 0)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/cliente_back.png"), QSizePolicy.Minimum, QSizePolicy.Minimum),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20, 0, 0, 0)

        # aggiunta dei due layout al layout esterno
        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Te"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)

    # metodo che crea il box contenente i widget per la ricerca di un cliente in base al nome e al cognome
    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Rilascio Tessera")
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
        self.cognome_ricerca = User_int_utility.crea_casella_testo("Inserire il codice della tessera")

        layout.addWidget(User_int_utility.crea_label("Codice fiscale del cliente"), 0, 0)
        layout.addWidget(User_int_utility.crea_label("Codice della tessera"), 1, 0)
        layout.addWidget(self.nome_ricerca, 0, 1)
        layout.addWidget(self.cognome_ricerca, 1, 1)
        layout.addItem(QSpacerItem(60, 10, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2, 2, 1)
        layout.addWidget(User_int_utility.crea_push_button("Conferma", self.rilascia_tessera,
                                                           "Cliccare per rilasciare la tessera",
                                                           QSizePolicy.Expanding, QSizePolicy.Expanding), 0, 3, 2, 1)
        box.setLayout(layout)
        return box

    def rilascia_tessera(self):
        pass

    def crea_box_descrizione_tess(self):
        box = QGroupBox()
        box.setTitle("Funzionamento Tessera ")
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        grid = QGridLayout()
        grid.setContentsMargins(8, 30, 8, 15)

        grid.addWidget(User_int_utility.crea_label("La tessera ha un costo (deciso dall’amministratore) che viene pagato al momento del rilascio. "
                                                   "\nIl cliente che possiede la tessera può mostrarla al personale di biglietteria ogni volta che "
                                                   "\nacquista un biglietto e in tale occasione sulla tessera vengono caricati un numero di punti pari "
                                                   "\na 10 volte l’importo del biglietto. Quando i punti accumulati da un cliente sulla sua tessera "
                                                   "\nraggiungono una certa soglia prefissata, viene applicato uno sconto sul prezzo del prossimo "
                                                   "\nbiglietto acquistato da tale cliente; nel momento in cui viene applicato lo sconto, viene sottratta "
                                                   "\nal saldo dei punti una quantità di punti pari alla soglia prefissata. "),0, 0)
        box.setLayout(grid)
        return box

    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        #self.controller.save_data()              #salvataggio dei dati
        self.callback()                          #fa riapparire la finestra precedente
