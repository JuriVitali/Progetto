from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QHBoxLayout, QSpacerItem, QGroupBox, \
    QVBoxLayout

from Utilità.User_int_utility import User_int_utility

class VistaVisualizzaPresenzeSpettacolo(QWidget):
    def __init__(self, controller, spettacolo, callback, parent=None):
        super(VistaVisualizzaPresenzeSpettacolo, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()       #fa scomparire la finestra precedente

        self.spettacolo = spettacolo

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione presenze dello spettacolo")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)                 #sposta al centro la finestra
        self.ext_layout = QGridLayout()
        self.ext_layout.setContentsMargins(0, 0, 0, 0)

        # aggiunta di tutti i widget e i layout al layout esterno
        self.ext_layout.addLayout(User_int_utility.crea_banda_superiore(""), 0, 0, 1, 3)
        self.ext_layout.addWidget(self.crea_box_presenze(), 1, 0)
        self.ext_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding), 1, 1)
        self.ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/cliente_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 2)
        self.setLayout(self.ext_layout)

    # Metodo che crea e restituisce un box contenente una list_view, dove compare la
    # lista dei clienti che soddisfano i requisiti immessi nella ricerca, e due pulsanti
    def crea_box_presenze(self):
        box = QGroupBox()
        box.setTitle("Lista delle presenze")
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(8, 40, 8, 8)

        self.list_view = User_int_utility.crea_list_view()
        box_layout.addWidget(self.list_view)
        self.update_listview()
        box_layout.addWidget(User_int_utility.crea_push_button("Visualizza info", self.show_info_cliente,
                                                               "Visualizza le informazioni della persona selezionata",
                                                               QSizePolicy.Minimum, QSizePolicy.Minimum))

        box.setLayout(box_layout)
        return box

    # Metodo che crea e restituisce un box contenente i dati del cliente e, se li possiede,
    # i dati della tessera e dell'abbonamento
    def crea_box_info_cliente(self, cliente_selezionato):
        ext_box = QGroupBox()                       # Il box conterrà a sua volta tre box interni
        ext_box.setTitle("Info di " + cliente_selezionato.nome + " " + cliente_selezionato.cognome)
        ext_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ext_box_layout = QVBoxLayout()
        ext_box_layout.setContentsMargins(8, 40, 8, 8)
        ext_box.setLayout(ext_box_layout)

        # creazione del primo box con le info del cliente
        box_anagrafica = QGroupBox()
        User_int_utility.box_scuro(box_anagrafica)
        layout_anagrafica = QHBoxLayout()
        layout_anagrafica.setContentsMargins(8, 15, 8, 15)
        box_anagrafica.setLayout(layout_anagrafica)

        layout_anagrafica.addWidget(User_int_utility.crea_label("Nome: \nCognome: \nData di nascita: \nCodice fiscale: \nTelefono: \nEmail: ",
                                    15, "s"))
        layout_anagrafica.addWidget(User_int_utility.crea_label(cliente_selezionato.nome + "\n"
                                                      + cliente_selezionato.cognome + "\n"
                                                      + QDate(cliente_selezionato.data_nascita).toString("yyyy.MM.dd") + "\n"
                                                      + cliente_selezionato.cod_fisc + "\n"
                                                      + cliente_selezionato.telefono + "\n"
                                                      + cliente_selezionato.email, 15, "s"))

        ext_box_layout.addWidget(box_anagrafica)
        ext_box_layout.addItem(QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Minimum))

        return ext_box

    # metodo che fa apparire una groupbox con le informazioni del cliente selezionato
    def show_info_cliente(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.cliente_selezionato = self.spettacolo.lista_presenze[index]
            self.ext_layout.addWidget(self.crea_box_info_cliente(self.cliente_selezionato), 1, 1)


    # metodo che aggiorna gli elementi nella listview
    def update_listview(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.spettacolo.lista_presenze:
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.callback()         #fa riapparire la finestra precedente




