from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QVBoxLayout, QSpacerItem
from PyQt5.QtGui import QPixmap, QIcon

from RilasciaAbbonamento.View.VistaRilasciaAbbonamento import VistaRilasciaAbbonamento
from RilasciaTessera.View.VistaRilasciaTessera import VistaRilasciaTessera
from Spettacoli.Views.VistaVisProgrammazioneSpettacoli import VistaVisProgrammazioneSpettacoli
from GestioneClienti.Views.VistaGestisciCliente import VistaGestisciCliente
from Utilità.User_int_utility import User_int_utility
from Vendita_Biglietti.Views.VistaSceltaSpettacolo import VistaSceltaSpettacolo


class VistaHomeBiglietteria(QWidget):

    def __init__(self, callback,parent=None):
        super(VistaHomeBiglietteria, self).__init__(parent)

        self.callback = callback
        self.callback()                 #fa scomparire la vista del login

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Home Biglietteria")                      #titolo
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")                 #colore dello sfondo
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)         #sposta la finestra al centro dello schermo
        ext_layout = QVBoxLayout()              #layout esterno

        orizzontal_layout = QHBoxLayout()             #layout che dovrà contenere il menù con i pulsanti e lo sfondo della schermata

        background_image = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Sfondi/bigliett_back.png'),QSizePolicy.Expanding, QSizePolicy.Expanding)

        # creazione del menù con pulsanti
        orizzontal_layout.addLayout(self.crea_menu_pulsanti())
        orizzontal_layout.addWidget(background_image)
        orizzontal_layout.setContentsMargins(0,0,0,0)

        # aggiunta dei layout interni a quello esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore())         #aggiunge il layout contenente il logo
        ext_layout.addLayout(orizzontal_layout)
        ext_layout.setContentsMargins(0,0,0,0)

        self.setLayout(ext_layout)

    #metodo che crea il menù contenente i pulsanti
    def crea_menu_pulsanti(self):
        menu_pulsanti = QVBoxLayout()  # creazione del layout verticale che conterrà i pulsanti
        menu_pulsanti.addItem(QSpacerItem(10, 7, QSizePolicy.Minimum, QSizePolicy.Minimum))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_vend_biglietti, QIcon('Immagini/Icone/servizi_icon.ico'),
                                                   'Vendita dei biglietti'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_ril_tessera, QIcon('Immagini/Icone/tessera_icon.png'),
                                                   'Rilascia una tessera'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_ril_abbonamento, QIcon('Immagini/Icone/abbonamento_icon.png'),
                                                                       'Rilascia un abbonamento'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_spettacoli, QIcon('Immagini/Icone/spettacoli_icon.jpg'),
                                                   'Visualizza gli spettacoli in programma'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_clienti, QIcon('Immagini/Icone/customer_icon.ico'),
                                                   'Gestione della registrazione dei clienti'))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.go_to_lista_presenze, QIcon('Immagini/Icone/lista_presenza_icon.png'),
                                                                       'Lista Presenze'))
        menu_pulsanti.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        menu_pulsanti.addWidget(User_int_utility.crea_home_push_button(self.logout, QIcon('Immagini/Icone/logout_icon.png'), 'Logout'))

        menu_pulsanti.setContentsMargins(4, 0, 4, 0)
        return menu_pulsanti

    # metodo che fa apparire la finestra per il rilascio di un abbonamento
    def go_to_ril_abbonamento(self):
        self.rilascia_abbonamento = VistaRilasciaAbbonamento(self.modifica_visibilita)
        self.rilascia_abbonamento.show()

    # metodo che fa apparire la finestra per il rilascio di una tessera
    def go_to_ril_tessera(self):
        self.rilascia_tessera = VistaRilasciaTessera(self.modifica_visibilita)
        self.rilascia_tessera.show()

    # metodo che fa apparire la finestra per la gestione dei clienti
    def go_to_clienti(self):
        self.vista_clienti = VistaGestisciCliente(self.modifica_visibilita)
        self.vista_clienti.show()

    # metodo che fa apparire la finestra per la visualizzazione degli spettacoli in programma
    def go_to_spettacoli(self):
        self.vista_spettacoli = VistaVisProgrammazioneSpettacoli(False, self.modifica_visibilita)
        self.vista_spettacoli.show()

    # metodo che fa apparire la finestra per la vendita dei biglietti
    def go_to_vend_biglietti(self):
        self.vista_vend_biglietti = VistaSceltaSpettacolo(self.modifica_visibilita)
        self.vista_vend_biglietti.show()

    # metodo che fa apparire la finestra per la consultazione del manuale
    def go_to_lista_presenze(self):
        pass

    # metodo che fa tornare alla schermata di login
    def logout(self):
        self.callback()
        self.close()

    # metodo che modifica la visibilità della schermata
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

