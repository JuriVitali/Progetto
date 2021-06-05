from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QSizePolicy, QCalendarWidget

from Spettacoli.Controllers.ControlloreListaSpettacoli import ControlloreListaSpettacoli
from Utilità.User_int_utility import User_int_utility
from Spettacoli.Views.VistaAggiungiSpettacolo import VistaAggiungiSpettacoli

#se modificabile è True allora sarà possibile modificare la programmazione degli spettacoli,
#altrimenti no
class VistaVisProgrammazioneSpettacoli(QWidget):
    def __init__(self, modificabile, callback):
        super(VistaVisProgrammazioneSpettacoli, self).__init__()

        self.controller = ControlloreListaSpettacoli()

        self.callback = callback
        self.callback()

        self.setWindowTitle("Visualizzazione programmazione spettacoli")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QVBoxLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        User_int_utility.set_window_style(self)

        self.data = QDate.currentDate()
        self.crea_calendario()
        self.label_giorno = User_int_utility.crea_label("")
        self.label_giorno.setStyleSheet("background-color: #222;"
                                        "color: #DDD;"
                                        "border-radius: 5px;")

        self.grid = QGridLayout()
        self.grid.setContentsMargins(10,20,10,10)
        self.crea_group_box()

        self.grid.addWidget(self.label_giorno, 0, 0, 1, 2)
        self.grid.addWidget(self.calendario, 2, 0, 2, 2)
        self.grid.addWidget(User_int_utility.crea_push_button("Cambia giorno", self.cambia_giorno, "Visualizza gli "
                            "spettacoli in programma per il giorno selezionato", QSizePolicy.Expanding, QSizePolicy.Expanding),
                            2, 2, 2, 1)
        if modificabile == True:
            self.grid.addWidget(User_int_utility.crea_green_or_red_push_button("Aggiungi uno spettacolo", self.show_aggiungi_spettacolo,
                                QSizePolicy.Expanding, QSizePolicy.Expanding, "G"), 2, 3)
            self.grid.addWidget(User_int_utility.crea_green_or_red_push_button("Elimina uno spettacolo", self.show_elimina_spettacolo,
                                                  QSizePolicy.Expanding, QSizePolicy.Expanding, "R"), 3, 3)

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Sp"))
        ext_layout.addLayout(self.grid)

        self.update_ui()

        self.setLayout(ext_layout)


    def crea_group_box(self):
        self.lista_list_view = []
        for i in [1, 2, 3, 4]:
            box = QGroupBox()
            box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            box.setTitle("Sala " + str(i))

            v_layout = QVBoxLayout()
            self.lista_list_view.append(User_int_utility.crea_list_view())
            v_layout.addWidget(self.lista_list_view[i-1])
            v_layout.setContentsMargins(10, 35, 10, 5)
            box.setLayout(v_layout)
            self.grid.addWidget(box, 1, i-1)


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

    def update_ui(self):
        self.label_giorno.setText("Film in programma per il giorno " + str(self.data.day()) + "-" + str(self.data.month()) + ""
                                  "-" + str(self.data.year()))

        lista_spettacoli_giornaliera = self.controller.get_spettacoli_by_day(self.data)

        self.listviews_models = []
        for i in range(len(self.lista_list_view)):
            spettacoli_sala = lista_spettacoli_giornaliera[i]

            self.listviews_models.append(QStandardItemModel(self.lista_list_view[i]))
            if len(spettacoli_sala) > 0:
                for spettacolo in spettacoli_sala:
                    item = QStandardItem()
                    item.setText(spettacolo.film.titolo + "   " + spettacolo.ora_inizio.toString("HH:mm") + "-" + spettacolo.ora_fine.toString("HH:mm"))
                    item.setEditable(False)
                    self.listviews_models[i].appendRow(item)
            else:
                item = QStandardItem()
                item.setText("Nessuno spettacolo in programma")
                item.setEditable(False)
                self.listviews_models[i].appendRow(item)
            self.lista_list_view[i].setModel(self.listviews_models[i])

    def cambia_giorno(self):
        self.data = self.calendario.selectedDate()
        self.update_ui()

    def show_elimina_spettacolo(self):
        pass

    def show_aggiungi_spettacolo(self):
        self.vista_aggiungi_spettacolo = VistaAggiungiSpettacoli(self.controller, self.modifica_visibilita, self.data, self.update_ui)

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.controller.save_data()     #salvataggio dei dati
        self.callback()                 #fa riapparire la finestra precedente
