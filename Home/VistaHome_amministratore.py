from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QSpacerItem
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QFont, QIcon

class VistaHome_amministratore(QWidget):

    def __init__(self, parent=None):
        super(VistaHome_amministratore, self).__init__(parent)
        self.setWindowTitle("Home Amministratore")                      #titolo
        self.setStyleSheet("background-color : #333;")                 #colore dello sfondo


        self.ext_layout = QVBoxLayout()

        striscia = QLabel('  Ciak e Azione')
        striscia.setFont(QFont('Segoe Script', 38))
        striscia.setStyleSheet("color:  #00BF7F;"
                               "background-color: #ddd;"
                                )
        striscia.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum)
        orizzontal_layout = QHBoxLayout()

        label = QLabel()                                                #label su cui deve essere caricata l'immagine

        pixmap = QPixmap('Home\\Sfondo_amm2.jpg')        #caricamento dell'immagine
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setContentsMargins(0,0,0,0)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        menu_pulsanti = QVBoxLayout()     #creazione del layout verticale che conterrà i pulsanti
        menu_pulsanti.addItem(QSpacerItem(10,18, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(self.get_push_button("Dipendenti", self.go_to_dipendenti, QIcon('Home\\dipendente_icon.png'), 'Gestione dei dipendenti'))
        menu_pulsanti.addWidget(self.get_push_button("Film", self.go_to_film, QIcon('Home\\film_icon.png'), 'Lista dei film'))
        menu_pulsanti.addWidget(self.get_push_button("Spettacoli", self.go_to_spettacoli, QIcon('Home\\spettacoli_icon.jpg'), 'Programmazione degli spettacoli'))
        menu_pulsanti.addWidget(self.get_push_button("Report", self.go_to_report, QIcon('Home\\report_icon.png'), 'Visualizzazione dei report'))
        menu_pulsanti.addWidget(self.get_push_button("Servizi", self.go_to_servizi, QIcon('Home\\servizi_icon.ico'), 'Gestione dei servizi'))
        menu_pulsanti.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(self.get_push_button("Manuale", self.go_to_manuale, QIcon('Home\\manual_icon.png'), 'Manuale'))
        menu_pulsanti.setContentsMargins(4,0,4,0)

        orizzontal_layout.addLayout(menu_pulsanti)
        orizzontal_layout.addWidget(label)
        orizzontal_layout.setContentsMargins(0,0,0,0)

        self.ext_layout.addWidget(striscia)
        self.ext_layout.addLayout(orizzontal_layout)
        self.ext_layout.setContentsMargins(0,0,0,0)

        self.setLayout(self.ext_layout)
        self.setGeometry(140, 80, 500, 500)


    #Restituisce un pulsante ed il suo collegamento
    def get_push_button(self, nome, on_click, icon, tooltip):
        button = QPushButton()
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        #button.setFont(QFont("Arial Black", 18))
        button.setStyleSheet("QPushButton"                   #stile del pulsante
                            "{"
                            "border-radius: 7px;"
                            "background-color : #333;"
                            "color: #eef;"
                            "}"
                             "QPushButton::pressed"
                             "{"
                             "color: #111;"
                             "border-width: 3px;"
                             "border-style: flat;"
                             "border-color: #333;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #00BF7F ;"  
                             "}"
                            )
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(70,50))
        button.setToolTip(tooltip)
        button.setToolTipDuration(2200)
        return button

    #Funzione che gestiranno i click dei pulsanti
    def go_to_report(self):
        self.ext_layout.removeWidget(label)
        self.ext_layout.addLayout(GestisciDipendente())


    def go_to_dipendenti(self):
        pass

    def go_to_film(self):
        pass

    def go_to_spettacoli(self):
        pass

    def go_to_servizi(self):
        pass

    def go_to_manuale(self):
        pass