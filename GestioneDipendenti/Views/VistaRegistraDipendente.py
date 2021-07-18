from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGroupBox, QFormLayout, QSizePolicy, QGridLayout, \
    QSpacerItem, QMessageBox

from GestioneDipendenti.Models.Dipendente import Dipendente
from Utilità.User_int_utility import User_int_utility
from Utilità.Parametri import Parametri


class VistaRegistraDipendente(QWidget):

    def __init__(self, controller, callback, parent=None):
        super(VistaRegistraDipendente, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()                                     #fa scomparire la finestra precedente

        self.setWindowTitle("Registrazione dipendente")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)             #sposta la finestra al centro dello schermo
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        box_dati = QGroupBox()
        box_dati.setTitle("Dati del nuovo dipendente")
        box_dati.setLayout(self.crea_form())                #viene creato il box contenente i widget per l'inserimento dei dati
        box_dati.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        # vengono aggiunti alla finestra tutti i layout ed i widget necessari
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Di"), 0, 0, 1, 2)
        ext_layout.addWidget(box_dati, 1, 0)
        ext_layout.addItem(QSpacerItem(10, 50, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum, QSizePolicy.Minimum), 1, 1, 5, 1)
        ext_layout.addItem(QSpacerItem(10, 30, QSizePolicy.Expanding, QSizePolicy.Minimum), 3, 0)
        ext_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Conferma", self.add_dipendente, QSizePolicy.Minimum, QSizePolicy.Expanding, "G"), 4, 0)
        ext_layout.addItem(QSpacerItem(10, 45, QSizePolicy.Expanding, QSizePolicy.Minimum), 5, 0)
        self.setLayout(ext_layout)

    # metodo che restituisce un form layout in cui sono contenuti i widget per l'inserimento
    # dei dati del dipendente, ad eccezione della data di nascita
    def crea_form(self):
        form = QFormLayout()
        form.setContentsMargins(8, 40, 8, 12)
        oggi = QDate.currentDate()

        # creazione dei widget per l'inserimento dei dati
        self.lista_aree_competenza = ["Biglietteria", "Bar", "Pulizie"]
        self.nome = User_int_utility.crea_casella_testo("Inserire il nome")
        self.cognome = User_int_utility.crea_casella_testo("Inserire il cognome")
        self.data_nascita = User_int_utility.crea_date_edit(oggi.addYears(-90), oggi.addYears(-16))
        self.cod_fisc = User_int_utility.crea_casella_testo("Inserire il codice fiscale")
        self.telefono = User_int_utility.crea_casella_testo("Inserire il numero di telefono")
        self.email = User_int_utility.crea_casella_testo("Inserire l'email")
        self.cod_autent = User_int_utility.crea_casella_testo("Inserire solo per dipendenti della biglietteria")
        self.area_comp = User_int_utility.crea_combo_box(Parametri.aree_di_competenza)

        # aggiunta dei widget al layout
        form.addRow(User_int_utility.crea_label("Nome"), self.nome)
        form.addRow(User_int_utility.crea_label("Cognome"), self.cognome)
        form.addRow(User_int_utility.crea_label("Data di nascita"), self.data_nascita)
        form.addRow(User_int_utility.crea_label("Codice fiscale"), self.cod_fisc)
        form.addRow(User_int_utility.crea_label("Telefono"), self.telefono)
        form.addRow(User_int_utility.crea_label("Email"), self.email)
        form.addRow(User_int_utility.crea_label("Area di competenza"), self.area_comp)
        form.addRow(User_int_utility.crea_label("Codice autenticazione"), self.cod_autent)
        return form

    # metodo che permette di aggiungere il dipendente di cui sono stati inseriti i dati alla lista.
    # prima viene eseguito un controllo sui dati. Se esso dà esito negativo il dipendente non viene aggiunto alla
    # lista e sullo schermo compare un messaaggio di errore
    def add_dipendente(self):
        area_competenza = Parametri.aree_di_competenza[self.area_comp.currentIndex()]

        if area_competenza == "Biglietteria":
            dipendente = Dipendente(
                self.nome.text(),
                self.cognome.text(),
                self.data_nascita.date(),
                self.cod_fisc.text(),
                self.telefono.text(),
                self.email.text(),
                area_competenza,
                self.cod_autent.text())
        else:
            dipendente = Dipendente(
                self.nome.text(),
                self.cognome.text(),
                self.data_nascita.date(),
                self.cod_fisc.text(),
                self.telefono.text(),
                self.email.text(),
                area_competenza)
        avviso = self.controller.controlla_campi_dipendente(dipendente)
        if avviso == None:
            self.controller.aggiungi_dipendente(dipendente)
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.callback()                             # fa riapparire la finestra precedente