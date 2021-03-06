from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem

from GestioneServizi.Controller.ControlloreParametriServizi import ControlloreParametriServizi
from Utilità.User_int_utility import User_int_utility


class VistaGestisciServizi(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaGestisciServizi, self).__init__()

        self.controller = ControlloreParametriServizi()

        self.callback = callback
        self.callback()

        # Settaggio impostazioni principali della finestra
        self.setWindowTitle("Gestione Servizi")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)

        #Creazione del layout della finestra
        self.ext_layout = QGridLayout()
        self.ext_layout.setContentsMargins(0, 0, 0, 0)

        #Aggiunta degli elementi al layout della finestra
        self.ext_layout.addLayout(User_int_utility.crea_banda_superiore("Se"), 0, 0, 1, 4)
        self.ext_layout.addWidget(User_int_utility.crea_push_button("Biglietto", self.show_biglietto,
                                                               "Cliccare per visualizzare le informazioni relative al biglietto",
                                                               QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0)
        self.ext_layout.addWidget(User_int_utility.crea_push_button("Abbonamento", self.show_abbonamento,
                                                                "Cliccare per visualizzare le informazioni relative al biglietto",
                                                                QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 1)
        self.ext_layout.addWidget(User_int_utility.crea_push_button("Tessera", self.show_tessera,
                                                                "Cliccare per visualizzare le informazioni relative al biglietto",
                                                                QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 2)
        self.ext_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding,QSizePolicy.Expanding), 2, 0, 1, 3)
        self.ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/services-back.png"), QSizePolicy.Minimum, QSizePolicy.Expanding), 1, 3, 2, 1)

        self.setLayout(self.ext_layout)

    # Metodo che crea e restituisce il QGroupBox contenente le tariffe dei biglietti
    def crea_box_biglietto(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        box.setTitle("Tariffe biglietti")

        # Creazione dei pulsanti di modifica e di conferma delle modifiche delle tariffe
        self.modifica_par_biglietto = User_int_utility.crea_push_button("Modifica", self.modifica_parametri_biglietto, "",
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.conferma_par_biglietto = User_int_utility.crea_green_or_red_push_button("Conferma modifiche", self.conferma_parametri_biglietto,
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum, "G")

        # creazione delle doublespinbox per la modifica delle tariffe
        new_tariffa_base = User_int_utility.crea_double_spin_box(0, 60, self.controller.get_tariffa_base_biglietto())
        new_magg_premium = User_int_utility.crea_double_spin_box(0, 60, self.controller.get_magg_premium_biglietto())
        new_magg_weekend = User_int_utility.crea_double_spin_box(0, 60, self.controller.get_magg_weekend_biglietto())
        new_sconto_under_14 = User_int_utility.crea_double_spin_box(0, 60, self.controller.get_sconto_under_14_biglietto())

        #Lista che contiene le doublespinbox
        self.lista_nuovi_par_biglietto = [ new_tariffa_base, new_magg_premium, new_magg_weekend, new_sconto_under_14]

        #Creazione del layout del box e aggiunta degli elementi ad esso
        self.layout_biglietto = QGridLayout()
        self.layout_biglietto.addWidget(User_int_utility.crea_label("Tariffa base\nMaggiorazione poltrone premium\n"
                                                                    "Maggiorazione weekend\nSconto under 14"), 0, 0)
        self.layout_biglietto.addWidget(User_int_utility.crea_label("{:.2f}".format(self.controller.get_tariffa_base_biglietto()) + " €\n" +
                                                                    "{:.2f}".format(self.controller.get_magg_premium_biglietto()) + " €\n" +
                                                                    "{:.2f}".format(self.controller.get_magg_weekend_biglietto()) + " €\n" +
                                                                    "{:.2f}".format(self.controller.get_sconto_under_14_biglietto()) + " €"), 0, 1)
        self.layout_biglietto.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding,QSizePolicy.Minimum), 1, 0, 1, 2)
        self.layout_biglietto.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding, QSizePolicy.Expanding), 3, 0, 1, 2)
        self.layout_biglietto.addWidget(self.modifica_par_biglietto, 4, 0, 1, 2)
        self.layout_biglietto.setContentsMargins(8, 50, 8, 8)

        box.setLayout(self.layout_biglietto)
        return box

    # Metodo collegato al pulsante di modifica delle tariffe dei biglietti. Tale metodo fa apparire
    # delle doublespinbox per la modifica delle tariffe e un pulsante di conferma delle modifiche.
    # In particolare viene creato un QGroupBox che viene poi aggiunto tra gli elementi del box creato
    # dal metodo crea_box_biglietto.
    def modifica_parametri_biglietto(self):
        box = QGroupBox()
        box.setTitle("Nuove tariffe dei biglietti")
        User_int_utility.box_scuro(box)
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 45, 8, 8)

        # Aggiunta delle label al box
        box_layout.addWidget(User_int_utility.crea_label("Nuova tariffa base", 15, "s"), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuova maggiorazione poltrone premium", 15, "s"), 1,0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo maggiorazione weekend", 15, "s"), 2, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo sconto under 14", 15, "s"), 3, 0)

        # Aggiunta delle double_spin_box al box
        i = 0
        for parametro in self.lista_nuovi_par_biglietto:
            box_layout.addWidget(parametro, i, 1)
            box_layout.addWidget(User_int_utility.crea_label("€", 15, "s"), i, 2)
            i = i + 1

        box_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 4, 4, 1)
        box.setLayout(box_layout)

        # Aggiunta del nuovo box al precedente e del tasto conferma modifiche
        self.layout_biglietto.addWidget(box, 2, 0, 1, 2)
        self.layout_biglietto.addWidget(self.conferma_par_biglietto, 4, 0, 1, 2)

    # Metodo collegato al pulsante di conferma delle modifiche delle tariffe dei biglietti
    # che sovrascrive le vecchie tariffe con le nuove
    def conferma_parametri_biglietto(self):
        new_tariffa_base = self.lista_nuovi_par_biglietto[0].value()
        new_magg_premium = self.lista_nuovi_par_biglietto[1].value()
        new_magg_weekend = self.lista_nuovi_par_biglietto[2].value()
        new_sconto_under_14 = self.lista_nuovi_par_biglietto[3].value()
        self.controller.set_parametri_biglietto([new_tariffa_base, new_magg_premium, new_magg_weekend, new_sconto_under_14])

        self.show_biglietto()   # Viene fattto ricomparire il box iniziale del biglietto con le informazioni aggiornate

    # Metodo che crea e restituisce il QGroupBox contenente il valore dei parametri della tessera
    def crea_box_tessera(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        box.setTitle("Parametri tessera")

        # Creazione dei pulsanti di modifica e di conferma delle modifiche dei parametri
        self.modifica_par_tessera = User_int_utility.crea_push_button("Modifica", self.modifica_parametri_tessera, "",
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.conferma_par_tessera = User_int_utility.crea_green_or_red_push_button("Conferma modifiche", self.conferma_parametri_tessera,
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum, "G")

        # creazione delle doublespinbox per la modifica dei parametri
        new_prezzo_tessera = User_int_utility.crea_double_spin_box(0, 60, self.controller.get_prezzo_tessera())
        new_soglia_punti = User_int_utility.crea_spin_box(10, 2000, int(self.controller.get_soglia_punti_sconto_tessera()), 10)
        new_sconto_tessera = User_int_utility.crea_double_spin_box(0, 60, self.controller.get_sconto_tessera())

        # Lista che contiene le doublespinbox
        self.lista_nuovi_par_tessera = [new_prezzo_tessera, new_soglia_punti, new_sconto_tessera]

        # Creazione del layout del box e aggiunta degli elementi ad esso
        self.layout_tessera = QGridLayout()
        self.layout_tessera.addWidget(User_int_utility.crea_label("Prezzo tessera   \nSoglia punti da raggiungere per lo sconto    \n"
                                                                    "Sconto ottenibile con la tessera   \nPunti accumulati ad ogni euro speso   "), 0, 0)
        self.layout_tessera.addWidget(User_int_utility.crea_label("{:.2f}".format(self.controller.get_prezzo_tessera()) + " €\n" +
                                                                  str(self.controller.get_soglia_punti_sconto_tessera()) + "\n" +
                                                                  "{:.2f}".format(self.controller.get_sconto_tessera()) + " €\n" +
                                                                  str(self.controller.get_punti_per_euro())), 0, 1)

        self.layout_tessera.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding,QSizePolicy.Minimum), 1, 0, 1, 2)
        self.layout_tessera.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding, QSizePolicy.Expanding), 3, 0, 1, 2)
        self.layout_tessera.addWidget(self.modifica_par_tessera, 4, 0, 1, 2)
        self.layout_tessera.setContentsMargins(8, 50, 8, 8)

        box.setLayout(self.layout_tessera)
        return box

    # Metodo collegato al pulsante di modifica dei parametri della tessera. Tale metodo fa apparire
    # delle doublespinbox per la modifica dei parametri della tessera e un pulsante di conferma delle modifiche.
    # In particolare viene creato un QGroupBox che viene poi aggiunto tra gli elementi del box creato
    # dal metodo crea_box_tessera.
    def modifica_parametri_tessera(self):
        box = QGroupBox()
        box.setTitle("Nuovi parametri della tessera")
        User_int_utility.box_scuro(box)
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 45, 8, 8)

        # Aggiunta delle label al box
        box_layout.addWidget(User_int_utility.crea_label("Nuovo prezzo tessera", 15, "s"), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuova soglia punti da raggiungere per lo sconto", 15, "s"), 1, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo sconto ottenibile con la tessera", 15, "s"), 2, 0)

        # Aggiunta delle double_spin_box al box
        box_layout.addWidget(self.lista_nuovi_par_tessera[0], 0, 1)
        box_layout.addWidget(User_int_utility.crea_label("€", 15, "s"), 0, 2)
        box_layout.addWidget(self.lista_nuovi_par_tessera[1], 1, 1)
        box_layout.addWidget(self.lista_nuovi_par_tessera[2], 2, 1)
        box_layout.addWidget(User_int_utility.crea_label("€", 15, "s"), 2, 2)

        box_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 4, 3, 1)
        box.setLayout(box_layout)

        # Aggiunta del nuovo box al precedente e del tasto conferma modifiche
        self.layout_tessera.addWidget(box, 2, 0, 1, 2)
        self.layout_tessera.addWidget(self.conferma_par_tessera, 4, 0, 1, 2)

    # Metodo collegato al pulsante di conferma delle modifiche dei parametri della tessera
    # che sovrascrive le vecchie tariffe con le nuove
    def conferma_parametri_tessera(self):
        new_prezzo_tessera = self.lista_nuovi_par_tessera[0].value()
        new_soglia_punti = self.lista_nuovi_par_tessera[1].value()
        new_sconto_tessera = self.lista_nuovi_par_tessera[2].value()
        self.controller.set_parametri_tessera([new_prezzo_tessera, new_soglia_punti, new_sconto_tessera])

        self.show_tessera()     # Viene fattto ricomparire il box iniziale della tessera con le informazioni aggiornate

    # Metodo che crea e restituisce il QGroupBox contenente il valore dei parametri dell'abbonamento
    def crea_box_abbonamento(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        box.setTitle("Parametri abbonamento")

        # Creazione dei pulsanti di modifica e di conferma delle modifiche dei parametri
        self.modifica_par_abbonamento = User_int_utility.crea_push_button("Modifica", self.modifica_parametri_abbonamento, "",
                                                                      QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.conferma_par_abbonamento = User_int_utility.crea_green_or_red_push_button("Conferma modifiche",
                                                                                   self.conferma_parametri_abbonamento,
                                                                                   QSizePolicy.Expanding,
                                                                                   QSizePolicy.Minimum, "G")

        # creazione delle doublespinbox per la modifica dei parametri
        new_prezzo_abbonamento = User_int_utility.crea_double_spin_box(0, 150, self.controller.get_prezzo_abbonamento())
        new_ingressi_consentiti = User_int_utility.crea_spin_box(1, 100, self.controller.get_ingressi_consentiti_abb())
        new_durata_abbonamento = User_int_utility.crea_spin_box(1, 800, self.controller.get_durata_abb())

        # Lista che contiene le doublespinbox
        self.lista_nuovi_par_abbonamento = [new_prezzo_abbonamento, new_ingressi_consentiti, new_durata_abbonamento]

        self.layout_abbonamento = QGridLayout()
        self.layout_abbonamento.addWidget(User_int_utility.crea_label("Prezzo abbonamento\nIngressi consentiti con l'abbonamento\n"
                                                                  "Durata (in giorni) dell'abbonamento"), 0, 0)
        self.layout_abbonamento.addWidget(User_int_utility.crea_label("{:.2f}".format(self.controller.get_prezzo_abbonamento()) + " €\n" +
                                                                    str(self.controller.get_ingressi_consentiti_abb()) + "\n" +
                                                                    str(self.controller.get_durata_abb())), 0, 1)

        # Creazione del layout del box e aggiunta degli elementi ad esso
        self.layout_abbonamento.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        self.layout_abbonamento.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding, QSizePolicy.Expanding), 3, 0, 1, 2)
        self.layout_abbonamento.addWidget(self.modifica_par_abbonamento, 4, 0, 1, 2)
        self.layout_abbonamento.setContentsMargins(8, 50, 8, 8)

        box.setLayout(self.layout_abbonamento)
        return box

    # Metodo collegato al pulsante di modifica dei parametri dell'abbonamento. Tale metodo fa apparire
    # delle doublespinbox per la modifica dei parametri dell'abbonamento e un pulsante di conferma delle modifiche.
    # In particolare viene creato un QGroupBox che viene poi aggiunto tra gli elementi del box creato
    # dal metodo crea_box_abbonamento.
    def modifica_parametri_abbonamento(self):
        box = QGroupBox()
        box.setTitle("Nuovi parametri dell'abbonamento")
        User_int_utility.box_scuro(box)
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 45, 8, 8)

        # Aggiunta delle label al box
        box_layout.addWidget(User_int_utility.crea_label("Nuovo prezzo abbonamento", 15, "s"), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo numero di ingressi consentiti con l'abbonamento", 15, "s"), 1,0)
        box_layout.addWidget(User_int_utility.crea_label("Nuova durata (in giorni) dell'abbonamento", 15, "s"), 2, 0)

        # Aggiunta delle double_spin_box al box
        box_layout.addWidget(self.lista_nuovi_par_abbonamento[0], 0, 1)
        box_layout.addWidget(User_int_utility.crea_label("€", 15, "s"), 0, 2)
        box_layout.addWidget(self.lista_nuovi_par_abbonamento[1], 1, 1)
        box_layout.addWidget(self.lista_nuovi_par_abbonamento[2], 2, 1)

        box_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 4, 3, 1)
        box.setLayout(box_layout)

        # Aggiunta del nuovo box al precedente e del tasto conferma modifiche
        self.layout_abbonamento.addWidget(box, 2, 0, 1, 2)
        self.layout_abbonamento.addWidget(self.conferma_par_abbonamento, 4, 0, 1, 2)

    # Metodo collegato al pulsante di conferma delle modifiche dei parametri dell'abbonamento
    # che sovrascrive le vecchie tariffe con le nuove
    def conferma_parametri_abbonamento(self):
        new_prezzo_abbonamento = self.lista_nuovi_par_abbonamento[0].value()
        new_ingressi_consentiti = self.lista_nuovi_par_abbonamento[1].value()
        new_durata = self.lista_nuovi_par_abbonamento[2].value()
        self.controller.set_parametri_abbonamento([new_prezzo_abbonamento, new_ingressi_consentiti, new_durata])

        self.show_abbonamento() # Viene fattto ricomparire il box iniziale dell'abbonamento con le informazioni aggiornate

    # Metodo collegato al pulsante "Biglietto" che fa comparire il QGroupBox con le tariffe attuali
    # dei biglietti
    def show_biglietto(self):
        self.ext_layout.addWidget(self.crea_box_biglietto(), 2, 0, 1, 3)

    # Metodo collegato al pulsante "Tessera" che fa comparire il QGroupBox con i parametri attuali
    # relativi al funzionamento della tessera
    def show_tessera(self):
        self.ext_layout.addWidget(self.crea_box_tessera(), 2, 0, 1, 3)

    # Metodo collegato al pulsante "Abbonamento" che fa comparire il QGroupBox con i parametri attuali
    # relativi al funzionamento dell'abbonamento
    def show_abbonamento(self):
        self.ext_layout.addWidget(self.crea_box_abbonamento(), 2, 0, 1, 3)

    # Metodo che fa comparire la finestra se è nascosta, mentre la fa scomparire se è visibile
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data() #Salvataggio dei dati
        self.callback()     # Chiamata al metodo che fa ricomparire la finestra precedente