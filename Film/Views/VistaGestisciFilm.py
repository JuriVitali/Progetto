from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QHBoxLayout, \
    QMessageBox

from Film.Controllers.ControlloreListaFilm import ControlloreListaFilm
from Utilità.User_int_utility import User_int_utility
from Film.Views.VistaAggiungiFilm import VistaAggiungiFilm
from Film.Views.VistaVisualizzaFilm import VistaVisualizzaFilm


class VistaGestisciFilm(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaGestisciFilm, self).__init__()

        self.controller = ControlloreListaFilm()

        self.callback = callback
        self.callback()                                     #fa scomparire la finestra precedente

        self.setWindowTitle("Gestione Film")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)                #sposta la finestra al centro dello schermo

        #Creazione di un layout a griglia interno contenente i vari widget e l'immagine
        grid_layout = QGridLayout()
        grid_layout.addWidget(User_int_utility.crea_push_button("Aggiungi film", self.show_new_film,
                                                                "Cliccare per aggiungere un film al sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza tutti i film", self.show_lista_film_completa,
                                                                "Cliccare per visualizzare tutti i film inseriti nel sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        grid_layout.addItem(QSpacerItem(20, 95, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        grid_layout.addWidget(self.crea_box_ricerca(), 2, 0, 1, 2)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/film_back.png"), QSizePolicy.Minimum, QSizePolicy.Expanding),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20,0,0, 0)

        #aggiunta dei due layout al layout esterno
        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Fi"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)

    # metodo che crea il box contenente i widget per la ricerca di un film in base al titolo
    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Cerca un film")
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
        layout = QHBoxLayout()

        self.titolo_ricerca = User_int_utility.crea_casella_testo("Inserire il titolo")

        layout.addWidget(User_int_utility.crea_label("Titolo"))
        layout.addWidget(self.titolo_ricerca)
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(User_int_utility.crea_push_button("Cerca film", self.show_lista_film_filtrata, "Cliccare per ricercare il film",
                                                           QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.setContentsMargins(15, 35, 15, 25)
        box.setLayout(layout)
        return box

    #metodo che fa apparire la finestra per l'inserimento dei dati di un nuovo film
    def show_new_film(self):
        self.vista_aggiungi_film = VistaAggiungiFilm(self.controller, self.modifica_visibilita)
        self.vista_aggiungi_film.show()

    #metodo che fa apparire una finestra in cui vengono visualizzati tutti i film presenti a sistema
    def show_lista_film_completa(self):
        self.vista_lista_film = VistaVisualizzaFilm(self.controller, self.modifica_visibilita)
        self.vista_lista_film.show()

    #metodo che fa apparire una finestra in cui vengono visualizzati i film con il titolo inserito.
    #Se il titolo inserito non è corretto, visualizza un messaggio di errore
    def show_lista_film_filtrata(self):
        avviso = self.controller.controlla_campi_ricerca(self.titolo_ricerca.text())
        if avviso == None:
            self.vista_lista_dipendenti = VistaVisualizzaFilm(self.controller, self.modifica_visibilita,
                                                                    self.titolo_ricerca.text())
            self.vista_lista_dipendenti.show()
        else:
            QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)

    #metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data()     #salvataggio dei dati
        self.callback()                 #fa riapparire la finestra precedente