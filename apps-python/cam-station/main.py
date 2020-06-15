import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow
from PyQt5.Qt import PYQT_VERSION_STR
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    print("PyQt version:", PYQT_VERSION_STR)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Resources/fire.png"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())