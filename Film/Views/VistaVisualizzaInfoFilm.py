from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGridLayout, QSizePolicy, QSpacerItem, QGroupBox, QHBoxLayout, QWidget

from Film.Controllers.ControlloreFilm import ControlloreFilm
from Utilità.User_int_utility import User_int_utility


class VistaVisualizzaInfoFilm(QWidget):
    def __init__(self, film, callback):
        super(VistaVisualizzaInfoFilm, self).__init__()

        self.controller = ControlloreFilm(film)

        self.callback = callback
        self.callback()                  #fa scomparire la finestra precedente

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione info film")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        #aggiunta dei vari elementi che compongono la UI al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Fi"), 0, 0, 1, 2)
        ext_layout.addWidget(self.crea_box_dati(), 1, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/film_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 1, 2, 1)
        ext_layout.addItem(QSpacerItem(10, 280, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0, 1, 2)

        self.setLayout(ext_layout)

    #metodo che ritorna il box dove vengono mostrate le informazioni sul film
    def crea_box_dati(self):
        box = QGroupBox()
        box.setTitle(self.controller.get_titolo())
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        box_layout = QHBoxLayout()
        box_layout.setContentsMargins(8, 30, 8, 15)

        box_layout.addWidget(User_int_utility.crea_label("Titolo: \nCasa di produzione: \nDurata: \nGenere: \nEtà minima: "))
        box_layout.addWidget(User_int_utility.crea_label(self.controller.get_titolo() + "\n"
                                                   + self.controller.get_casa_prod() + "\n"
                                                   + self.controller.get_durata() + " minuti\n"
                                                   + self.controller.get_genere() + "\n"
                                                   + self.controller.get_eta_minima()))

        box.setLayout(box_layout)
        return box

    def closeEvent(self, event):
        self.callback()             #fa riapparire la finestra precedente