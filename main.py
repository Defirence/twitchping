import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle("Twitch Ping v0.1")
    w.show()
    sys.exit(app.exec_())
