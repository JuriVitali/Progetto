from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QIcon

class VistaHome_amministratore(QWidget):

    def __init__(self, parent=None):
        super(VistaHome_amministratore, self).__init__(parent)
        self.setWindowTitle("Home Amministratore")                      #titolo
        self.setStyleSheet("background-color : #333;")                 #colore dello sfondo
        self.setGeometry(200, 100, 800, 500)

        orizzontal_layout = QHBoxLayout()                               #layout esterno

        label = QLabel()                                                #label su cui deve essere caricata l'immagine

        pixmap = QPixmap('Imm1.png')
        label.setPixmap(pixmap)                                          #caricamento dell'immagine (che non funziona)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        menu_pulsanti = QVBoxLayout()                                    #creazione del layout verticale che conterrà i pulsanti
        menu_pulsanti.addWidget(self.get_push_button("Dipendenti", self.go_to_dipendenti(), QIcon('icona_dipendenti.png'), 'Gestione dei dipendenti'))
        menu_pulsanti.addWidget(self.get_push_button("Film", self.go_to_film(), QIcon('icona_film.jpg'), 'Lista dei film'))
        menu_pulsanti.addWidget(self.get_push_button("Spettacoli", self.go_to_spettacoli(), QIcon('icona_spettacolo.png'), 'Programmazione degli spettacoli'))
        menu_pulsanti.addWidget(self.get_push_button("Report", self.go_to_report(), QIcon('icona_report.png'), 'Visualizzazione dei report'))
        menu_pulsanti.addWidget(self.get_push_button("Servizi", self.go_to_servizi(), QIcon('icona_biglietto.jpg'), 'Gestione dei servizi'))
        menu_pulsanti.addWidget(self.get_push_button("Manuale", self.go_to_manuale(), QIcon('icona_manuale.png'), 'Manuale'))

        orizzontal_layout.addLayout(menu_pulsanti)
        orizzontal_layout.addWidget(label)

        self.setLayout(orizzontal_layout)


    #Restituisce un pulsante ed il suo collegamento
    def get_push_button(self, nome, on_click, icon, tooltip):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        #button.clicked.connect(on_click)
        button.setFont(QFont("Arial Black", 14))
        button.setStyleSheet("QPushButton"                   #stile del pulsante
                            "{"
                            "border-radius: 10px;"
                            "background-color : #333;"
                            "color: white;"
                            "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : blue;"
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