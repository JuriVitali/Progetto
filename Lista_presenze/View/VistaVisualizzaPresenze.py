from PyQt5.QtCore import QDate, QTime
from PyQt5.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox

from Lista_presenze.View.VistaVisualizzaPresenzeSpettacolo import VistaVisualizzaPresenzeSpettacolo
from Spettacoli.Controllers.ControlloreListaSpettacoli import ControlloreListaSpettacoli
from Utilità.User_int_utility import User_int_utility

class VistaVisualizzaPresenze(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaVisualizzaPresenze, self).__init__()

        self.controller = ControlloreListaSpettacoli()

        self.callback = callback
        self.callback()

        self.lista_spettacoli = self.controller.get_spettacoli_passati()

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Lista Presenze")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)           #sposta la finestra al centro dello schermo

        # Creazione di un layout a griglia interno contenente i vari widget e l'immagine
        grid_layout = QGridLayout()
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza Presenze", self.visualizza_presenze,
                                              "Cliccare per visualizzare le presenze per il film selezionato",
                                              QSizePolicy.Minimum, QSizePolicy.Expanding), 2, 0)
        grid_layout.addItem(QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Minimum), 1, 0)
        grid_layout.addWidget(self.crea_box_ricerca(), 0, 0)
        grid_layout.addWidget(self.crea_box_lista_spettacoli(), 0, 1, 3, 1)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/cliente_back.png"),
                                                                  QSizePolicy.Minimum, QSizePolicy.Minimum), 0, 2, 3, 1)    #immagine
        grid_layout.setContentsMargins(20, 0, 0, 0)

        # aggiunta dei due layout al layout esterno
        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore(""))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)

    # metodo che crea il box contenente i widget per la ricerca di un cliente in base al nome e al cognome
    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Cerca uno spettacolo")
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
        layout.setContentsMargins(8, 40, 8, 8)

        ieri = QDate.currentDate().addDays(-1)

        self.titolo_ricerca = User_int_utility.crea_casella_testo("Inserire il film")
        self.data_ricerca = User_int_utility.crea_date_edit(ieri.addDays(-13), ieri)
        self.list_view = User_int_utility.crea_list_view()

        layout.addWidget(User_int_utility.crea_label("Titolo film"), 0, 0)
        layout.addWidget(User_int_utility.crea_label("Data"), 1, 0)
        layout.addWidget(self.titolo_ricerca, 0, 1)
        layout.addWidget(self.data_ricerca, 1, 1)
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2, 2, 1)
        layout.addWidget(User_int_utility.crea_push_button("Cerca spettacolo", self.show_lista_spettacoli_filtrata,
                                                           "Cliccare per ricercare il film",
                                                           QSizePolicy.Minimum, QSizePolicy.Minimum), 2, 0, 1, 2)
        box.setLayout(layout)
        return box

    # Metodo che crea e restituisce un box contenente una list_view, dove compare la
    # lista dei clienti che soddisfano i requisiti immessi nella ricerca, e due pulsanti
    def crea_box_lista_spettacoli(self):
        box = QGroupBox()
        box.setTitle("Lista degli spettacoli")
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(8, 40, 8, 8)

        self.list_view = User_int_utility.crea_list_view()
        box_layout.addWidget(self.list_view)
        self.update_listview()

        box.setLayout(box_layout)
        return box

    def show_lista_spettacoli_filtrata(self):
        self.lista_spettacoli = self.controller.get_spettacoli_titolo_data(self.titolo_ricerca.text(), self.data_ricerca.date())
        self.update_listview()

    # metodo che fa apparire una finestra in cui vengono visualizzati tutti i clienti presenti a sistema
    def visualizza_presenze(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.vista_lista_presenze = VistaVisualizzaPresenzeSpettacolo(self.controller, self.lista_spettacoli[index], self.modifica_visibilita)
            self.vista_lista_presenze.show()

   # metodo che aggiorna gli elementi nella listview
    def update_listview(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for spettacolo in self.lista_spettacoli:
                item = QStandardItem()
                item.setText(spettacolo.data.toString("yyyy.MM.dd") + " " + spettacolo.ora_inizio.toString("HH:mm") + " " +
                             str(spettacolo.sala.nome) + " " + str(spettacolo.film.titolo))
                item.setEditable(False)
                self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
            User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
            self.callback()                          #fa riapparire la finestra precedente
