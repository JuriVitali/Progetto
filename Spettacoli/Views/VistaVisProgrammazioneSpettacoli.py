from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QSizePolicy, QCalendarWidget
from Utilità.User_int_utility import User_int_utility

#se modificabile è True allora sarà possibile modificare la programmazione degli spettacoli,
#altrimenti no
class VistaVisProgrammazioneSpettacoli(QWidget):
    def __init__(self, modificabile, callback):
        super(VistaVisProgrammazioneSpettacoli, self).__init__()

        self.callback = callback
        self.callback()

        self.setWindowTitle("Visualizzazione programmazione spettacoli")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QVBoxLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")

        self.data = QDate.currentDate()
        self.crea_calendario()
        self.label_giorno = User_int_utility.crea_label("")
        self.label_giorno.setStyleSheet("background-color: #222;"
                                        "color: #DDD;"
                                        "border-radius: 5px;")

        self.grid = QGridLayout()
        self.grid.setContentsMargins(10,20,10,10)
        self.crea_group_box()
        self.update_ui()

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
        self.setLayout(ext_layout)


    def crea_group_box(self):
        self.lista_label = []
        for i in [1, 2, 3, 4]:
            box = QGroupBox()
            box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            box.setTitle("Sala " + str(i))
            box.setStyleSheet("QGroupBox"
                              "{"
                              "background-color: #222;"
                              "border-radius: 8px;"
                              "}"
                              "QGroupBox::title"
                              "{"
                              "background-color: " + User_int_utility.tertiary_color + ";"
                              "border-radius: 4px"
                              "}")

            v_layout = QVBoxLayout()
            self.lista_label.append(User_int_utility.crea_label("Nessuno spettacolo in programma", 12))
            v_layout.addWidget(self.lista_label[i-1])
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

    def cambia_giorno(self):
        self.data = self.calendario.selectedDate()
        self.update_ui()

    def show_elimina_spettacolo(self):
        pass

    def show_aggiungi_spettacolo(self):
        pass

    def closeEvent(self, event):
        self.callback()
