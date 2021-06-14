from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QCheckBox, QPushButton, QSizePolicy, QHeaderView, \
    QTableWidgetItem

from Vendita_Biglietti.Controller.ControlloreSpettacolo import ControlloreSpettacolo
from Utilità.User_int_utility import User_int_utility
from functools import partial

class VistaMappaPosti(QWidget):
    def __init__(self, spettacolo, callback):
        super(VistaMappaPosti, self).__init__()

        self.controller = ControlloreSpettacolo(spettacolo)

        self.callback = callback
        self.callback()

        self.spettacolo = spettacolo

        self.setWindowTitle("Prenotazione posti")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        self.crea_mappa_posti()
        self.lista_posti_selezionati = []

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Bi"), 0, 0, 1, 2)
        ext_layout.addWidget(self.mappa_posti, 1, 0)
        ext_layout.addWidget(User_int_utility.crea_label("Sebastiano Sebastianelli ............"), 1, 1)
        self.setLayout(ext_layout)

    def crea_mappa_posti(self):
        self.mappa_posti = QTableWidget(len(self.spettacolo.sala.file), self.spettacolo.sala.lunghezza_file)
        self.mappa_posti.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.mappa_posti.setStyleSheet("""
                                        QTableWidget {
                                        background-color: #222; 
                                        border-radius: 5px;
                                        }

                                        QTableWidget::item {                    
                                        background-color: #222;
                                        margin-top: 5px; 
                                        margin-left: 2px;
                                        margin-right: 2px;       
                                        border-radius: 6px;
                                        padding-left: 1px;
                                        }

                                        QTableWidget::item:selected {
                                        background-color: #222;
                                        }
                                        
                                        QHeaderView::section {
                                        Background-color: #222;
                                        color: #DDD;
                                        }
                                        """)


        conta_file = 0
        for i in (self.spettacolo.sala.file):
            for j in range(self.spettacolo.sala.lunghezza_file):
                button = QPushButton()
                button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
                self.applica_stile_posto(self.spettacolo.sala.posti[conta_file][j], button)
                button.clicked.connect(partial(self.seleziona_posto, i, j+1))
                self.mappa_posti.setCellWidget(conta_file, j, button)
            conta_file += 1

        self.mappa_posti.setHorizontalHeaderLabels(self.spettacolo.sala.file)

        h_header = self.mappa_posti.horizontalHeader()
        for i in range(self.spettacolo.sala.lunghezza_file):
            h_header.setSectionResizeMode(i, QHeaderView.Stretch)

        v_header = self.mappa_posti.verticalHeader()
        for i in range(len(self.spettacolo.sala.file)):
            v_header.setSectionResizeMode(i, QHeaderView.Stretch)


    # metodo che applica alla checkbox del posto uno stile che varia a seconda
    # se un posto è standard o premium
    def applica_stile_posto(self, posto, button):
        if posto.premium == True:
            button.setStyleSheet("QPushButton {"
                                   "border: 2px" + User_int_utility.tertiary_color + ";"
                                   "background-color : " + User_int_utility.tertiary_color + ";"
                                   "border-radius: 8px;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "border-width: 4px;"
                                   "border-style: flat;"
                                   "border-color: #222;"
                                   "}"
                                   "QPushButton::hover"
                                   "{"
                                   "background-color : #850000 ;"
                                   "}"
                                   )
        else:
            button.setStyleSheet("QPushButton {"
                                   "border: 2px" + User_int_utility.secondary_color + ";"
                                   "background-color : " + User_int_utility.secondary_color + ";"
                                   "border-radius: 8px;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "border-width: 4px;"
                                   "border-style: flat;"
                                   "border-color: #222;"
                                   "}"
                                   "QPushButton::hover"
                                   "{"
                                   "background-color : #979401 ;"
                                   "}"
                                   )


    def seleziona_posto(self, fila, posizione):
        posto_scelto = self.controller.get_posto(fila, posizione)
        if posto_scelto in self.lista_posti_selezionati:
            self.lista_posti_selezionati.remove(posto_scelto)
        else:
            self.lista_posti_selezionati.append(posto_scelto)
        self.update_ui()

    def update_ui(self):
        pass

    def closeEvent(self, event):
        self.callback()                 #fa riapparire la finestra precedente