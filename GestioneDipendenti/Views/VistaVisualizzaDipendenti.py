from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QListView, QHBoxLayout

from GestioneDipendenti.Views.VistaVisualizzaInfoDipendente import VistaVisualizzaInfoDipendente
from Utilità.User_int_utility import User_int_utility


class VistaVisualizzaDipendenti(QWidget):
    def __init__(self, controller, callback, nome=None, cognome=None, parent=None):
        super(VistaVisualizzaDipendenti, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()

        self.nome_cercato = nome
        self.cognome_cercato = cognome

        if self.nome_cercato != None and self.cognome_cercato!= None:
            self.lista_filtrata = self.get_dipendente_by_nome()
        else:
            self.lista_filtrata = self.controller.get_lista_completa()

        self.setWindowTitle("Visualizzazione dipendenti")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        self.list_view = User_int_utility.crea_list_view()
        self.update_ui()

        butt_layout = QHBoxLayout()
        butt_layout.addWidget(User_int_utility.crea_push_button("Visualizza info", self.show_info_dipendente,
                                                                "Visualizza le informazioni del dipendente selezionato",
                                                                QSizePolicy.Expanding, QSizePolicy.Minimum))
        butt_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Elimina", self.elimina_dipendente_by_index,
                                                                             QSizePolicy.Expanding, QSizePolicy.Minimum, "R"))

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Di"), 0, 0, 1, 2)
        ext_layout.addWidget(self.list_view, 1, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/dipendenti_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 1, 2, 1)
        ext_layout.addLayout(butt_layout, 2, 0)
        self.setLayout(ext_layout)


    def get_dipendente_by_nome(self):
        return self.controller.get_dipendente_by_nome(self.nome_cercato, self.cognome_cercato)

    def show_info_dipendente(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.vista_visualizza_info = VistaVisualizzaInfoDipendente(self.lista_filtrata[index], self.modifica_visibilita)
            self.vista_visualizza_info.show()

    def elimina_dipendente_by_index(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.controller.elimina_dipendente_by_index(index, self.lista_filtrata)
            self.update_ui()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.lista_filtrata:
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.callback()