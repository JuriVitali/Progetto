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

        self.setWindowTitle("Gestione Servizi")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        self.ext_layout = QGridLayout()
        self.ext_layout.setContentsMargins(0, 0, 0, 0)

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

    def crea_box_biglietto(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        box.setTitle("Tariffe biglietti")

        self.modifica_par_biglietto = User_int_utility.crea_push_button("Modifica", self.modifica_parametri_biglietto, "",
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.conferma_par_biglietto = User_int_utility.crea_green_or_red_push_button("Conferma modifiche", self.conferma_parametri_biglietto,
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum, "G")

        new_tariffa_base = {'euro': User_int_utility.crea_spin_box(0, 60, User_int_utility.get_euro(self.controller.get_tariffa_base_biglietto())),
                                 'centesimi': User_int_utility.crea_spin_box(0, 99, User_int_utility.get_centesimi(self.controller.get_tariffa_base_biglietto()), 10)}
        new_magg_weekend = {'euro': User_int_utility.crea_spin_box(0, 60, User_int_utility.get_euro(self.controller.get_magg_weekend_biglietto())),
                                 'centesimi': User_int_utility.crea_spin_box(0, 99, User_int_utility.get_centesimi(self.controller.get_magg_weekend_biglietto()), 10)}
        new_magg_premium = {'euro': User_int_utility.crea_spin_box(0, 60, User_int_utility.get_euro(self.controller.get_magg_premium_biglietto())),
                                 'centesimi': User_int_utility.crea_spin_box(0, 99, User_int_utility.get_centesimi(self.controller.get_magg_premium_biglietto()), 10)}
        new_sconto_under_14 = {'euro': User_int_utility.crea_spin_box(0, 60, User_int_utility.get_euro(self.controller.get_sconto_under_14_biglietto())),
                                 'centesimi': User_int_utility.crea_spin_box(0, 99, User_int_utility.get_centesimi(self.controller.get_sconto_under_14_biglietto()), 10)}
        self.lista_nuovi_par_biglietto = [ new_tariffa_base, new_magg_premium, new_magg_weekend, new_sconto_under_14]

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

    def modifica_parametri_biglietto(self):
        box = QGroupBox()
        box.setTitle("Nuove tariffe dei biglietti")
        box.setStyleSheet("QGroupBox"
                          "{"
                          "background-color: #111;"
                          "border-radius: 8px"
                          "}"
                          "QGroupBox::title"
                          "{"
                          "background-color: " + User_int_utility.tertiary_color + ";"
                          "border-radius: 4px"
                          "}"
                          )
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 45, 8, 8)

        box_layout.addWidget(User_int_utility.crea_label("Nuova tariffa base", 15, "s"), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuova maggiorazione poltrone premium", 15, "s"), 1,0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo maggiorazione weekend", 15, "s"), 2, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo sconto under 14", 15, "s"), 3, 0)

        i = 0
        for parametro in self.lista_nuovi_par_biglietto:
            box_layout.addWidget(parametro['euro'], i, 1)
            box_layout.addWidget(parametro['centesimi'], i, 2)
            box_layout.addWidget(User_int_utility.crea_label("€", 15, "s"), i, 3)
            i = i + 1

        box_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 4, 4, 1)
        box.setLayout(box_layout)

        self.layout_biglietto.addWidget(box, 2, 0, 1, 2)
        self.layout_biglietto.addWidget(self.conferma_par_biglietto, 4, 0, 1, 2)

    def conferma_parametri_biglietto(self):
        new_tariffa_base = self.lista_nuovi_par_biglietto[0]["euro"].value() + (self.lista_nuovi_par_biglietto[0]["centesimi"].value() / 100)
        new_magg_premium = self.lista_nuovi_par_biglietto[1]["euro"].value() + (self.lista_nuovi_par_biglietto[1]["centesimi"].value() / 100)
        new_magg_weekend = self.lista_nuovi_par_biglietto[2]["euro"].value() + (self.lista_nuovi_par_biglietto[2]["centesimi"].value() / 100)
        new_sconto_under_14 = self.lista_nuovi_par_biglietto[3]["euro"].value() + (self.lista_nuovi_par_biglietto[3]["centesimi"].value() / 100)
        self.controller.set_parametri_biglietto([new_tariffa_base, new_magg_premium, new_magg_weekend, new_sconto_under_14])

        self.show_biglietto()

    def crea_box_tessera(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        box.setTitle("Parametri tessera")

        self.modifica_par_tessera = User_int_utility.crea_push_button("Modifica", self.modifica_parametri_tessera, "",
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.conferma_par_tessera = User_int_utility.crea_green_or_red_push_button("Conferma modifiche", self.conferma_parametri_tessera,
                                                                        QSizePolicy.Expanding, QSizePolicy.Minimum, "G")

        new_prezzo_tessera = {'euro': User_int_utility.crea_spin_box(0, 60, User_int_utility.get_euro(self.controller.get_prezzo_tessera())),
                                 'centesimi': User_int_utility.crea_spin_box(0, 99, User_int_utility.get_centesimi(self.controller.get_prezzo_tessera()), 10)}
        new_soglia_punti = {'punti': User_int_utility.crea_spin_box(10, 2000, int(self.controller.get_soglia_punti_sconto_tessera()),10)}
        new_sconto_tessera = {'euro': User_int_utility.crea_spin_box(0, 60, User_int_utility.get_euro(self.controller.get_sconto_tessera())),
                                 'centesimi': User_int_utility.crea_spin_box(0, 99, User_int_utility.get_centesimi(self.controller.get_sconto_tessera()), 10)}
        self.lista_nuovi_par_tessera = [new_prezzo_tessera, new_soglia_punti, new_sconto_tessera]


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

    def modifica_parametri_tessera(self):
        box = QGroupBox()
        box.setTitle("Nuovi parametri della tessera")
        box.setStyleSheet("QGroupBox"
                             "{"
                             "background-color: #111;"  
                             "border-radius: 8px"
                             "}"
                             "QGroupBox::title"
                             "{"
                             "background-color: " + User_int_utility.tertiary_color + ";"
                             "border-radius: 4px"
                             "}"
                          )
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 45, 8, 8)

        box_layout.addWidget(User_int_utility.crea_label("Nuovo prezzo tessera", 15, "s"), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuova soglia punti da raggiungere per lo sconto", 15, "s"), 1, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo sconto ottenibile con la tessera", 15, "s"), 2, 0)

        i = 0
        for parametro in self.lista_nuovi_par_tessera:
            if i==1 :
                box_layout.addWidget(parametro['punti'], i, 1)
            else:
                box_layout.addWidget(parametro['euro'], i, 1)
                box_layout.addWidget(parametro['centesimi'], i, 2)
                box_layout.addWidget(User_int_utility.crea_label("€", 15, "s"), i, 3)
            i = i + 1

        box_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 4, 3, 1)
        box.setLayout(box_layout)

        self.layout_tessera.addWidget(box, 2, 0, 1, 2)
        self.layout_tessera.addWidget(self.conferma_par_tessera, 4, 0, 1, 2)

    def conferma_parametri_tessera(self):
        new_prezzo_tessera = self.lista_nuovi_par_tessera[0]["euro"].value() + (self.lista_nuovi_par_tessera[0]["centesimi"].value() / 100)
        new_soglia_punti = self.lista_nuovi_par_tessera[1]["punti"].value()
        new_sconto_tessera = self.lista_nuovi_par_tessera[2]["euro"].value() + (self.lista_nuovi_par_tessera[2]["centesimi"].value() / 100)
        self.controller.set_parametri_tessera([new_prezzo_tessera, new_soglia_punti, new_sconto_tessera])

        self.show_tessera()

    def crea_box_abbonamento(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        box.setTitle("Parametri abbonamento")

        self.modifica_par_abbonamento = User_int_utility.crea_push_button("Modifica", self.modifica_parametri_abbonamento, "",
                                                                      QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.conferma_par_abbonamento = User_int_utility.crea_green_or_red_push_button("Conferma modifiche",
                                                                                   self.conferma_parametri_abbonamento,
                                                                                   QSizePolicy.Expanding,
                                                                                   QSizePolicy.Minimum, "G")

        new_prezzo_abbonamento = {'euro': User_int_utility.crea_spin_box(0, 150, User_int_utility.get_euro(self.controller.get_prezzo_abbonamento())),
                                  'centesimi': User_int_utility.crea_spin_box(0, 99, User_int_utility.get_centesimi(self.controller.get_prezzo_abbonamento()), 10)}
        new_ingressi_consentiti = User_int_utility.crea_spin_box(1, 100, self.controller.get_ingressi_consentiti_abb())
        new_durata_abbonamento = User_int_utility.crea_spin_box(1, 800, User_int_utility.get_euro(self.controller.get_durata_abb()))
        self.lista_nuovi_par_abbonamento = [new_prezzo_abbonamento, new_ingressi_consentiti, new_durata_abbonamento]

        self.layout_abbonamento = QGridLayout()
        self.layout_abbonamento.addWidget(User_int_utility.crea_label("Prezzo abbonamento\nIngressi consentiti con l'abbonamento\n"
                                                                  "Durata (in giorni) dell'abbonamento"), 0, 0)
        self.layout_abbonamento.addWidget(User_int_utility.crea_label("{:.2f}".format(self.controller.get_prezzo_abbonamento()) + " €\n" +
                                                                    str(self.controller.get_ingressi_consentiti_abb()) + "\n" +
                                                                    str(self.controller.get_durata_abb())), 0, 1)

        self.layout_abbonamento.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        self.layout_abbonamento.addItem(QSpacerItem(10, 60, QSizePolicy.Expanding, QSizePolicy.Expanding), 3, 0, 1, 2)
        self.layout_abbonamento.addWidget(self.modifica_par_abbonamento, 4, 0, 1, 2)
        self.layout_abbonamento.setContentsMargins(8, 50, 8, 8)

        box.setLayout(self.layout_abbonamento)
        return box

    def modifica_parametri_abbonamento(self):
        box = QGroupBox()
        box.setTitle("Nuovi parametri dell'abbonamento")
        box.setStyleSheet("QGroupBox"
                          "{"
                          "background-color: #111;"
                          "border-radius: 8px"
                          "}"
                          "QGroupBox::title"
                          "{"
                          "background-color: " + User_int_utility.tertiary_color + ";"
                          "border-radius: 4px"
                          "}"
                          )
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 45, 8, 8)


        box_layout.addWidget(User_int_utility.crea_label("Nuovo prezzo abbonamento", 15, "s"), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Nuovo numero di ingressi consentiti con l'abbonamento", 15, "s"), 1,0)
        box_layout.addWidget(User_int_utility.crea_label("Nuova durata (in giorni) dell'abbonamento", 15, "s"), 2, 0)

        box_layout.addWidget(self.lista_nuovi_par_abbonamento[0]['euro'], 0, 1)
        box_layout.addWidget(self.lista_nuovi_par_abbonamento[0]['centesimi'], 0, 2)
        box_layout.addWidget(User_int_utility.crea_label("€", 15, "s"), 0, 3)
        box_layout.addWidget(self.lista_nuovi_par_abbonamento[1], 1, 1, 1, 2)
        box_layout.addWidget(self.lista_nuovi_par_abbonamento[2], 2, 1, 1, 2)

        box_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 4, 3, 1)
        box.setLayout(box_layout)

        self.layout_abbonamento.addWidget(box, 2, 0, 1, 2)
        self.layout_abbonamento.addWidget(self.conferma_par_abbonamento, 4, 0, 1, 2)

    def conferma_parametri_abbonamento(self):
        new_prezzo_abbonamento = self.lista_nuovi_par_abbonamento[0]["euro"].value() + (self.lista_nuovi_par_abbonamento[0]["centesimi"].value() / 100)
        new_ingressi_consentiti = self.lista_nuovi_par_abbonamento[1].value()
        new_durata = self.lista_nuovi_par_abbonamento[2].value()
        self.controller.set_parametri_abbonamento([new_prezzo_abbonamento, new_ingressi_consentiti, new_durata])

        self.show_abbonamento()

    def show_biglietto(self):
        self.ext_layout.addWidget(self.crea_box_biglietto(), 2, 0, 1, 3)

    def show_tessera(self):
        self.ext_layout.addWidget(self.crea_box_tessera(), 2, 0, 1, 3)

    def show_abbonamento(self):
        self.ext_layout.addWidget(self.crea_box_abbonamento(), 2, 0, 1, 3)

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data()
        self.callback()