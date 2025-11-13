# ============================================================================
# SuperText - Main Window Module
# Copyright (c) RGXU4 Corporation. All rights reserved.
# License: RGXU4 License Agreement
# This software is provided "as-is" without warranty.
# ============================================================================

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
        self.actionresizeing.triggered.connect(self.resize_text)
        self.actionunderline.triggered.connect(self.make_underline)
        self.actiontext_bg_colore.triggered.connect(self.set_text_background_color)
        
        # Initialize font size
        self.current_font_size = 12
        
        # Setup keyboard shortcuts for text resizing
        self.setup_resize_shortcuts()

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

    # -------- Text Resizing --------
    def setup_resize_shortcuts(self):
        """Setup keyboard shortcuts for text resizing"""
        from PyQt5.QtWidgets import QShortcut
        from PyQt5.QtGui import QKeySequence
        
        # Ctrl++ for increase font size
        QShortcut(QKeySequence(self.tr("Ctrl+Plus")), self, self.increase_font_size)
        QShortcut(QKeySequence(self.tr("Ctrl+=")), self, self.increase_font_size)
        
        # Ctrl+- for decrease font size
        QShortcut(QKeySequence(self.tr("Ctrl+Minus")), self, self.decrease_font_size)
        QShortcut(QKeySequence(self.tr("Ctrl+-")), self, self.decrease_font_size)
        
        # Ctrl+0 for reset to default
        QShortcut(QKeySequence(self.tr("Ctrl+0")), self, self.reset_font_size)

    def resize_text(self):
        """Open a dialog to resize text"""
        from PyQt5.QtWidgets import QSpinBox, QDialog, QVBoxLayout, QPushButton, QLabel
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Resize Text")
        dialog.setGeometry(100, 100, 300, 150)
        
        layout = QVBoxLayout()
        
        # Label
        label = QLabel(f"Current Size: {self.current_font_size}pt")
        layout.addWidget(label)
        
        # Spin box for font size
        spin_box = QSpinBox()
        spin_box.setMinimum(8)
        spin_box.setMaximum(72)
        spin_box.setValue(self.current_font_size)
        spin_box.setSuffix("pt")
        layout.addWidget(spin_box)
        
        # Apply button
        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(lambda: self.apply_font_size(spin_box.value(), dialog))
        layout.addWidget(apply_btn)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def increase_font_size(self):
        """Increase font size by 2pt"""
        if self.current_font_size < 72:
            self.current_font_size += 2
            self.apply_font_size_to_all(self.current_font_size)

    def decrease_font_size(self):
        """Decrease font size by 2pt"""
        if self.current_font_size > 8:
            self.current_font_size -= 2
            self.apply_font_size_to_all(self.current_font_size)

    def reset_font_size(self):
        """Reset font size to default (12pt)"""
        self.current_font_size = 12
        self.apply_font_size_to_all(self.current_font_size)

    def apply_font_size(self, size, dialog=None):
        """Apply font size to selected text or all text"""
        self.current_font_size = size
        self.apply_font_size_to_all(size)
        if dialog:
            dialog.close()

    def apply_font_size_to_all(self, size):
        """Apply font size to all text in the editor"""
        cursor = self.textEdit.textCursor()
        cursor.select(cursor.Document)
        
        fmt = cursor.charFormat()
        fmt.setFontPointSize(size)
        cursor.mergeCharFormat(fmt)
        
        self.textEdit.setTextCursor(cursor)

    def make_underline(self):
        """Toggle underline for selected text"""
        cursor = self.textEdit.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        cursor.mergeCharFormat(fmt)

    def set_text_background_color(self):
        """Set background color for selected text"""
        color = QColorDialog.getColor()
        
        if color.isValid():
            cursor = self.textEdit.textCursor()
            fmt = cursor.charFormat()
            fmt.setBackground(color)
            cursor.mergeCharFormat(fmt)

        


        
