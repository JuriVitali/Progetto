from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QListView, QHBoxLayout

from Utilità.User_int_utility import User_int_utility


class VistaVisualizzaDipendenti(QWidget):
    def __init__(self, nome, cognome, callback, parent=None):
        super(VistaVisualizzaDipendenti, self).__init__()
        self.setWindowTitle("Visualizzazione dipendenti")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        self.callback = callback
        self.callback()

        self.nome = nome
        self.cognome = cognome

        self.list_view = User_int_utility.crea_list_view()
        #self.lista_filtrata = self.get_dipendente_by_nome()
        #self.update_ui()

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
        pass

    def get_dipendente_by_index(self):
        pass

    def show_info_dipendente(self):
        pass

    def elimina_dipendente_by_index(self):
        pass

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.lista_filtrata:
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.callback()