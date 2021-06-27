from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox

from GestioneClienti.Controller.ControlloreListaClienti import ControlloreListaClienti

from GestioneClienti.Views.VistaRegistraCliente import VistaRegistraCliente
from GestioneClienti.Views.VistaVisualizzaClienti import VistaVisualizzaClienti
from Lista_presenze.View.VistaVisualizzaPresenzeFilm import VistaVisualizzaPresenzeFilm
from Spettacoli.Controllers.ControlloreListaSpettacoli import ControlloreListaSpettacoli
from Utilità.User_int_utility import User_int_utility

class VistaVisualizzaPresenze(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaVisualizzaPresenze, self).__init__()

        self.controller = ControlloreListaSpettacoli()

        self.callback = callback
        self.callback()

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Lista Presenze")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)           #sposta la finestra al centro dello schermo

        # Creazione di un layout a griglia interno contenente i vari widget e l'immagine
        grid_layout = QGridLayout()
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza Presenze", self.show_lista_clienti_completa,
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

        oggi = QDate.currentDate()

        self.titolo_ricerca = User_int_utility.crea_casella_testo("Inserire il film")
        self.data_ricerca = User_int_utility.crea_date_edit(oggi.addDays(-14), oggi)
        self.list_view = User_int_utility.crea_list_view()

        layout.addWidget(User_int_utility.crea_label("Titolo film"), 0, 0)
        layout.addWidget(User_int_utility.crea_label("Data"), 1, 0)
        layout.addWidget(self.titolo_ricerca, 0, 1)
        layout.addWidget(self.data_ricerca, 1, 1)
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2, 2, 1)
        layout.addWidget(User_int_utility.crea_push_button("Cerca spettacolo", self.update_listview,
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

    # Metodo che, dopo aver verificato i campi inseriti, apre la vista per la visualizzazione dei clienti se essi sono corretti,
    # altrimenti genera un avviso
    def show_lista_clienti_filtrata(self):
            #avviso = self.controller.controlla_campi_ricerca(self.titolo_ricerca.text())
            if avviso == None:
                self.vista_lista_clienti = VistaVisualizzaPresenzeFilm(self.controller, self.modifica_visibilita,)
                self.vista_lista_clienti.show()
            else:
                QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)

    # metodo che fa apparire una finestra in cui vengono visualizzati tutti i clienti presenti a sistema
    def show_lista_clienti_completa(self):
            self.vista_lista_clienti = VistaVisualizzaPresenzeFilm(self.controller, self.modifica_visibilita, None, None)
            self.vista_lista_clienti.show()

   # metodo che aggiorna gli elementi nella listview
    def update_listview(self):
        self.lista_film_filtrata_titolo = self.controller.ricerca_film(self.titolo_ricerca.text())
        #self.lista_film_filtrata_data = self.lista_film_filt(self.lista_film_filtrata)
        self.listview_model = QStandardItemModel(self.list_view)
        #for data in self.lista_film_filtrata_titolo:
        for film in self.lista_film_filtrata_titolo:
                item = QStandardItem()
                item.setText(film.titolo + "")
                item.setEditable(False)
                self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
            User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
            #self.controller.save_data()              #salvataggio dei dati
            self.callback()                          #fa riapparire la finestra precedente
