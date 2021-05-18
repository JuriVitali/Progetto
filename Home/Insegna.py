from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QSizePolicy

class Insegna(QWidget):
    def __init__(self, parent=None):
        super(Insegna, self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        striscia = QLabel('  Ciak e Azione')
        striscia.setFont(QFont('Segoe Script', 38))
        striscia.setStyleSheet("color:  #00BF7F;"
                               "background-color: #111;"
                               "radius: 10px;"
                               "offset: -3,-3"
                               )
        striscia.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout.addWidget(striscia)
        self.setLayout(layout)
