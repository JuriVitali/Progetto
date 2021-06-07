from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGroupBox, QFormLayout, QSizePolicy, QGridLayout, \
    QSpacerItem, QMessageBox

from GestioneClienti.Models.Cliente import Cliente
from Utilità.User_int_utility import User_int_utility

class VistaRegistraCliente(QWidget):
    def __init__(self, controller, callback, parent=None):
        super(VistaRegistraCliente, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()                                     # fa scomparire la finestra precedente

        self.setWindowTitle("Registrazione cliente")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)             # sposta la finestra al centro dello schermo
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        box_dati = QGroupBox()
        box_dati.setLayout(self.crea_form())                # viene creato il box contenente i widget per l'inserimento dei dati
        box_dati.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        box_data_n = self.crea_box_nascita()  # viene creato il box contenente i widget per l'inserimento della data di nascita

        box_abb_tess = self.crea_box_abb_tess()

        # vengono aggiunti alla finestra tutti i layout ed i widget necessari
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Cl"), 0, 0, 1, 2)
        ext_layout.addWidget(box_dati, 1, 0)
        ext_layout.addItem(QSpacerItem(10, 50, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0)
        ext_layout.addWidget(box_data_n, 2, 0)
        ext_layout.addWidget(box_abb_tess, 3, 0)
        ext_layout.addWidget(
            User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Minimum), 1, 1, 5, 1)
        ext_layout.addItem(QSpacerItem(10, 50, QSizePolicy.Expanding, QSizePolicy.Minimum), 4, 0)
        ext_layout.addWidget(
            User_int_utility.crea_green_or_red_push_button("Conferma", self.add_cliente, QSizePolicy.Minimum,
                                                           QSizePolicy.Expanding, "G"), 5, 0)
        self.setLayout(ext_layout)

    # metodo che restituisce un form layout in cui sono contenuti i widget per l'inserimento
    # dei dati del dipendente, ad eccezione della data di nascita
    def crea_form(self):
        form = QFormLayout()

        # creazione dei widget per l'inserimento dei dati
        self.nome = User_int_utility.crea_casella_testo("Inserire il nome")
        self.cognome = User_int_utility.crea_casella_testo("Inserire il cognome")
        self.cod_fisc = User_int_utility.crea_casella_testo("Inserire il codice fiscale")
        self.email = User_int_utility.crea_casella_testo("Inserire l'email")

        # aggiunta dei widget al layout
        form.addRow(User_int_utility.crea_label("Nome"), self.nome)
        form.addRow(User_int_utility.crea_label("Cognome"), self.cognome)
        form.addRow(User_int_utility.crea_label("Codice fiscale"), self.cod_fisc)
        form.addRow(User_int_utility.crea_label("Email"), self.email)
        return form

    def crea_box_abb_tess(self):
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

    def crea_box_nascita(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box.setTitle("Data di nascita")
        grid = QGridLayout()
        grid.setContentsMargins(8, 30, 8, 8)

        self.giorno_n = User_int_utility.crea_spin_box(1, 31, 1)
        self.mese_n = User_int_utility.crea_spin_box(1, 12, 1)
        oggi = QDate.currentDate()
        self.anno_n = User_int_utility.crea_spin_box(1940, (oggi.year() - 16), 1980)

        grid.addWidget(User_int_utility.crea_label("Giorno"), 0, 0)
        grid.addWidget(User_int_utility.crea_label("Mese"), 0, 1)
        grid.addWidget(User_int_utility.crea_label("Anno"), 0, 2)
        grid.addWidget(self.giorno_n, 1, 0)
        grid.addWidget(self.mese_n, 1, 1)
        grid.addWidget(self.anno_n, 1, 2)

        box.setLayout(grid)
        return box

    # metodo che permette di aggiungere il dipendente di cui sono stati inseriti i dati alla lista.
    # prima viene eseguito un controllo sui dati. Se esso dà esito negativo il dipendente non viene aggiunto alla
    # lista e sullo schermo compare un messaaggio di errore
    def add_cliente(self):
        data_nascita = QDate(self.anno_n.value(), self.mese_n.value(), self.giorno_n.value())

        cliente = Cliente(
                self.nome.text(),
                self.cognome.text(),
                data_nascita,
                self.cod_fisc.text(),
                self.email.text(),
                self.cod_abb.text(),
                self.cod_tess.text())
        self.controller.aggiungi_cliente(cliente)
        self.close()
        '''avviso = self.controller.controlla_campi_cliente(cliente)
        if avviso == None:
            self.controller.aggiungi_cliente(cliente)
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)'''

    def closeEvent(self, event):
        self.callback()                       # fa riapparire la finestra precedente