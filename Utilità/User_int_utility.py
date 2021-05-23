from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QSizePolicy, QLabel, QHBoxLayout


class User_int_utility():
    geometry = [50, 50]
    primary_color = "#333"
    secondary_color = "#ADAA01"
    tertiary_color = "#C90101"

    #metodo statico che restituisce un QHBoxLayout contenente due label che formano il logo del cinema
    @staticmethod
    def crea_logo():
        orizzontal_layout = QHBoxLayout()

        striscia = User_int_utility.crea_label_con_imm(QPixmap('Immagini\\Logo.png'), QSizePolicy.Minimum, QSizePolicy.Minimum)
        riempimento = User_int_utility.crea_label_con_imm(QPixmap('Immagini\\Riempimento.png'), QSizePolicy.Expanding, QSizePolicy.Minimum)

        orizzontal_layout.addWidget(striscia)
        orizzontal_layout.addWidget(riempimento)

        return orizzontal_layout


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


