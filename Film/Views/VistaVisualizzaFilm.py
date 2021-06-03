from PyQt5.QtGui import QStandardItem, QStandardItemModel, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QSizePolicy

from Film.Views.VistaVisualizzaInfoFilm import VistaVisualizzaInfoFilm
from Utilità.User_int_utility import User_int_utility


class VistaVisualizzaFilm(QWidget):
    def __init__(self, controller, callback, titolo=None, parent=None):
        super(VistaVisualizzaFilm, self).__init__()

        self.controller = controller

        self.callback = callback
        self.callback()                                 #fa scomparire la finestra precedente

        self.titolo_cercato = titolo

        if self.titolo_cercato != None :                             #se il titolo non è None filtra in base ad esso
            self.lista_filtrata = self.get_film_by_titolo()          # la lista dei film presenti a sistema
        else:
            self.lista_filtrata = self.controller.get_lista_completa()

        #settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione film")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)                     #sposta al centro la finestra
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        self.list_view = User_int_utility.crea_list_view()
        self.update_ui()                                            #popola la listview con i film corrispondenti agli
                                                                    #eventuali parametri di ricerca

        #creazione di un layout orizzontale per i pushbutton
        butt_layout = QHBoxLayout()
        butt_layout.addWidget(User_int_utility.crea_push_button("Visualizza info", self.show_info_film,
                                                                "Visualizza le informazioni del film selezionato",
                                                                QSizePolicy.Expanding, QSizePolicy.Minimum))
        butt_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Elimina", self.elimina_film_by_index,
                                                           QSizePolicy.Expanding, QSizePolicy.Minimum, "R"))

        #aggiunta di tutti i widget e i layout al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Fi"), 0, 0, 1, 2)
        ext_layout.addWidget(self.list_view, 1, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/film_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 1, 2, 1)
        ext_layout.addLayout(butt_layout, 2, 0)

        self.setLayout(ext_layout)

    #metodo che ritorna la lista dei film presenti a sistema filtrata in base al titolo
    def get_film_by_titolo(self):
        return self.controller.get_film_by_titolo(self.titolo_cercato)

    #metodo che fa apparire una finestra con le informazioni del film selezionato
    def show_info_film(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.vista_visualizza_info = VistaVisualizzaInfoFilm(self.lista_filtrata[index], self.modifica_visibilita)
            self.vista_visualizza_info.show()

    #metodo che eliina il film selezionato
    def elimina_film_by_index(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            self.controller.elimina_film_by_index(index, self.lista_filtrata)
            self.update_ui()

    #metodo che aggiorna gli elementi nella listview
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for film in self.lista_filtrata:
            item = QStandardItem()
            item.setText(film.titolo)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    #metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.callback()         #fa riapparire la finestra precedente