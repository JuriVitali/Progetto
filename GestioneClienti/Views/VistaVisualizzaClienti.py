from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QListView, QHBoxLayout, QSpacerItem, QGroupBox, \
    QVBoxLayout

from GestioneClienti.Views.VistaVisualizzaAbb import VistaVisualizzaAbb
from GestioneClienti.Views.VistaVisualizzaInfoCliente import VistaVisualizzaInfoCliente
from GestioneClienti.Views.VistaVisualizzaTessera import VistaVisualizzaTessera
from Utilità.User_int_utility import User_int_utility


class VistaVisualizzaClienti(QWidget):
    def __init__(self, controller, callback, nome=None, cognome=None, parent=None):
        super(VistaVisualizzaClienti, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()                                 #fa scomparire la finestra precedente

        self.nome_cercato = nome
        self.cognome_cercato = cognome

        #se almeno uno tra nome e cognome cercati non è None filtra la lista dei clienti presente a sistema
        #in base ad essi
        if self.nome_cercato != None or self.cognome_cercato!= None:
            self.lista_filtrata = self.get_cliente_by_nome()
        else:
            self.lista_filtrata = self.controller.get_lista_completa()

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione clienti")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)                 #sposta al centro la finestra
        self.ext_layout = QGridLayout()
        self.ext_layout.setContentsMargins(0, 0, 0, 0)

        # aggiunta di tutti i widget e i layout al layout esterno
        self.ext_layout.addLayout(User_int_utility.crea_banda_superiore("Cl"), 0, 0, 1, 3)
        self.ext_layout.addWidget(self.crea_box_lista_clienti(), 1, 0)
        self.ext_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding), 1, 1)
        self.ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/cliente_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 2)
        self.setLayout(self.ext_layout)

    def crea_box_lista_clienti(self):
        box = QGroupBox()
        box.setTitle("Lista dei clienti")
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)

        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(8, 40, 8, 8)

        self.list_view = User_int_utility.crea_list_view()
        box_layout.addWidget(self.list_view)
        self.update_listview()

        box_layout.addWidget(User_int_utility.crea_push_button("Visualizza info cliente", self.show_info_cliente,
                                                               "Visualizza le informazioni del cliente selezionato",
                                                               QSizePolicy.Minimum, QSizePolicy.Minimum))
        box_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Elimina cliente", self.elimina_cliente_by_index,
                                                               QSizePolicy.Minimum, QSizePolicy.Minimum, "R"))

        box.setLayout(box_layout)
        return box

    def crea_box_info_cliente(self, cliente_selezionato):
        ext_box = QGroupBox()
        ext_box.setTitle("Info di " + cliente_selezionato.nome + " " + cliente_selezionato.cognome)
        ext_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ext_box_layout = QVBoxLayout()
        ext_box_layout.setContentsMargins(8, 40, 8, 8)
        ext_box.setLayout(ext_box_layout)

        box_anagrafica = QGroupBox()
        box_anagrafica.setTitle("Anagrafica")
        User_int_utility.box_scuro(box_anagrafica)
        layout_anagrafica = QHBoxLayout()
        layout_anagrafica.setContentsMargins(8, 40, 8, 8)
        box_anagrafica.setLayout(layout_anagrafica)

        layout_anagrafica.addWidget(User_int_utility.crea_label("Nome: \nCognome: \nData di nascita: \nCodice fiscale: \nEmail: ",
                                    15, "s"))
        layout_anagrafica.addWidget(User_int_utility.crea_label(cliente_selezionato.nome + "\n"
                                                      + cliente_selezionato.cognome + "\n"
                                                      + cliente_selezionato.data_nascita.toString("yyyy.MM.dd") + "\n"
                                                      + cliente_selezionato.cod_fisc + "\n"
                                                      + cliente_selezionato.email, 15, "s"))
        ext_box_layout.addWidget(box_anagrafica)

        box_abbonamento = QGroupBox()
        box_abbonamento.setTitle("Informazioni abbonamento")
        User_int_utility.box_scuro(box_abbonamento)
        layout_abbonamento = QHBoxLayout()
        layout_abbonamento.setContentsMargins(8, 40, 8, 8)
        box_abbonamento.setLayout(layout_abbonamento)
        if cliente_selezionato.cod_abb is not None:
            layout_abbonamento.addWidget(User_int_utility.crea_label("Codice abbonamento: \nIngressi Disponibili: \nData di scadenza:",
                                            15, "s"))
            layout_abbonamento.addWidget(User_int_utility.crea_label("Codice abbonamento: \nIngressi Disponibili: \nData di scadenza:", 15, "s"))
        else:
            layout_abbonamento.addWidget(User_int_utility.crea_label(cliente_selezionato.nome + " " +cliente_selezionato.cognome +
                                                                     " non è in possesso di un abbonamento", 15, "s"))
        ext_box_layout.addWidget(box_abbonamento)

        box_tessera = QGroupBox()
        box_tessera.setTitle("Informazioni tessera")
        User_int_utility.box_scuro(box_tessera)
        layout_tessera = QHBoxLayout()
        layout_tessera.setContentsMargins(8, 40, 8, 8)
        box_tessera.setLayout(layout_tessera)
        if cliente_selezionato.cod_tess is not None:
            layout_tessera.addWidget(User_int_utility.crea_label("Codice tessera: \nPunti: ",15, "s"))
            layout_tessera.addWidget(User_int_utility.crea_label("Codice tessera: \nPunti: ",15, "s"))
        else:
            layout_tessera.addWidget(User_int_utility.crea_label(cliente_selezionato.nome + " " + cliente_selezionato.cognome +
                                            " non è in possesso di una tessera", 15, "s"))
        ext_box_layout.addWidget(box_tessera)

        ext_box_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding,QSizePolicy.Expanding))

        return ext_box

    # metodo che ritorna la lista dei clienti presenti a sistema filtrata in base al nome e al cognome cercati
    def get_cliente_by_nome(self):
        return self.controller.get_cliente_by_nome(self.nome_cercato, self.cognome_cercato)

    # metodo che fa apparire una groupbox con le informazioni del cliente selezionato
    def show_info_cliente(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.ext_layout.addWidget(self.crea_box_info_cliente(self.lista_filtrata[index]), 1, 1)

    # metodo che elimina il cliente selezionato
    def elimina_cliente_by_index(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.controller.elimina_cliente_by_index(index, self.lista_filtrata)
            self.update_listview()
            
            self.ext_layout.addWidget(User_int_utility.crea_label(""), 1, 1)

    # metodo che aggiorna gli elementi nella listview
    def update_listview(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.lista_filtrata:
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




