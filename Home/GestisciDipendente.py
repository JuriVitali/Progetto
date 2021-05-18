from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QSizePolicy


class GestisciDipendente (QHBoxLayout):

    def __init__(self, parent=None):
        super(GestisciDipendente, self).__init__(parent)

        form = QFormLayout()
        nome = QLineEdit
        cognome = QLineEdit
        form.addRow(QLabel("Nome"), nome)
        form.addRow(QLabel("Cognome"), cognome)

        self.addLayout(form)
        self.addWidget(self.get_push_button("Conferma", self.conferma()))



    def get_push_button(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        #button.clicked.connect(on_click)
        button.setFont(QFont("Arial Black", 18))
        button.setStyleSheet("QPushButton"                   #stile del pulsante
                            "{"
                            "border-radius: 7px;"
                            "background-color : #333;"
                            "color: #eef;"
                            "}"
                             "QPushButton::pressed"
                             "{"
                             "color: #111;"
                             "border-width: 3px;"
                             "border-style: flat;"
                             "border-color: #333;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #00BF7F ;"
                             "}"
                            )
        button.setToolTipDuration(2200)
        return button

    def conferma(self):
        pass
