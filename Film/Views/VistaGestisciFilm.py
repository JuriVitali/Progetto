from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QHBoxLayout

from Film.Controllers.ControlloreGestisciFilm import ControlloreGestisciFilm
from Utilità.User_int_utility import User_int_utility


class VistaGestisciFilm(QWidget):
    def __init__(self, parent=None):
        super(VistaGestisciFilm, self).__init__()
        #self.controller = ControlloreGestisciFilm()

        self.setWindowTitle("Gestione Film")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(User_int_utility.geometry[0], User_int_utility.geometry[1], 50, 50)

        grid_layout = QGridLayout()
        grid_layout.addWidget(User_int_utility.crea_push_button("Aggiungi film", self.show_new_film,
                                                                "Cliccare per aggiungere un film al sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza tutti i film", self.show_lista_film,
                                                                "Cliccare per visualizzare tutti i film inseriti nel sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        grid_layout.addItem(QSpacerItem(20, 95, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        grid_layout.addWidget(self.crea_box_ricerca(), 2, 0, 1, 2)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/film_back.png"), QSizePolicy.Minimum, QSizePolicy.Expanding),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20,28,0, 20)

        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Fi"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)


    def show_new_film(self):
        pass

    def show_lista_film(self, titolo=None):
        pass

    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Cerca un film")
        box.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
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

        self.titolo_ricerca = User_int_utility.crea_casella_testo()

        layout.addWidget(User_int_utility.crea_label("Titolo"))
        layout.addWidget(self.titolo_ricerca)
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(User_int_utility.crea_push_button("Cerca film", self.show_lista_film,
                                              "Cliccare per ricercare il film",
                                              QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.setContentsMargins(15,35,15,25)
        box.setLayout(layout)
        return box

    def closeEvent(self, event):
        pass
        #self.controller.save_data()