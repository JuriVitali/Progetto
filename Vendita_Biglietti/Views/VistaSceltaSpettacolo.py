
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QSizePolicy

from Spettacoli.Controllers.ControlloreListaSpettacoli import ControlloreListaSpettacoli
from Utilità.Parametri import Parametri
from Utilità.User_int_utility import User_int_utility
from Vendita_Biglietti.Views.VistaMappaPosti import VistaMappaPosti


class VistaSceltaSpettacolo(QWidget):
    def __init__(self, callback):
        super(VistaSceltaSpettacolo, self).__init__()

        self.controller = ControlloreListaSpettacoli()

        self.ritorna_home = [self.close]

        self.callback = callback
        self.callback()

        self.setWindowTitle("Scelta spettacolo")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Bi"), 0, 0)
        ext_layout.addLayout(self.crea_group_boxes(), 1, 0)

        self.setLayout(ext_layout)

    def crea_group_boxes(self):
        griglia_boxes = QGridLayout()

        self.lista_list_view = []
        self.listviews_models = []
        self.lista_spettacoli_oggi = self.controller.get_spettacoli_by_day(QDate.currentDate())
        lista_funzioni_selezione = [self.seleziona_spettacolo_sala_1, self.seleziona_spettacolo_sala_2,
                                    self.seleziona_spettacolo_sala_3, self.seleziona_spettacolo_sala_4]

        i = 0
        for sala in Parametri.sale:
            box = QGroupBox()
            box.setTitle(sala)
            box_layout = QVBoxLayout()
            box_layout.setContentsMargins(8, 40, 8, 8)

            list_view = User_int_utility.crea_list_view()

            self.popola_list_view(list_view, i+1)
            self.lista_list_view.append(list_view)

            box_layout.addWidget(list_view)
            box_layout.addWidget(User_int_utility.crea_push_button("Seleziona spettacolo", lista_funzioni_selezione[i],
                                                                   "", QSizePolicy.Expanding, QSizePolicy.Minimum))
            box.setLayout(box_layout)

            griglia_boxes.addWidget(box, i//2, i%2)
            i=i+1

        return griglia_boxes

    def popola_list_view(self, list_view, numero_sala):
        self.listviews_models.append(QStandardItemModel(list_view))
        spettacoli_sala = self.lista_spettacoli_oggi[numero_sala-1]

        if len(spettacoli_sala) > 0:
            for spettacolo in spettacoli_sala:
                item = QStandardItem()
                item.setText(spettacolo.ora_inizio.toString("HH:mm") + "-" + spettacolo.ora_fine.toString(
                    "HH:mm") + "    " + spettacolo.film.titolo)
                item.setEditable(False)
                self.listviews_models[numero_sala-1].appendRow(item)
        else:
            item = QStandardItem()
            item.setText("Nessuno spettacolo in programma")
            item.setEditable(False)
            item.setSelectable(False)
            self.listviews_models[numero_sala-1].appendRow(item)
        list_view.setModel(self.listviews_models[numero_sala-1])

    def seleziona_spettacolo_sala_1(self):
        if (len(self.lista_list_view[0].selectedIndexes()) > 0):
            index = self.lista_list_view[0].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[0][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    def seleziona_spettacolo_sala_2(self):
        if (len(self.lista_list_view[1].selectedIndexes()) > 0):
            index = self.lista_list_view[1].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[1][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    def seleziona_spettacolo_sala_3(self):
        if (len(self.lista_list_view[2].selectedIndexes()) > 0):
            index = self.lista_list_view[2].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[2][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    def seleziona_spettacolo_sala_4(self):
        if (len(self.lista_list_view[3].selectedIndexes()) > 0):
            index = self.lista_list_view[3].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[3][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data()
        self.callback()                 #fa riapparire la finestra precedente




