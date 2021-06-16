from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QSizePolicy, QLabel, QHBoxLayout, QPushButton, QLineEdit, QDesktopWidget, QComboBox, \
    QSpinBox, QListView, QDoubleSpinBox, QDateEdit


class User_int_utility():

    # codici dei principali colori dell'interfaccia
    primary_color = "#333"              #grigio
    secondary_color = "#ADAA01"         #oro
    tertiary_color = "#B50202"          #rosso

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

    #Metodo statico che ritorna una label con titolo e dimensione del font passati come parametri e  stile del programma
    # Se il parametro colore è "c" viene creata una label leggeremente più chiara, altrimenti
    # ne viene creata una di un grigio più scuro
    @staticmethod
    def crea_label(titolo, fontsize=15, colore = "c"):
        label = QLabel(titolo)
        if colore == "c":
            label.setStyleSheet("color: #DDD;"
                            "background-color: #222;")
        else:
            label.setStyleSheet("color: #DDD;"
                            "background-color: #111;")
        label.setFont(QFont("Segoe UI Semibold", fontsize))
        return label

    # metodo statico che ritorna una QlineEdit con stile del programma
    # e con il placeholder passatogli
    @staticmethod
    def crea_casella_testo(placeholder=None, oSizePolicy=QSizePolicy.Expanding):
        line = QLineEdit()
        line.setSizePolicy(oSizePolicy, QSizePolicy.Fixed)
        line.setPlaceholderText(placeholder)
        line.setStyleSheet("border-radius: 6px;"
                           "padding: 0 8px;"
                           "background: #111;"
                           "color: #DDD")
        return line

    # Metodo statico che sposta il widget che gli viene passato al centro dello schermo,
    # qualunque sia la dimensione di quest'ultimo
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

    # metodo statico che crea una combo box i cui elementi sono gli elementi della
    # lista passata come parametro
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

    #metodo statico che crea una spin box. I suoi valori minimo, massimo e iniziale sono
    #quelli passati come parametri. Lo step di default è 1 ma può essere modificato
    # passando quello desiderato come quarto parametro
    @staticmethod
    def crea_spin_box(min, max, initial_value, step=1):
        spin_box = QSpinBox()
        spin_box.setMinimum(min)
        spin_box.setMaximum(max)
        spin_box.setValue(initial_value)
        spin_box.setSingleStep(step)
        spin_box.setStyleSheet("border-radius: 6px;"
                               "padding: 0 8px;"
                               "background: #111;"
                               "color: #DDD")
        return spin_box

    # metodo statico che crea una doublespinbox il cui valore ha 2 cifre decimali.
    # I suoi valori minimo, massimo e iniziale sono
    # quelli passati come parametri. Lo step di default è 0.10 ma può essere modificato
    # passando quello desiderato come quarto parametro
    @staticmethod
    def crea_double_spin_box(min, max, initial_value, step=0.10):
        double_spin_box = QDoubleSpinBox()
        double_spin_box.setMinimum(min)
        double_spin_box.setMaximum(max)
        double_spin_box.setValue(initial_value)
        double_spin_box.setSingleStep(step)
        double_spin_box.setStyleSheet("border-radius: 6px;"
                               "padding: 0 8px;"
                               "background: #111;"
                               "color: #DDD")
        return double_spin_box

    # Crea una QDateEdit (casella di testo per l'inserimento di una data) con stile del programma.
    # Il primo parametro è la data "minima" consentita mentre il secondo è
    # quella massima
    @staticmethod
    def crea_date_edit(min, max):
        date_edit = QDateEdit()
        date_edit.setMinimumDate(min)
        date_edit.setMaximumDate(max)
        date_edit.setStyleSheet("border-radius: 6px;"
                               "padding: 0 8px;"
                               "background: #111;"
                               "color: #DDD")
        return date_edit

    #metodo statico che crea un pushbutton con titolo, collegamento, size policy e colore passati.
    #il colore è verde se viene passato "G", mentre negli altri casi è rosso
    @staticmethod
    def crea_green_or_red_push_button(titolo, on_click, oSizePolicy, vSizePolicy, color="R"):
        button = QPushButton(titolo)
        button.setSizePolicy(oSizePolicy, vSizePolicy)
        button.clicked.connect(on_click)
        if color == "G":
            button.setStyleSheet("QPushButton"  
                             "{"
                             "border-radius: 7px;"
                             "background-color : #22C808 ;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "border-width: 4px;"
                             "border-style: flat;"
                             "border-color: " + User_int_utility.primary_color + ";"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #1AB302 ;"
                             "}"
                             )
        else:
            button.setStyleSheet("QPushButton"  
                                 "{"
                                 "border-radius: 7px;"
                                 "background-color : " + User_int_utility.tertiary_color + " ;"
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

    #metodo statico che crea una listview con stile del programma
    @staticmethod
    def crea_list_view():
        list_view = QListView()
        list_view.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        list_view.setStyleSheet("border-radius: 6px;"
                           "padding: 0 8px;"
                           "background: #111;"
                           "color: #DDD")
        return list_view

    # metodo statico che fa scomparire il widget passato se questo è visibile o lo fa apparire se
    # è nascosto
    @staticmethod
    def modifica_visibilita_finestra(widget):
        if widget.isHidden() == False:
            widget.hide()
        else:
            widget.show()

    #metodo statico che setta lo stile della finestra passatagli, dei suoi messagebox e dei
    # suoi QGroupBox
    @staticmethod
    def set_window_style(widget):
        widget.setStyleSheet("QWidget {"
                             "background-color : " + User_int_utility.primary_color + ";"
                             "}"
                             "QMessageBox {"
                             "background-color: #EEE;"
                             "}"
                             "QMessageBox QLabel {"
                             "background-color: #EEE;"
                             "color: " + User_int_utility.tertiary_color + ";"
                             "}"
                             "QMessageBox QPushButton { "
                             "color: white;"
                             "background-color : " + User_int_utility.tertiary_color + " ;"
                             "}"
                             "QGroupBox"
                             "{"
                             "background-color: #222;"  
                             "border-radius: 8px"
                             "}"
                             "QGroupBox::title"
                             "{"
                             "background-color: " + User_int_utility.tertiary_color + ";"
                             "border-radius: 4px"
                             "}"
                             )

    # Metodo che applica lo stile del programma con sfondo più scuro al QGroupBox passatogli
    @staticmethod
    def box_scuro(box):
        box.setStyleSheet("QGroupBox"
                          "{"
                          "background-color: #111;"
                          "border-radius: 8px"
                          "}"
                          "QGroupBox::title {"
                          "background-color: " + User_int_utility.tertiary_color + ";"
                          "border-radius: 4px"
                          "}"
                          )





