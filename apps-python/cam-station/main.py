import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow
from PyQt5.Qt import PYQT_VERSION_STR

if __name__ == "__main__":
    print("PyQt version:", PYQT_VERSION_STR)
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())