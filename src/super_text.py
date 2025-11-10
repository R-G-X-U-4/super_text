from PyQt5.QtWidgets import QApplication , QMainWindow , QMessageBox , QFileDialog , QCheckBox
from PyQt5.uic import loadUi
import sys
# import markdown  # --> for markdown support 
import time 


class TextEdit(QMainWindow):
    def __init__(self):
        super(TextEdit,self).__init__()
        loadUi('windows.ui',self)
        self.current_file = None 
        self.actionNew.triggered.connect(self.new)
        self.actionSave.triggered.connect(self.save)
        self.actionOpen.triggered.connect(self.open)
        self.actionAbout.triggered.connect(self.about)
        self.actionLicense.triggered.connect(self.license_agreement)
        self.checkBox.stateChanged.connect(self.toggale_autosave)
        self.autosave_enabled = True 
      
    def new(self):
        if not self.textEdit.document().isEmpty():
            warninig_message = QMessageBox.question( self,'Unsaved changes','There is one unsaved document do you want to save before creating a new one ?',
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            if warninig_message == QMessageBox.Yes :
                self.save() # --> Not implemented yet !
                self.textEdit.clear()
                self.current_file = None
            elif warninig_message == QMessageBox.No:
                self.textEdit.clear()
                self.current_file = None
            elif warninig_message == QMessageBox.Cancel:
                return 
            
    def save(self):
        if self.current_file is None :
            self.saveas()
        else:
            with open(self.current_file ,'w') as f:
                f.write(self.textEdit.toPlainText())

    def saveas(self):
        file_name,_ = QFileDialog.getSaveFileName(self,'SaveFile','','Text File(*.txt);; All File(*)')
        if file_name :
            self.current_file = file_name
            self.save()

    def open(self):
        file_name,_= QFileDialog.getOpenFileName(self,'Open File','','Text File (*.txt);; All File(*)')
        if file_name:
            with open(file_name,'r',encoding='utf8') as file: 
                file_content = file.read()
                self.textEdit.setPlainText(file_content)
                self.current_file = file_name
    
    def about(self):
        QMessageBox.information(self,'About','SuperText is text editor software that can help you  write documents and office pappers in one software \n Super Text also support markdown  that can help you write clean documents \n  Release version  0.1 \n (c) Super Text RGXU4 corporation')
        
    def license_agreement(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle('License Agreement')
        msg_box.setText("""
<h2>RGXU4 License Agreement</h2>
<p>By using this software, you agree to the following terms:</p>

<h3>1. License to Use</h3>
<p>You may use this software for personal purposes according to these terms.</p>

<h3>2. Restrictions</h3>
<ul>
<li>You may <b>not</b> sell, redistribute, or sublicense copies of this software.</li>
<li>You may modify the software only if it is open-source, for <b>personal use only</b>.</li>
</ul>

<h3>3. Ownership of Content</h3>
<p>Any content you create using this software belongs to you, for personal or commercial use. The software itself remains the property of RGXU4 Corporation.</p>

<h3>4. Prohibited Uses</h3>
<p>You may not use this software to create illegal content.</p>

<h3>5. Disclaimer</h3>
<p>The software is provided <b>"as-is"</b> without warranty. RGXU4 Corporation is not responsible for any damage or loss resulting from its use.</p>
""")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def toggale_autosave(self,state):
        if self.checkBox.isChecked():
            self.autosave_enabled = True 
            print('Alhumdullah checked !')
        else :
            print('Alhumdullah unchacked')
    def auto_save (self):
        if self.autosave_enabled and self.current_file is not None:
             with open(self.current_file ,'w') as f:
                 f.write(self.textEdit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = TextEdit()
    ui.show()
    app.exec_()

