from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QSizePolicy, QLabel, QHBoxLayout, QPushButton, QLineEdit, QDesktopWidget, QComboBox, \
    QSpinBox, QFormLayout, QListView


class User_int_utility():
    primary_color = "#333"     #codici dei principali colori dell'interfaccia
    secondary_color = "#ADAA01"
    tertiary_color = "#B50202"

    #metodo che crea la parte superiore dell'interfaccia in cui è presente il logo a cui,
    #in base al parametro passato, affianca un sottotitolo
    @staticmethod
    def crea_banda_superiore(sottotitolo=None):
        o_layout = QHBoxLayout()
        logo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_logo/Logo.png'), QSizePolicy.Minimum, QSizePolicy.Minimum)
        riempimento = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Riempimento.png'), QSizePolicy.Expanding,QSizePolicy.Minimum)

        o_layout.addWidget(logo)
        o_layout.addWidget(riempimento)
        if sottotitolo == "Di":             # Di = dipendenti
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_dipendente.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Se":           #Se = servizi
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_servizi.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Re":           #Re = report
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_report.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Fi":           #Fi = film
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_film.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Sp":           #Sp = programmazione spettacoli
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_spettacoli.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Ma":           #Ma = manuale
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_manuale.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Bi":           #Bi = vendita biglietti
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_biglietti.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Cl":           #Cl = gestione cliente
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_clienti.png'),QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Te":           #Te = rilascio tessera
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_tessera.png'), QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        elif sottotitolo == "Ab":           #Ab = rilascio abbonamento
            sottotitolo = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Sott_abbonamento.png'), QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(sottotitolo)
        else:
            riempimento2 = User_int_utility.crea_label_con_imm(QPixmap('Immagini/Elem_Logo/Riempimento2.png'), QSizePolicy.Minimum, QSizePolicy.Minimum)
            o_layout.addWidget(riempimento2)

        return o_layout


    # metodo statico che riceve una Qpixmap e le desiderate SizePolicy
    # e restituisce una label contenente l'immagine
    @staticmethod
    def crea_label_con_imm(pixmap, oSizePolicy, vSizePolicy):
        label = QLabel()
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setContentsMargins(0, 0, 0, 0)
        label.setSizePolicy(oSizePolicy, vSizePolicy)
        return label

    #metodo che ritorna un push button con titolo, collegamento, tooltip e sizePolicy passati come parametri
    @staticmethod
    def crea_push_button(titolo, on_click, tooltip, oSizePolicy, vSizePolicy):
        button = QPushButton(titolo)
        button.setSizePolicy(oSizePolicy, vSizePolicy)
        button.clicked.connect(on_click)
        button.setStyleSheet("QPushButton"  # stile del pulsante
                             "{"
                             "border-radius: 7px;"
                             "background-color : " + User_int_utility.secondary_color + ";"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "border-width: 4px;"
                             "border-style: flat;"
                             "border-color: " + User_int_utility.primary_color + ";"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #9C9900 ;"                                                        
                             "}"
                         )
        button.setToolTip(tooltip)
        button.setToolTipDuration(2200)
        return button

    #Metodo statico che ritorna una label con titolo passato come parametro e stile predefinito
    @staticmethod
    def crea_label(titolo):
        label = QLabel(titolo)
        label.setStyleSheet("color: #DDD;"
                            "background-color: #222")
        return label

    #metodo statico che ritorna una QlineEdit con uno stile predefinito
    @staticmethod
    def crea_casella_testo(placeholder=None):
        line = QLineEdit()
        line.setPlaceholderText(placeholder)
        line.setStyleSheet("border-radius: 6px;"
                           "padding: 0 8px;"
                           "background: #111;"
                           "color: #DDD")
        return line

    #sposta il widget che gli viene passato al centro dello schermo, qualunque sia la dimensione di quest'ultimo
    @staticmethod
    def sposta_al_centro(widget):
        qtRectangle = widget.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        widget.move(qtRectangle.topLeft())

    # Funzione che riceve funzione da collegare al pulsante, icona del pulsante e tooltip e
    # restituisce un pulsante collegato alla funzione passata
    @staticmethod
    def crea_home_push_button(on_click, icon, tooltip):
        button = QPushButton()
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        button.setStyleSheet("QPushButton"  # stile del pulsante
                             "{"
                             "border-radius: 7px;"
                             "background-color : " + User_int_utility.primary_color + ";"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "border-width: 3px;"
                             "border-style: flat;"
                             "border-color: " + User_int_utility.primary_color + ";"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : " + User_int_utility.secondary_color + " ;"
                             "}")
        button.setIcon(icon)
        button.setIconSize(QSize(80, 60))
        button.setToolTip(tooltip)
        button.setToolTipDuration(2200)
        return button

    @staticmethod
    def crea_combo_box(lista_elementi):
        combo_box = QComboBox()
        combo_box_model = QStandardItemModel(combo_box)
        for elemento in lista_elementi:
            item = QStandardItem()
            item.setText(elemento)
            item.setEditable(False)
            combo_box_model.appendRow(item)
        combo_box.setModel(combo_box_model)
        combo_box.setStyleSheet("border-radius: 6px;"
                                "padding: 0 8px;"
                                "background: #111;"
                                "color: #DDD")
        return combo_box

    @staticmethod
    def crea_spin_box(min, max, initial_value):
        spin_box = QSpinBox()
        spin_box.setMinimum(min)
        spin_box.setMaximum(max)
        spin_box.setValue(initial_value)
        spin_box.setStyleSheet("border-radius: 6px;"
                               "padding: 0 8px;"
                               "background: #111;"
                               "color: #DDD")
        return spin_box

    @staticmethod
    def crea_green_or_red_push_button(titolo, on_click, oSizePolicy, vSizePolicy, color="R"):
        button = QPushButton(titolo)
        button.setSizePolicy(oSizePolicy, vSizePolicy)
        button.clicked.connect(on_click)
        if color == "G":
            button.setStyleSheet("QPushButton"  
                             "{"
                             "border-radius: 7px;"
                             "background-color : #18E200 ;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "border-width: 4px;"
                             "border-style: flat;"
                             "border-color: " + User_int_utility.primary_color + ";"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #15C600 ;"
                             "}"
                             )
        else:
            button.setStyleSheet("QPushButton"  
                                 "{"
                                 "border-radius: 7px;"
                                 "background-color : #FF0000 ;"
                                 "}"
                                 "QPushButton::pressed"
                                 "{"
                                 "border-width: 4px;"
                                 "border-style: flat;"
                                 "border-color: " + User_int_utility.primary_color + ";"
                                 "}"
                                 "QPushButton::hover"
                                 "{"
                                 "background-color : #D50000 ;"
                                 "}"
                                 )
        return button

    @staticmethod
    def crea_list_view():
        list_view = QListView()
        list_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        list_view.setStyleSheet("border-radius: 6px;"
                           "padding: 0 8px;"
                           "background: #111;"
                           "color: #DDD")
        return list_view


