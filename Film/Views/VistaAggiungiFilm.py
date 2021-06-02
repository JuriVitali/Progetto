from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGroupBox, QFormLayout, QSizePolicy, QGridLayout, \
    QSpacerItem, QMessageBox

from Film.Models.Film import Film
from Utilità.User_int_utility import User_int_utility
from Utilità.Controlli import Controlli


class VistaAggiungiFilm(QWidget):

    def __init__(self, controller, callback, parent=None):
        super(VistaAggiungiFilm, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()

        self.setWindowTitle("Inserimento film")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        box_dati = QGroupBox()
        box_dati.setLayout(self.crea_form())
        box_dati.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        self.setStyleSheet("QWidget {background-color : " + User_int_utility.primary_color + ";}"
                          "QGroupBox"
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

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Fi"), 0, 0, 1, 2)
        ext_layout.addItem(QSpacerItem(10, 40, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0)
        ext_layout.addWidget(box_dati, 2, 0)
        ext_layout.addItem(QSpacerItem(10, 120, QSizePolicy.Expanding, QSizePolicy.Minimum), 3, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/film_back.png"), QSizePolicy.Minimum, QSizePolicy.Minimum), 1, 1, 5, 1)
        ext_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Conferma",self.add_film, QSizePolicy.Minimum, QSizePolicy.Expanding,"G"), 4, 0)
        ext_layout.addItem(QSpacerItem(10, 45, QSizePolicy.Expanding, QSizePolicy.Minimum), 5, 0)
        self.setLayout(ext_layout)


    def crea_form(self):
        form = QFormLayout()
        self.titolo = User_int_utility.crea_casella_testo("Inserire il titolo")
        self.casa_prod = User_int_utility.crea_casella_testo("Inserire la casa di produzione")
        self.durata = User_int_utility.crea_spin_box(1, 500, 90)
        self.genere = User_int_utility.crea_casella_testo("Inserire il genere")
        self.eta_minima = User_int_utility.crea_combo_box(Controlli.eta_minima)

        form.addRow(User_int_utility.crea_label("Titolo"), self.titolo)
        form.addRow(User_int_utility.crea_label("Casa di produzione"), self.casa_prod)
        form.addRow(User_int_utility.crea_label("Durata (in minuti)"), self.durata)
        form.addRow(User_int_utility.crea_label("Genere"), self.genere)
        form.addRow(User_int_utility.crea_label("Età minima"), self.eta_minima)
        return form

    def add_film(self):
        eta_minima = Controlli.eta_minima[self.eta_minima.currentIndex()]
        film = Film(self.titolo.text(),
                    self.casa_prod.text(),
                    self.durata.text(),
                    self.genere.text(),
                    eta_minima)
        avviso = self.controller.controlla_campi_film(film)
        if  avviso == None:
            self.controller.aggiungi_film(film)
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.callback()