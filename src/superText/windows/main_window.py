from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from core.file_manager import FileManager
from utils.message_helper import MessageBoxHelper
from PyQt5.QtGui import QFont , QColor
from PyQt5.QtWidgets import QColorDialog
import os

# Get absolute path of UI file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = os.path.join(BASE_DIR, '..', 'ui', 'windows.ui')

class TextEditWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(UI_PATH, self)

        # Core logic objects
        self.file_manager = FileManager()
        self.current_file = None
        self.msg_helper = MessageBoxHelper()
        self.autosave_enabled = True

        # Connect signals
        self.actionNew.triggered.connect(self.new_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionAbout.triggered.connect(self.about)
        self.actionLicense.triggered.connect(self.license_agreement)
        self.checkBox.stateChanged.connect(self.toggle_autosave)
        self.actionBold.triggered.connect(self.make_bold)
        self.actioncolorepicker.triggered.connect(self.colore_packer)
        self.actionitalic.triggered.connect(self.make_italic)

    # ---------------- File Actions ----------------
    def new_file(self):
        if not self.textEdit.document().isEmpty():
            answer = self.msg_helper.ask_save_confirmation()
            if answer == 'yes':
                self.save_file()
            elif answer == 'cancel':
                return
        self.textEdit.clear()
        self.current_file = None

    def save_file(self):
         html_content = self.textEdit.toHtml()
         self.current_file = self.file_manager.save(html_content, self.current_file)

    def open_file(self):
        result = self.file_manager.open(self)  # self is the parent widget
        if result:
            content, file_path = result
            self.textEdit.setHtml(content)
            self.current_file = file_path



    # ---------------- Helpers ----------------
    def toggle_autosave(self, state):
        self.autosave_enabled = self.checkBox.isChecked()
        print("Autosave:", self.autosave_enabled)

    def auto_save(self):
        if self.autosave_enabled and self.current_file is not None:
            content = self.textEdit.toPlainText()
            self.file_manager.save(content, self.current_file)

    # ---------------- Dialogs ----------------
    def about(self):
        self.msg_helper.show_about()

    def license_agreement(self):
        self.msg_helper.show_license()
    def make_bold(self):
        cursore = self.textEdit.textCursor()
        fmt = cursore.charFormat()
        if fmt.fontWeight() == QFont.Bold:
            fmt.setFontWeight(QFont.Normal)
        else :
            fmt.setFontWeight(QFont.Bold)
        cursore.mergeCharFormat(fmt)
    def colore_packer(self):
        colore = QColorDialog.getColor()

        if colore.isValid():
            cursore = self.textEdit.textCursor()
            fmt = cursore.charFormat()
            fmt.setForeground(colore)
            cursore.mergeCharFormat(fmt)
    def  make_italic(self):
        cursore = self.textEdit.textCursor()
        fmt = cursore.charFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        cursore.mergeCharFormat(fmt)


        
