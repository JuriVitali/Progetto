from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QListView, QHBoxLayout

from GestioneClienti.Views.VistaVisualizzaInfoCliente import VistaVisualizzaInfoCliente
from Utilità.User_int_utility import User_int_utility


class VistaVisualizzaClienti(QWidget):
    def __init__(self, controller, callback, nome=None, cognome=None, parent=None):
        super(VistaVisualizzaClienti, self).__init__()
        print("0")

        self.controller = controller

        self.callback = callback
        self.callback()                                 #fa scomparire la finestra precedente

        self.nome_cercato = nome
        self.cognome_cercato = cognome


        #se almeno uno tra nome e cognome cercati non è None filtra la lista dei dipendenti presente a sistema
        #in base ad essi
        if self.nome_cercato != None or self.cognome_cercato!= None:
            self.lista_filtrata = self.get_cliente_by_nome()
        else:
            self.lista_filtrata = self.controller.get_lista_completa()


        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione clienti")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)                 #sposta al centro la finestra
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        self.list_view = User_int_utility.crea_list_view()
        self.update_ui()                                    #popola la listview con i film corrispondenti agli
                                                            #eventuali parametri di ricerca

        # creazione di un layout orizzontale per i pushbutton
        butt_layout = QHBoxLayout()
        butt_layout.addWidget(User_int_utility.crea_push_button("Visualizza dati tessera", self.show_info_cliente_tess,
                                                                "Visualizza le informazioni sulla tessera del cliente selezionato",
                                                                QSizePolicy.Expanding, QSizePolicy.Minimum))
        butt_layout.addWidget(User_int_utility.crea_push_button("Visualizza dati abbonamento", self.show_info_cliente_abb,
                                                                "Visualizza le informazioni sull'abboanmento del cliente selezionato",
                                                                QSizePolicy.Expanding, QSizePolicy.Minimum))
        butt_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Elimina", self.elimina_cliente_by_index,
                                                                             QSizePolicy.Expanding, QSizePolicy.Minimum, "R"))

        # aggiunta di tutti i widget e i layout al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Cl"), 0, 0, 1, 2)
        ext_layout.addWidget(self.list_view, 1, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 1, 2, 1)
        ext_layout.addLayout(butt_layout, 2, 0)
        self.setLayout(ext_layout)

    # metodo che ritorna la lista dei dipendenti presenti a sistema filtrata in base al nome e al cognome cercati
    def get_cliente_by_nome(self):
        return self.controller.get_cliente_by_nome(self.nome_cercato, self.cognome_cercato)

    # metodo che fa apparire una finestra con le informazioni dell'abbonamento del cliente selezionato
    def show_info_cliente_abb(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.vista_visualizza_info = VistaVisualizzaInfoCliente(self.lista_filtrata[index], self.modifica_visibilita)
            self.vista_visualizza_info.show()

    # metodo che fa apparire una finestra con le informazioni della tessera del cliente selezionato
    def show_info_cliente_tess(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.vista_visualizza_info = VistaVisualizzaInfoCliente(self.lista_filtrata[index], self.modifica_visibilita)
            self.vista_visualizza_info.show()

    # metodo che elimina il dipendente selezionato
    def elimina_cliente_by_index(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.controller.elimina_cliente_by_index(index, self.lista_filtrata)
            self.update_ui()



            # metodo che aggiorna gli elementi nella listview
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.lista_filtrata:
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome + "  " + cliente.cod_fisc)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.callback()         #fa riapparire la finestra precedente