from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QSizePolicy, QVBoxLayout, QTableWidget, QHeaderView, \
     QTableWidgetItem

from Utilità.User_int_utility import User_int_utility
from Vendita_Biglietti.Views.VistaRiepilogoBiglietti import VistaRiepilogoBiglietti


class VistaInserimentoDatiBiglietti(QWidget):
    def __init__(self, spettacolo, controller, callback, ritorna_home):
        super(VistaInserimentoDatiBiglietti, self).__init__()

        self.controller = controller

        # lista di funzioni che una volta giunti alla fine della vendita consentirà
        # di tornare alla home
        self.ritorna_home = ritorna_home
        self.ritorna_home.append(self.close)

        self.callback = callback
        self.callback()         #Fa scomparire la finestra precedente

        self.spettacolo = spettacolo

        # settaggio dei parametri generali della finestra
        self.setWindowTitle("Visualizzazione dati biglietti")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        # aggiunta dei widget al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Bi"), 0, 0)
        ext_layout.addWidget(self.crea_box(), 1, 0)

        self.setLayout(ext_layout)

    # Metodo che crea una QGroupBox contenente una tabella con i dati sui biglietti e
    # un pulsante per proseguire nella vendita dei biglietti
    def crea_box(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        box_layout = QVBoxLayout()
        box.setLayout(box_layout)
        box_layout.setContentsMargins(15, 20, 15, 15)

        box_layout.addWidget(self.crea_tabella())
        box_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Avanti", self.conferma, QSizePolicy.Expanding,
                                                                            QSizePolicy.Minimum, "G"))
        return box

    # metodo che crea la tabella con i dati di tessere e abbonamenti
    def crea_tabella(self):
        lista_biglietti = self.controller.get_lista_biglietti()
        self.lista_check_box = []

        tabella = QTableWidget(len(lista_biglietti), 4)

        # Modifica i colori della tabella e dei suoi item
        User_int_utility.applica_stile_tabella(tabella)

        #Settaggio dei titoli delle colonne
        tabella.setHorizontalHeaderLabels(["Cliente", "Posto", "Abbonamento", "Tessera"])

        #Ridimensionamento delle colonne
        h_header = tabella.horizontalHeader()
        for i in range(0, 4):
            h_header.setSectionResizeMode(i, QHeaderView.Stretch)

        # Ridimensionamento delle righe
        v_header = tabella.verticalHeader()
        for i in range(len(lista_biglietti)):
            v_header.setSectionResizeMode(i, QHeaderView.Stretch)
        v_header.hide()

        # Inserimento degli elementi all'interno della tabella
        i = 0
        for biglietto in lista_biglietti:
            label_tessera = User_int_utility.crea_label("")
            if biglietto.cliente.tessera is not None:
                if self.controller.controlla_disp_sconto_tessera(biglietto):
                    label_tessera.setText("Sconto disponibile")
                else:
                    label_tessera.setText("Punti ancora non sufficienti\nper ottenere lo sconto")
            else:
                label_tessera.setText("Non possiede la tessera")

            tabella.setCellWidget(i, 0, User_int_utility.crea_label(biglietto.cliente.nome + " " + biglietto.cliente.cognome))
            tabella.setCellWidget(i, 1, User_int_utility.crea_label(biglietto.fila_posto + "-" + str(biglietto.colonna_posto)))
            tabella.setCellWidget(i, 3, label_tessera)

            if biglietto.cliente.abbonamento is not None:
                check_box_abb = QTableWidgetItem("Utilizza abbonamento")
                check_box_abb.setCheckState(Qt.Unchecked)
                tabella.setItem(i, 2, check_box_abb)
                self.lista_check_box.append({"biglietto": biglietto, "box": check_box_abb})
            else:
                tabella.setCellWidget(i, 2, User_int_utility.crea_label("Non possiede l'abbonamento"))

            i += 1

        return tabella

    # metodo che aggiorna i parametri dei biglietti in base ai clienti
    # che hanno intenzione di utilizzare il loro abbonamento e crea la finestra di riepilogo
    def conferma(self):
        for elem in self.lista_check_box:
            if elem["box"].checkState() == Qt.Checked:
                elem["biglietto"].parametri["utilizza abb"] = True

        self.riepilogo = VistaRiepilogoBiglietti(self.controller, self.spettacolo, self.modifica_visibilita, self.ritorna_home)
        self.riepilogo.show()

    # metodo che modifica la visibiità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.callback()                 #fa riapparire la finestra precedente



