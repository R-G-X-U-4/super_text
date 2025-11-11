from PyQt5.QtWidgets import QApplication
from windows.main_window import TextEditWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = TextEditWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
