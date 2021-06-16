import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication

from Home.Views.VistaLogin import VistaLogin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI Semibold", 15))
    vista_login = VistaLogin()
    vista_login.show()
    sys.exit(app.exec())


