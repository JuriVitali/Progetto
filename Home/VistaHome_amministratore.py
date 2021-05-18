from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QSpacerItem
from PyQt5.QtGui import QPixmap, QFont, QIcon


class VistaHome_amministratore(QWidget):

    def __init__(self, parent=None):
        super(VistaHome_amministratore, self).__init__(parent)
        self.setWindowTitle("Home Amministratore")                      #titolo
        self.setStyleSheet("background-color : #333;")                 #colore dello sfondo
        self.setGeometry(140, 80, 1000, 600)

        ext_layout = QVBoxLayout()

        striscia = QLabel('  Ciak e Azione')
        striscia.setFont(QFont('Segoe Script', 38))
        striscia.setStyleSheet("color:  #00BF7F;"
                               "background-color: #111;"
                               "radius: 10px;"
                               "offset: -3,-3"
                                )
        striscia.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum)
        orizzontal_layout = QHBoxLayout()

        label = QLabel()                                                #label su cui deve essere caricata l'immagine

        pixmap = QPixmap('Imm1.png')
        label.setPixmap(pixmap)                                          #caricamento dell'immagine (che non funziona)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        menu_pulsanti = QVBoxLayout()     #creazione del layout verticale che conterrà i pulsanti
        menu_pulsanti.addItem(QSpacerItem(10,18, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(self.get_push_button("Dipendenti", self.go_to_dipendenti(), QIcon('icona_dipendenti.png'), 'Gestione dei dipendenti'))
        menu_pulsanti.addWidget(self.get_push_button("Film", self.go_to_film(), QIcon('icona_film.jpg'), 'Lista dei film'))
        menu_pulsanti.addWidget(self.get_push_button("Spettacoli", self.go_to_spettacoli(), QIcon('icona_spettacolo.png'), 'Programmazione degli spettacoli'))
        menu_pulsanti.addWidget(self.get_push_button("Report", self.go_to_report(), QIcon('icona_report.png'), 'Visualizzazione dei report'))
        menu_pulsanti.addWidget(self.get_push_button("Servizi", self.go_to_servizi(), QIcon('icona_biglietto.jpg'), 'Gestione dei servizi'))
        menu_pulsanti.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(self.get_push_button("Manuale", self.go_to_manuale(), QIcon('icona_manuale.png'), 'Manuale'))
        menu_pulsanti.setContentsMargins(5,0,5,0)

        orizzontal_layout.addLayout(menu_pulsanti)
        orizzontal_layout.addWidget(label)

        ext_layout.addWidget(striscia)
        ext_layout.addLayout(orizzontal_layout)
        ext_layout.setContentsMargins(0,0,0,5)

        self.setLayout(ext_layout)


    #Restituisce un pulsante ed il suo collegamento
    def get_push_button(self, nome, on_click, icon, tooltip):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        #button.clicked.connect(on_click)
        button.setFont(QFont("Arial Black", 18))
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
        button.setToolTip(tooltip)
        button.setToolTipDuration(2200)
        return button

    #Funzione che gestiranno i click dei pulsanti
    def go_to_report(self):
        pass

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