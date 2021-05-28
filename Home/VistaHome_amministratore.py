from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QSpacerItem
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QFont, QIcon
from Utilità.User_int_utility import User_int_utility
from GestioneDipendenti.Views.VistaGestisciDipendente import VistaGestisciDipendente
from Film.Views.VistaGestisciFilm import VistaGestisciFilm

class VistaHome_amministratore(QWidget):

    def __init__(self, parent=None):
        super(VistaHome_amministratore, self).__init__(parent)
        self.setWindowTitle("Home Amministratore")                      #titolo
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")                 #colore dello sfondo
        self.setGeometry(User_int_utility.geometry[0], User_int_utility.geometry[1], 600, 500)
        ext_layout = QVBoxLayout()              #layout esterno

        orizzontal_layout = QHBoxLayout()             #layout che dovrà contenere il menù con i pulsanti e lo sfondo della schermata

        background_image = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Sfondi/imm_back_amm.png'),QSizePolicy.Expanding, QSizePolicy.Expanding)

        menu_pulsanti = QVBoxLayout()     #creazione del layout verticale che conterrà i pulsanti
        menu_pulsanti.addItem(QSpacerItem(10,18, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(self.get_push_button(self.go_to_dipendenti, QIcon('Immagini/Icone/dipendente_icon.png'), 'Gestione dei dipendenti'))
        menu_pulsanti.addWidget(self.get_push_button(self.go_to_film, QIcon('Immagini/Icone/film_icon.png'), 'Lista dei film'))
        menu_pulsanti.addWidget(self.get_push_button(self.go_to_spettacoli, QIcon('Immagini/Icone/spettacoli_icon.jpg'), 'Programmazione degli spettacoli'))
        menu_pulsanti.addWidget(self.get_push_button(self.go_to_report, QIcon('Immagini/Icone/report_icon.png'), 'Visualizzazione dei report'))
        menu_pulsanti.addWidget(self.get_push_button(self.go_to_servizi, QIcon('Immagini/Icone/servizi_icon.ico'), 'Gestione dei servizi'))
        menu_pulsanti.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(self.get_push_button(self.go_to_manuale, QIcon('Immagini/Icone/manual_icon.png'), 'Manuale'))
        menu_pulsanti.setContentsMargins(4,0,4,0)

        orizzontal_layout.addLayout(menu_pulsanti)
        orizzontal_layout.addWidget(background_image)
        orizzontal_layout.setContentsMargins(0,0,0,0)

        ext_layout.addLayout(User_int_utility.crea_banda_superiore())         #aggiunge il layout contenente il logo
        ext_layout.addLayout(orizzontal_layout)
        ext_layout.setContentsMargins(0,0,0,0)

        self.setLayout(ext_layout)


    #Funzione che riceve funzione da collegare al pulsante, icona del pulsante e tooltip e
    #restituisce un pulsante collegato alla funzione passata
    def get_push_button(self, on_click, icon, tooltip):
        button = QPushButton()
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        button.setStyleSheet("QPushButton"                   #stile del pulsante
                            "{"
                            "border-radius: 7px;"
                            "background-color : " + User_int_utility.primary_color + ";"
                            "}"
                             "QPushButton::pressed"
                             "{"
                             "border-width: 3px;"
                             "border-style: flat;"
                             "border-color: " + User_int_utility.primary_color + ";"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : " + User_int_utility.secondary_color + " ;"  
                             "}"
                            )
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(80,60))
        button.setToolTip(tooltip)
        button.setToolTipDuration(2200)
        return button

    #Funzione che gestiranno i click dei pulsanti
    def go_to_report(self):
        pass

    def go_to_dipendenti(self):
        self.vista_gestione_dipendenti = VistaGestisciDipendente()
        self.vista_gestione_dipendenti.show()
        pass

    def go_to_film(self):
        self.vista_gestione_film = VistaGestisciFilm()
        self.vista_gestione_film.show()
        pass

    def go_to_spettacoli(self):
        pass

    def go_to_servizi(self):
        pass

    def go_to_manuale(self):
        pass