from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGroupBox, QFormLayout, QSizePolicy, QGridLayout, \
    QSpacerItem, QMessageBox

from GestioneClienti.Model.Cliente import Cliente
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

        # vengono aggiunti alla finestra tutti i layout ed i widget necessari
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Cl"), 0, 0, 1, 2)
        ext_layout.addWidget(self.crea_box_anagrafica(), 1, 0)
        ext_layout.addItem(QSpacerItem(10, 50, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0)
        ext_layout.addWidget(self.crea_box_abb_tess(), 2, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/cliente_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Minimum), 1, 1, 5, 1)
        ext_layout.addItem(QSpacerItem(10, 40, QSizePolicy.Expanding, QSizePolicy.Minimum), 3, 0)
        ext_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Conferma", self.add_cliente, QSizePolicy.Minimum,
                                                           QSizePolicy.Expanding, "G"), 4, 0)
        ext_layout.addItem(QSpacerItem(10, 35, QSizePolicy.Expanding, QSizePolicy.Minimum), 5, 0)

        self.setLayout(ext_layout)

    # metodo che restituisce un form layout in cui sono contenuti i widget per l'inserimento
    # dei dati del cliente, ad eccezione della data di nascita, del coidce abbonamento e del codice tessera
    def crea_box_anagrafica(self):
        box = QGroupBox()
        box.setTitle("Dati anagrafici")
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        form = QFormLayout()
        form.setContentsMargins(8, 40, 8, 15)
        oggi = QDate.currentDate()

        # creazione dei widget per l'inserimento dei dati
        self.nome = User_int_utility.crea_casella_testo("Inserire il nome")
        self.cognome = User_int_utility.crea_casella_testo("Inserire il cognome")
        self.data_nascita = User_int_utility.crea_date_edit(oggi.addYears(-120), oggi.addDays(-1))
        self.cod_fisc = User_int_utility.crea_casella_testo("Inserire il codice fiscale")
        self.telefono = User_int_utility.crea_casella_testo("Inserire il numero di telefono")
        self.email = User_int_utility.crea_casella_testo("Inserire l'email")

        # aggiunta dei widget al layout
        form.addRow(User_int_utility.crea_label("Nome"), self.nome)
        form.addRow(User_int_utility.crea_label("Cognome"), self.cognome)
        form.addRow(User_int_utility.crea_label("Data di nascita"), self.data_nascita)
        form.addRow(User_int_utility.crea_label("Codice fiscale"), self.cod_fisc)
        form.addRow(User_int_utility.crea_label("Telefono"), self.telefono)
        form.addRow(User_int_utility.crea_label("Email"), self.email)

        box.setLayout(form)
        return box

    # metodo che crea e restituisce un group box in cui sono contenuti i widget per l'inserimento dei
    # codici di tessera e abbonamento
    def crea_box_abb_tess(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box.setTitle("Assegnazione tessera e/o abbonamento")

        form = QFormLayout()
        form.setContentsMargins(8, 40, 8, 15)

        self.cod_abb = User_int_utility.crea_casella_testo("Se si desidera rilasciare un abbonamento inserire il codice")
        self.cod_tess = User_int_utility.crea_casella_testo("Se si desidera rilasciare una tessera inserire il codice")

        form.addRow(User_int_utility.crea_label("Codice abbonamento"), self.cod_abb)
        form.addRow(User_int_utility.crea_label("Codice tessera"), self.cod_tess)

        box.setLayout(form)
        return box

    # metodo che permette di aggiungere alla lista dei clienti registrati a sistema
    # il cliente di cui sono stati inseriti i dati.
    # Prima viene eseguito un controllo sui dati del cliente, sul codice della tessera(se inserito) e sul codice
    # dell'abbonamento (se inserito).
    # Se il controllo dà esito negativo il cliente non viene aggiunto alla lista e sullo schermo compare un messaaggio di errore
    def add_cliente(self):
        cliente = Cliente(
                self.nome.text(),
                self.cognome.text(),
                self.data_nascita.date(),
                self.cod_fisc.text(),
                self.telefono.text(),
                self.email.text())

        avviso = self.controller.controlla_campi_cliente(cliente, self.cod_abb.text(), self.cod_tess.text())
        if avviso == None:
            self.controller.aggiungi_cliente(cliente, self.cod_abb.text(), self.cod_tess.text())
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.callback()                       # fa riapparire la finestra precedente