from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QMessageBox, \
    QHBoxLayout

from GestioneClienti.Controller.ControlloreListaClienti import ControlloreListaClienti
from GestioneServizi.Model.ParametriServizi import ParametriServizi
from Utilità.User_int_utility import User_int_utility

class VistaRilasciaTessera(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaRilasciaTessera, self).__init__()

        self.controller = ControlloreListaClienti()

        self.callback = callback
        self.callback()

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Rilascio Tessera")
        User_int_utility.set_window_style(self)
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)           #sposta la finestra al centro dello schermo

        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Te"), 0, 0, 1, 2)
        ext_layout.addWidget(self.crea_box_ricerca_cliente(), 1, 0, 2, 1)
        ext_layout.addWidget(self.crea_box_codice(), 3, 0)
        ext_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Conferma", self.rilascia_tessera,
                                                                            QSizePolicy.Minimum, QSizePolicy.Expanding, "G"), 2, 1, 2, 1)
        ext_layout.addWidget(self.crea_box_descrizione(), 1, 1)
        self.setLayout(ext_layout)

    # metodo che crea il box contenente i widget per la ricerca di un cliente in base al nome e al cognome
    def crea_box_ricerca_cliente(self):
        box = QGroupBox()
        box.setTitle("Selezione cliente")
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        box_layout = QGridLayout()
        box_layout.setContentsMargins(8, 35, 8, 8)

        self.nome_ricerca = User_int_utility.crea_casella_testo("Inserire il nome del cliente")
        self.cognome_ricerca = User_int_utility.crea_casella_testo("Inserire il cognome del cliente")
        self.list_view = User_int_utility.crea_list_view()

        box_layout.addWidget(User_int_utility.crea_label("Nome: "), 0, 0)
        box_layout.addWidget(User_int_utility.crea_label("Cognome: "), 1, 0)
        box_layout.addWidget(self.nome_ricerca, 0, 1)
        box_layout.addWidget(self.cognome_ricerca, 1, 1)
        box_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum), 0, 2, 2, 1)
        box_layout.addWidget(User_int_utility.crea_push_button("Cerca cliente", self.update_listview, "", QSizePolicy.Expanding, QSizePolicy.Minimum),
                             0, 3, 2, 1)
        box_layout.addItem(QSpacerItem(15, 10, QSizePolicy.Minimum, QSizePolicy.Minimum), 2, 0, 1, 4)
        box_layout.addWidget(User_int_utility.crea_label("  Nome e cognome" + "{0:>60}".format("Codice fiscale")), 3, 0, 1, 4)
        box_layout.addWidget(self.list_view, 4, 0, 1, 4)

        box.setLayout(box_layout)
        return box

    def crea_box_codice(self):
        box = QGroupBox()
        box.setTitle("Codice Tessera")
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        box_layout = QHBoxLayout()
        box_layout.setContentsMargins(8, 35, 8, 8)

        self.codice_tess = User_int_utility.crea_casella_testo("Inserire il codice della tessera")

        box_layout.addWidget(User_int_utility.crea_label("Codice tessera: "))
        box_layout.addWidget(self.codice_tess)

        box.setLayout(box_layout)
        return box

    def crea_box_descrizione(self):
        box = QGroupBox()
        box.setTitle("Descrizione funzionamento del servizio ")
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(10, 45, 10, 150)

        p = ParametriServizi()
        descrizione = "La tessera ha un prezzo di " + "{:.2f}".format(p.prezzo_tessera) + " euro e\n" \
                      "consente di accumulare " + str(p.punti_per_euro) + " punti per \n"\
                      "ogni euro speso per l'acqusto di biglietti.\n" \
                      "Al raggiungimento di " + str(p.soglia_punti_sconto_tessera) + " punti si\n" \
                      "ottiene uno sconto di " + "{:.2f}".format(p.soglia_punti_sconto_tessera) + " sul\n" \
                      "successivo biglietto acquistato."

        box_layout.addWidget(User_int_utility.crea_label(descrizione))
        box.setLayout(box_layout)
        return box

    def update_listview(self):
        self.lista_clienti_filtrata = self.controller.get_cliente_by_nome(self.nome_ricerca.text(), self.cognome_ricerca.text())
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.lista_clienti_filtrata:
            item = QStandardItem()
            item.setText(str(cliente.nome + " " + cliente.cognome).ljust(60) + cliente.cod_fisc)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def rilascia_tessera(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            index = self.list_view.selectedIndexes()[0].row()
            cliente_selezionato = self.lista_clienti_filtrata[index]

            avviso = self.controller.controlla_tessera(self.codice_tess.text(), cliente_selezionato)
            if avviso is None:
                self.controller.rilascia_tessera(self.codice_tess.text(), cliente_selezionato)
                self.close()
            else:
                QMessageBox.critical(self, 'Errore', avviso, QMessageBox.Ok, QMessageBox.Ok)


    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data()              #salvataggio dei dati
        self.callback()                          #fa riapparire la finestra precedente
