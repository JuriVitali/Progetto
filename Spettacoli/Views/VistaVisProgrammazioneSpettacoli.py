from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QSizePolicy, QCalendarWidget

from Spettacoli.Controllers.ControlloreListaSpettacoli import ControlloreListaSpettacoli
from Utilità.User_int_utility import User_int_utility
from Spettacoli.Views.VistaAggiungiSpettacolo import VistaAggiungiSpettacoli

#Vista che permette la visualizzazione degli spettacoli in programma.
#se modificabile è True allora sarà possibile modificare la programmazione degli spettacoli,
#altrimenti non sarà possibile.
class VistaVisProgrammazioneSpettacoli(QWidget):
    def __init__(self, modificabile, callback):
        super(VistaVisProgrammazioneSpettacoli, self).__init__()

        self.controller = ControlloreListaSpettacoli()

        self.modificabile = modificabile

        self.callback = callback
        self.callback()       #fa scomparire la finestra precedente

        # settaggio delle impostazioni generali della finestra
        self.setWindowTitle("Visualizzazione programmazione spettacoli")
        self.setGeometry(0, 0, 1250, 670)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QVBoxLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        self.data = QDate.currentDate()     #giorno per il quale si sta visualizzando la programmazione
        self.crea_calendario()

        self.label_giorno = User_int_utility.crea_label("")
        self.label_giorno.setStyleSheet("background-color: #222;"
                                        "color: #DDD;"
                                        "border-radius: 5px;")

        # Creazione di un layout interno che contiene tutti gli elementi della finestra ad eccezione della banda
        # superiore
        self.grid = QGridLayout()
        self.grid.setContentsMargins(10,10,10,10)
        self.crea_group_box()
        self.grid.addWidget(self.label_giorno, 0, 0, 1, 2)
        self.grid.addWidget(self.calendario, 2, 0, 2, 2)
        self.grid.addWidget(User_int_utility.crea_push_button("Cambia giorno", self.cambia_giorno, "Visualizza gli "
                            "spettacoli in programma per il giorno selezionato", QSizePolicy.Expanding, QSizePolicy.Expanding),
                            2, 2, 1, 2)

        if modificabile == True:
            self.grid.addWidget(User_int_utility.crea_green_or_red_push_button("Programma un nuovo spettacolo\nper questo giorno",
                                                                               self.show_aggiungi_spettacolo,
                                                                               QSizePolicy.Expanding, QSizePolicy.Expanding, "G"), 3, 2, 1, 2)

        # aggiunta dei vari elementi che compongono la UI al layout esterno
        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Sp"))
        ext_layout.addLayout(self.grid)

        self.update_ui()

        self.setLayout(ext_layout)

    # metodo che crea una groupbox per ogni sala con i relativi widget e le inserisce nel layout grid
    def crea_group_box(self):
        self.lista_list_view = []
        lista_collegamenti_eliminazione = [self.elimina_film_sala_1, self.elimina_film_sala_2,
                                           self.elimina_film_sala_3, self.elimina_film_sala_4]

        for i in [1, 2, 3, 4]:
            box = QGroupBox()
            box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            box.setTitle("Sala " + str(i))

            self.lista_list_view.append(User_int_utility.crea_list_view())

            v_layout = QVBoxLayout()
            v_layout.addWidget(self.lista_list_view[i-1])
            if self.modificabile == True:
                v_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Elimina spettacolo", lista_collegamenti_eliminazione[i-1],
                                                                              QSizePolicy.Minimum, QSizePolicy.Minimum, "R"))

            v_layout.setContentsMargins(10, 35, 10, 5)

            box.setLayout(v_layout)
            self.grid.addWidget(box, 1, i-1)

    # metodo che crea il calendario grazie alla classe QCalendarWidget e lo inserisce nel layout grid
    def crea_calendario(self):
        self.calendario = QCalendarWidget()
        self.calendario.setStyleSheet("QWidget {"
                                      "background-color:#222;"
                                      "color: #777;"
                                      "border-radius: 5px"
                                      "}"
                                      "QToolButton {"
                                      "background-color:#222;"
                                      "color: #DDD;"
                                      "icon-size: 25px;"
                                      "border-style: flat;"
                                      "}"
                                      "QMenu {"
                                      "background-color:#222;"
                                      "color: #DDD;"
                                      "}"
                                      )
        oggi = QDate.currentDate()
        self.calendario.setMinimumDate(oggi)
        self.calendario.setMaximumDate(oggi.addYears(1))
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

    # metodo che aggiorna l'interfaccia in base all'attributo self.data
    def update_ui(self):
        self.label_giorno.setText("Film in programma per il giorno " + str(self.data.day()) + "-" + str(self.data.month()) + ""
                                  "-" + str(self.data.year()))

        self.lista_spettacoli_giornaliera = self.controller.get_spettacoli_by_day(self.data)

        self.listviews_models = []
        for i in range(len(self.lista_list_view)):
            spettacoli_sala = self.lista_spettacoli_giornaliera[i]

            self.listviews_models.append(QStandardItemModel(self.lista_list_view[i]))
            if len(spettacoli_sala) > 0:
                for spettacolo in spettacoli_sala:
                    item = QStandardItem()
                    item.setText(spettacolo.ora_inizio.toString("HH:mm") + "-" + spettacolo.ora_fine.toString("HH:mm") + "    " + spettacolo.film.titolo)
                    item.setEditable(False)
                    self.listviews_models[i].appendRow(item)
            else:
                item = QStandardItem()
                item.setText("Nessuno spettacolo\nin programma")
                item.setEditable(False)
                self.listviews_models[i].appendRow(item)
            self.lista_list_view[i].setModel(self.listviews_models[i])

    # metodo che consente di cambiare il giorno per il quale si sta visualizzando la programmazione degli
    # spettacoli
    def cambia_giorno(self):
        self.data = self.calendario.selectedDate()
        self.update_ui()

    # metodo che consente l'eliminazione del film selezionato in programma nella sala 1
    def elimina_film_sala_1(self):
        if (len(self.lista_list_view[0].selectedIndexes()) > 0):
            index = self.lista_list_view[0].selectedIndexes()[0].row()
            self.controller.elimina_spettacolo_by_index(index, self.lista_spettacoli_giornaliera[0])
            self.update_ui()

    # metodo che consente l'eliminazione del film selezionato in programma nella sala 2
    def elimina_film_sala_2(self):
        if (len(self.lista_list_view[1].selectedIndexes()) > 0):
            index = self.lista_list_view[1].selectedIndexes()[0].row()
            self.controller.elimina_spettacolo_by_index(index, self.lista_spettacoli_giornaliera[1])
            self.update_ui()

    # metodo che consente l'eliminazione del film selezionato in programma nella sala 3
    def elimina_film_sala_3(self):
        if (len(self.lista_list_view[2].selectedIndexes()) > 0):
            index = self.lista_list_view[2].selectedIndexes()[0].row()
            self.controller.elimina_spettacolo_by_index(index, self.lista_spettacoli_giornaliera[2])
            self.update_ui()

    # metodo che consente l'eliminazione del film selezionato in programma nella sala 4
    def elimina_film_sala_4(self):
        if (len(self.lista_list_view[3].selectedIndexes()) > 0):
            index = self.lista_list_view[3].selectedIndexes()[0].row()
            self.controller.elimina_spettacolo_by_index(index, self.lista_spettacoli_giornaliera[3])
            self.update_ui()

    # metodo che crea una vista per l'aggiunta di un nuovo spettacolo
    def show_aggiungi_spettacolo(self):
        self.vista_aggiungi_spettacolo = VistaAggiungiSpettacoli(self.controller, self.modifica_visibilita, self.data, self.update_ui)

    # metodo che modifica la visibilità della finestra
    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        #self.controller.save_data()     #salvataggio dei dati
        self.callback()                 #fa riapparire la finestra precedente
