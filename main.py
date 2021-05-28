import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication

from Home.VistaHome_amministratore import VistaHome_amministratore

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI Semibold", 15))
    vista_home = VistaHome_amministratore()
    vista_home.show()
    sys.exit(app.exec())


