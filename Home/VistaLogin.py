from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette, QImage, QBrush, QIcon, QKeySequence
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QSizePolicy, QGridLayout, QPushButton, QShortcut
from Utilità.User_int_utility import User_int_utility
from Home.VistaHomeAmministratore import VistaHomeAmministratore
from Home.VistaHomeBiglietteria import VistaHomeBiglietteria

class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__()
        self.setWindowTitle("Login")
        self.setGeometry(0, 0, 1000, 600)
        User_int_utility.sposta_al_centro(self)
        self.setFixedSize(self.size())

        background = QImage("Immagini/Sfondi/login_back.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        ext_layout = QVBoxLayout()
        ext_layout.addWidget(self.crea_box_login())
        ext_layout.setContentsMargins(180,200,180,200)

        self.setLayout(ext_layout)

    def crea_box_login(self):
        box = QGroupBox()
        box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        box.setStyleSheet("border-radius: 20px")

        layout = QGridLayout()

        user_image = QPushButton()
        user_image.setStyleSheet("border-style: flat;")
        user_image.setIcon(QIcon("Immagini/Icone/user_icon.png"))
        user_image.setIconSize(QSize(100,110))
        layout.addWidget(user_image, 0, 0, 1, 3)
        self.casella_codice = User_int_utility.crea_casella_testo("Inserire codice di autenticazione")
        layout.addWidget(self.casella_codice, 1, 0)

        login = QPushButton()
        login.setIcon(QIcon("Immagini/Icone/login_icon.png"))
        login.setIconSize(QSize(55,55))
        login.setStyleSheet("QPushButton::pressed"
                             "{"
                             "border-width: 5px;"
                             "border-style: flat;"
                             "border-color: " + User_int_utility.primary_color + ";"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : " + User_int_utility.secondary_color + ";"  
                             "}")
        layout.addWidget(login, 1, 1)
        login.clicked.connect(self.accedi)

        box.setLayout(layout)
        return box

    def accedi(self):
        if self.casella_codice.text() == "A":
            self.home_amm = VistaHomeAmministratore(self.modifica_visibilita)
            self.home_amm.show()
        if self.casella_codice.text() == "D":
            self.home_big = VistaHomeBiglietteria(self.modifica_visibilita)
            self.home_big.show()
        self.casella_codice.setText("")

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)


