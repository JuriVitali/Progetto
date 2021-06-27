
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QSizePolicy, QFormLayout

from GestioneServizi.Model.ParametriServizi import ParametriServizi
from Spettacoli.Controllers.ControlloreListaSpettacoli import ControlloreListaSpettacoli
from Utilità.Parametri import Parametri
from Utilità.User_int_utility import User_int_utility
from Vendita_Biglietti.Views.VistaMappaPosti import VistaMappaPosti

# Vista che permette la selezione dello spettacolo per il quale si vogliono
# vendere i biglietti
class VistaSceltaSpettacolo(QWidget):
    def __init__(self, callback):
        super(VistaSceltaSpettacolo, self).__init__()

        self.controller = ControlloreListaSpettacoli()

        # lista di funzioni che una volta giunti alla fine della vendita consentirà
        # di tornare alla home
        self.ritorna_home = [self.close]

        self.callback = callback
        self.callback()             # funzione che nasconde la finestra precedente

        #settaggio dei parametri generali della finestra
        self.setWindowTitle("Scelta spettacolo")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        # aggiunta dei widget al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Bi"), 0, 0)
        ext_layout.addWidget(self.crea_box_tariffe_biglietti(), 1, 0)
        ext_layout.addLayout(self.crea_group_boxes(), 2, 0)

        self.setLayout(ext_layout)

    # Metodo che crea un box in cui vengono riepilogate le tariffe dei biglietti
    def crea_box_tariffe_biglietti(self):
        box = QGroupBox()
        box.setTitle("Tariffe biglietti")
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box_layout = QGridLayout()
        box.setLayout(box_layout)
        box_layout.setContentsMargins(8, 30, 8, 8)

        p = ParametriServizi()

        box_layout.addWidget(User_int_utility.crea_label("Tariffa base:\t\t " + "{:.2f}".format(p.tariffa_base_biglietto) + " €"), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Maggiorazione poltrona premium:  " + "{:.2f}".format(p.magg_premium_biglietto) + " €"), 0, 1)
        box_layout.addWidget(User_int_utility.crea_label("Maggiorazione weekend:\t " + "{:.2f}".format(p.magg_weekend_biglietto) + " €"), 1, 0)
        box_layout.addWidget(User_int_utility.crea_label("Sconto under 14: \t\t " + "{:.2f}".format(p.sconto_under_14_biglietto) + " €"), 1, 1)

        return box

    # Metodo che crea, popola con gli spettacoli e restituisce una group box per ogni sala
    # all'interno di un layout a griglia
    def crea_group_boxes(self):
        griglia_boxes = QGridLayout()

        self.lista_list_view = []
        self.listviews_models = []

        #lista degli spettacoli in programma oggi
        self.lista_spettacoli_oggi = self.controller.get_spettacoli_by_day_divisi(QDate.currentDate())

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

    # metodo che popola la list view associata ad una sala con i corrispondenti
    # spettacoli in programma
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

    # funzione che permette la selezione di uno spettacolo in sala 1
    # e crea la finestra con la corrispondente mappa dei posti
    def seleziona_spettacolo_sala_1(self):
        if (len(self.lista_list_view[0].selectedIndexes()) > 0):
            index = self.lista_list_view[0].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[0][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    # funzione che permette la selezione di uno spettacolo in sala 2
    # e crea la finestra con la corrispondente mappa dei posti
    def seleziona_spettacolo_sala_2(self):
        if (len(self.lista_list_view[1].selectedIndexes()) > 0):
            index = self.lista_list_view[1].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[1][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    # funzione che permette la selezione di uno spettacolo in sala 3
    # e crea la finestra con la corrispondente mappa dei posti
    def seleziona_spettacolo_sala_3(self):
        if (len(self.lista_list_view[2].selectedIndexes()) > 0):
            index = self.lista_list_view[2].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[2][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    # funzione che permette la selezione di uno spettacolo in sala 4
    # e crea la finestra con la corrispondente mappa dei posti
    def seleziona_spettacolo_sala_4(self):
        if (len(self.lista_list_view[3].selectedIndexes()) > 0):
            index = self.lista_list_view[3].selectedIndexes()[0].row()
            self.vista_mappa_posti = VistaMappaPosti(self.lista_spettacoli_oggi[3][index], self.modifica_visibilita, self.ritorna_home)
            self.vista_mappa_posti.show()

    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data()     # salvataggio degli spettacoli
        self.callback()                 #fa riapparire la finestra precedente




