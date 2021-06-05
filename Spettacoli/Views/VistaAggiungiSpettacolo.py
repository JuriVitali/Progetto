from PyQt5.QtCore import QTime
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem, QMessageBox

from Spettacoli.Model.Posto import Posto
from Utilità.User_int_utility import User_int_utility
from Spettacoli.Model.Sala import Sala
from Utilità.Parametri import Parametri
from Spettacoli.Model.Spettacolo import Spettacolo


class VistaAggiungiSpettacoli(QWidget):
    def __init__(self, controller, callback, data, update_vis_spettacoli):
        super(VistaAggiungiSpettacoli, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()

        self.update_vis_spettacoli = update_vis_spettacoli

        self.data = data
        self.lista_film = []

        self.setWindowTitle("Nuovo spettacolo")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Sp"), 0, 0, 1, 3)
        ext_layout.addWidget(self.crea_box_ricerca_titolo(), 1, 0, 1, 2)
        ext_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0, 1, 2)
        ext_layout.addWidget(self.crea_box_orario(), 3, 0)
        ext_layout.addWidget(self.crea_box_sala(), 3, 1)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/spett_background.png"), QSizePolicy.Minimum, QSizePolicy.Minimum), 1, 2, 5, 1)
        ext_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 4, 0, 1, 2)
        ext_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Conferma", self.add_spettacolo,
                                                                            QSizePolicy.Expanding, QSizePolicy.Expanding,
                                                                            "G"), 5, 0, 1, 2)

        self.setLayout(ext_layout)
        self.show()

    def crea_box_ricerca_titolo(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        box.setTitle("Selezione film")
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 35, 8, 8)

        self.list_view = User_int_utility.crea_list_view()
        self.titolo_cercato = User_int_utility.crea_casella_testo("Inserire il titolo del film")

        box_layout.addWidget(User_int_utility.crea_label("Film "), 0, 0)
        box_layout.addWidget(self.titolo_cercato, 0, 1)
        box_layout.addWidget(User_int_utility.crea_push_button("Cerca", self.cerca_film, "", QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 2)
        box_layout.addWidget(self.list_view, 1, 0, 1, 3)

        box.setLayout(box_layout)
        return box

    def crea_box_orario(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box.setTitle("Selezione orario di inizio e sala")
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 35, 8, 8)

        self.ora = User_int_utility.crea_spin_box(14, 23, 14)
        self.minuti = User_int_utility.crea_spin_box(0, 59, 0, 5)

        box_layout.addWidget(User_int_utility.crea_label("Orario di inizio "), 1, 0)
        box_layout.addWidget(User_int_utility.crea_label("Ora"), 0, 1)
        box_layout.addWidget(User_int_utility.crea_label("Minuti"), 0, 2)
        box_layout.addWidget(self.ora, 1, 1)
        box_layout.addWidget(self.minuti, 1, 2)

        box.setLayout(box_layout)
        return box

    def crea_box_sala(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box.setTitle("Selezione orario di inizio e sala")
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 35, 8, 8)

        self.sala = User_int_utility.crea_combo_box(Parametri.sale)

        box_layout.addWidget(User_int_utility.crea_label("Sala "), 0, 0)
        box_layout.addWidget(self.sala, 0, 1)

        box.setLayout(box_layout)
        return box


    def cerca_film(self):
        self.lista_film = self.controller.ricerca_film(self.titolo_cercato.text())
        self.update_ui()

    def add_spettacolo(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            film_selezionato = self.lista_film[index]

            ora_inizio = QTime(self.ora.value(), self.minuti.value())
            sala_scelta = Parametri.sale[self.sala.currentIndex()]

            if sala_scelta == Parametri.sale[0]:
                sala = Sala(Parametri.sale[0], Parametri.file_sala_1, Parametri.lunghezza_file_sala_1, Parametri.file_vip_sala_1)
            elif sala_scelta == Parametri.sale[1]:
                sala = Sala(Parametri.sale[1], Parametri.file_sala_2, Parametri.lunghezza_file_sala_2, Parametri.file_vip_sala_2)
            elif sala_scelta == Parametri.sale[2]:
                sala = Sala(Parametri.sale[2], Parametri.file_sala_3, Parametri.lunghezza_file_sala_3, Parametri.file_vip_sala_3)
            else:
                sala = Sala(Parametri.sale[3], Parametri.file_sala_4, Parametri.lunghezza_file_sala_4, Parametri.file_vip_sala_4)

            nuovo_spettacolo = Spettacolo(film_selezionato, self.data, ora_inizio, sala)
            avviso = self.controller.controlla_campi_spettacolo(nuovo_spettacolo)
            if avviso == None:
                self.controller.aggiungi_spettacolo(nuovo_spettacolo)
                self.update_vis_spettacoli()
                self.close()
            else:
                QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Errore', "Non è stato selezionato alcun film", QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.callback()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for film in self.lista_film:
            item = QStandardItem()
            item.setText(film.titolo)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


