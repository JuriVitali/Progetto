from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QSizePolicy, QVBoxLayout, QHeaderView, QTableWidget, \
    QMessageBox

from GestioneServizi.Model.ParametriServizi import ParametriServizi
from Utilità.User_int_utility import User_int_utility


class VistaRiepilogoBiglietti(QWidget):
    def __init__(self, controller, spettacolo, callback, ritorna_home):
        super(VistaRiepilogoBiglietti, self).__init__()

        self.controller = controller

        # lista di funzioni consente di tornare alla home
        self.ritorna_home = ritorna_home
        self.callback = callback
        self.callback()  # Fa scomparire la finestra precedente

        self.spettacolo = spettacolo

        # Diventa True solo quando la vendita è confermata
        self.finito = False

        self.lista_prezzi = self.controller.get_prezzi()
        self.lista_parametri_biglietti = self.controller.get_parametri_biglietti()

        # settaggio dei parametri generali della finestra
        self.setWindowTitle("Riepilogo biglietti e prezzi")
        self.setGeometry(0, 0, 1300, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        # aggiunta dei widget al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Bi"), 0, 0)
        ext_layout.addWidget(self.crea_box_esterno(), 1, 0)

        self.setLayout(ext_layout)

    # Metodo che crea e restituisce un box contente la tabella, il pulsante per la
    # conferma e un box interno con il prezzo totale dei biglietti
    def crea_box_esterno(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        box_layout = QGridLayout()
        box.setLayout(box_layout)
        box_layout.setContentsMargins(15, 20, 15, 15)

        box_layout.addWidget(self.crea_tabella(), 0, 0, 1, 2)
        box_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Conferma vendita", self.conferma, QSizePolicy.Expanding, QSizePolicy.Minimum, "G"),
                             1, 0)
        box_layout.addWidget(self.crea_box_totale(), 1, 1)
        return box

    # Metodo che restituisce un box contenente il prezzo totale dei biglietti
    def crea_box_totale(self):
        box = QGroupBox()
        User_int_utility.box_scuro(box)
        box.setTitle("Prezzo totale")
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box_layout = QVBoxLayout()
        box.setLayout(box_layout)
        box_layout.setContentsMargins(8, 30, 8, 8)

        totale = self.lista_prezzi["totale"]
        box_layout.addWidget(User_int_utility.crea_label("{:.2f}".format(totale) + " €", 19, "s"))

        return box

    # Metodo che resituisce una tabella con il riepilogo dei dati di ogni
    # biglietto
    def crea_tabella(self):
        lista_biglietti = self.controller.get_lista_biglietti()

        tabella = QTableWidget(len(lista_biglietti), 8)

        # Modifica i colori della tabella e dei suoi item
        User_int_utility.applica_stile_tabella(tabella)

        # Settaggio dei titoli delle colonne
        tabella.setHorizontalHeaderLabels(["Cliente", "Abbonamento", "Tariffa base", "Premium",
                                           "Weekend", "Sconto tessera", "Under 14", "Prezzo"])

        # Ridimensionamento delle colonne
        h_header = tabella.horizontalHeader()
        for i in range(0, 8):
            h_header.setSectionResizeMode(i, QHeaderView.Stretch)

        # Ridimensionamento delle righe
        v_header = tabella.verticalHeader()
        for i in range(len(lista_biglietti)):
            v_header.setSectionResizeMode(i, QHeaderView.Stretch)
        v_header.hide()

        # aggiunta dei widget alla tabella
        p = ParametriServizi()
        i = 0
        for biglietto in lista_biglietti:
            parametri_biglietto = self.lista_parametri_biglietti[i]
            tabella.setCellWidget(i, 0, User_int_utility.crea_label(biglietto.cliente.nome + "\n" + biglietto.cliente.cognome))

            if parametri_biglietto["utilizza abb"]:
                tabella.setCellWidget(i, 1, User_int_utility.crea_label("Utilizzato"))
                for j in range(2, 7):
                    tabella.setCellWidget(i, j, User_int_utility.crea_label("/"))
            else:
                tabella.setCellWidget(i, 1, User_int_utility.crea_label("Non utilizzato"))
                tabella.setCellWidget(i, 2, User_int_utility.crea_label("{:.2f}".format(p.tariffa_base_biglietto) + " €"))

                if parametri_biglietto["premium"]:
                    tabella.setCellWidget(i, 3, User_int_utility.crea_label("+ " + "{:.2f}".format(p.magg_premium_biglietto) + " €"))
                else:
                    tabella.setCellWidget(i, 3, User_int_utility.crea_label("No"))

                if parametri_biglietto["weekend"]:
                    tabella.setCellWidget(i, 4, User_int_utility.crea_label("+ " + "{:.2f}".format(p.magg_weekend_biglietto) + " €"))
                else:
                    tabella.setCellWidget(i, 4, User_int_utility.crea_label("No"))

                if parametri_biglietto["sconto tess"]:
                    tabella.setCellWidget(i, 5, User_int_utility.crea_label("- " + "{:.2f}".format(p.sconto_tessera) + " €"))
                else:
                    tabella.setCellWidget(i, 5, User_int_utility.crea_label("No"))

                if parametri_biglietto["under 14"]:
                    tabella.setCellWidget(i, 6, User_int_utility.crea_label("- " + "{:.2f}".format(p.sconto_under_14_biglietto) + " €"))
                else:
                    tabella.setCellWidget(i, 6, User_int_utility.crea_label("No"))

            tabella.setCellWidget(i, 7, User_int_utility.crea_label("{:.2f}".format(self.lista_prezzi["prezzi"][i]) + " €"))

            i += 1

        return tabella

    #Metodo che conferma la vendita dei biglietti
    def conferma(self):

        # Aggiorna la lista delle presenze
        lista_nuovi_spettatori = []
        for biglietto in self.controller.get_lista_biglietti():
            lista_nuovi_spettatori.append(biglietto.cliente)
        self.spettacolo.aggiorna_lista_presenze(lista_nuovi_spettatori)


        # Aggiorna i dati di tessere e abbonamenti, se sono stati utilizzati
        self.controller.aggiorna_servizi_utilizzati()

        # Report

        # prenota i posti per lo spettacolo
        self.controller.prenota_posti(self.spettacolo)

        self.controller.save_date()

        self.finito = True
        self.close()


    def closeEvent(self, event):
        if self.finito:
            for function in reversed(self.ritorna_home):          #ritorna alla home
                function()
        else:
            self.callback()                 #fa riapparire la finestra precedente
