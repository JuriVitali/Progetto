from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QSpacerItem
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QFont, QIcon
from Utilità.User_int_utility import User_int_utility

class VistaHomeBiglietteria(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeBiglietteria, self).__init__(parent)
        self.setWindowTitle("Home Biglietteria")                      #titolo
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")                 #colore dello sfondo
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)

        ext_layout = QVBoxLayout()              #layout esterno

        orizzontal_layout = QHBoxLayout()             #layout che dovrà contenere il menù con i pulsanti e lo sfondo della schermata

        background_image = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Sfondi/bigliett_back.png'),QSizePolicy.Expanding, QSizePolicy.Expanding)

        menu_pulsanti = QVBoxLayout()     #creazione del layout verticale che conterrà i pulsanti
        menu_pulsanti.addItem(QSpacerItem(10,18, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_vend_biglietti, QIcon('Immagini/Icone/servizi_icon.ico'), 'Vendita dei biglietti'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_ril_tessera, QIcon('Immagini/Icone/tessera_icon.png'), 'Rilascia una tessera'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_ril_abbonamento, QIcon('Immagini/Icone/abbonamento_icon.png'), 'Rilascia un abbonamento'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_spettacoli, QIcon('Immagini/Icone/spettacoli_icon.jpg'), 'Visualizza gli spettacoli in programma'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_clienti, QIcon('Immagini/Icone/customer_icon.ico'), 'Gestione della registrazione dei clienti'))
        menu_pulsanti.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_manuale, QIcon('Immagini/Icone/manual_icon.png'), 'Consulta manuale'))
        menu_pulsanti.setContentsMargins(4,0,4,0)

        orizzontal_layout.addLayout(menu_pulsanti)
        orizzontal_layout.addWidget(background_image)
        orizzontal_layout.setContentsMargins(0,0,0,0)

        ext_layout.addLayout(User_int_utility.crea_banda_superiore())         #aggiunge il layout contenente il logo
        ext_layout.addLayout(orizzontal_layout)
        ext_layout.setContentsMargins(0,0,0,0)

        self.setLayout(ext_layout)

    #Funzione che gestiranno i click dei pulsanti
    def go_to_ril_abbonamento(self):
        pass

    def go_to_ril_tessera(self):
        pass

    def go_to_clienti(self):
        pass

    def go_to_spettacoli(self):
        pass

    def go_to_vend_biglietti(self):
        pass

    def go_to_manuale(self):
        pass

