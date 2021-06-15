from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QPushButton, QSizePolicy, QHeaderView, \
    QGroupBox, QFormLayout, QMessageBox, QLineEdit

from Utilità.User_int_utility import User_int_utility
from functools import partial

from Vendita_Biglietti.Controller.ControlloreListaBiglietti import ControlloreListaBiglietti
from Vendita_Biglietti.Model.Biglietto import Biglietto
from Vendita_Biglietti.Views.VistaInserimentoDatiBiglietti import VistaInserimentoDatiBiglietti


class VistaMappaPosti(QWidget):
    def __init__(self, spettacolo, callback):
        super(VistaMappaPosti, self).__init__()

        self.controller = ControlloreListaBiglietti()

        self.callback = callback
        self.callback()

        self.spettacolo = spettacolo

        self.setWindowTitle("Prenotazione posti")
        self.setGeometry(0, 0, 1300, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        self.crea_mappa_posti()
        self.lista_posti_selezionati = []

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Bi"), 0, 0, 1, 2)
        ext_layout.addWidget(self.mappa_posti, 1, 0, 2, 1)
        ext_layout.addWidget(self.crea_box_posti_selezionati(), 1, 1)
        ext_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Avanti", self.conferma, QSizePolicy.Minimum,QSizePolicy.Minimum,"G"),
                             2, 1)
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
                button.clicked.connect(partial(self.seleziona_posto, i, j+1, conta_file))
                self.mappa_posti.setCellWidget(conta_file, j, button)
            conta_file += 1

        self.mappa_posti.setVerticalHeaderLabels(self.spettacolo.sala.file)

        h_header = self.mappa_posti.horizontalHeader()
        for i in range(self.spettacolo.sala.lunghezza_file):
            h_header.setSectionResizeMode(i, QHeaderView.Stretch)

        v_header = self.mappa_posti.verticalHeader()
        for i in range(len(self.spettacolo.sala.file)):
            v_header.setSectionResizeMode(i, QHeaderView.Stretch)


    # metodo che applica al push button del posto uno stile che varia a seconda
    # se un posto è standard o premium
    def applica_stile_posto(self, posto, button, selezionato=False):
        if not selezionato:
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
        else:
            button.setStyleSheet("QPushButton {"
                                   "border: 2px;"
                                   "background-color : #00C882;"
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
                                   "background-color : #009B65 ;"
                                   "}"
                                   )

    def crea_box_posti_selezionati(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        box.setTitle("Posti selezionati")
        self.box_layout = QFormLayout()
        box.setLayout(self.box_layout)
        self.box_layout.setContentsMargins(8, 40, 8, 8)

        return box

    def seleziona_posto(self, fila, posizione, numero_fila):
        posto_scelto = self.spettacolo.get_posto(fila, posizione)
        posto_selezionato_precedentemente = False

        for posto in self.lista_posti_selezionati:
            if posto["Posto"] == posto_scelto:
                self.lista_posti_selezionati.remove(posto)
                self.applica_stile_posto(self.spettacolo.get_posto(fila, posizione),
                                     self.mappa_posti.cellWidget(numero_fila, posizione - 1), False)
                posto_selezionato_precedentemente = True
                break

        if (not posto_selezionato_precedentemente) and len(self.lista_posti_selezionati) < 10:
            self.lista_posti_selezionati.append({"Posto": posto_scelto, "Cod_fisc": User_int_utility.crea_casella_testo("Codice fiscale",
                                                                                                                        QSizePolicy.Minimum)})
            self.applica_stile_posto(self.spettacolo.get_posto(fila, posizione),
                                     self.mappa_posti.cellWidget(numero_fila, posizione-1),
                                     True)
        elif len(self.lista_posti_selezionati) >= 10:
            QMessageBox.critical(self, 'Errore', "Si possono seleionare un massimo di 10 posti alla volta", QMessageBox.Ok, QMessageBox.Ok)

        self.update_ui()

    def update_ui(self):
        for i in reversed(range(self.box_layout.count())):
            self.box_layout.itemAt(i).widget().setParent(None)

        for posto in self.lista_posti_selezionati:
            posto_selezionato = posto["Posto"]
            if posto_selezionato.premium:
                poltrona = "Poltrona premium"
            else:
                poltrona = "Poltrona standard"
            self.box_layout.addRow(User_int_utility.crea_label(posto_selezionato.fila + "-" + str(posto_selezionato.posizione) + "  "  + poltrona),
                                   posto["Cod_fisc"])

    def conferma(self):
        for posto in self.lista_posti_selezionati:
            cliente = self.controller.get_cliente(posto["Cod_fisc"].text())

            if cliente is not None:
                self.controller.add_biglietto(Biglietto(
                    self.spettacolo.film.titolo,
                    self.spettacolo.data,
                    self.spettacolo.ora_inizio,
                    self.spettacolo.sala.nome,
                    posto["Posto"].fila,
                    posto["Posto"].posizione,
                    cliente))
            else:
                QMessageBox.critical(self, 'Errore', "Nessun cliente a sistema ha come codice fiscale " + posto["Cod_fisc"].text(),
                                     QMessageBox.Ok, QMessageBox.Ok)

        lista_biglietti = self.controller.get_lista_biglietti()
        if len(self.lista_posti_selezionati) == len(lista_biglietti):
            for biglietto in lista_biglietti:
                self.spettacolo.lista_presenze.append(biglietto.cliente)

            self.vista_inserimento_dati = VistaInserimentoDatiBiglietti()
            self.vista_inserimento_dati.show()
        #mostra nuova finestra

    def closeEvent(self, event):
        self.callback()                 #fa riapparire la finestra precedente