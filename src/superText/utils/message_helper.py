# ============================================================================
# SuperText - Message Helper Module
# Copyright (c) RGXU4 Corporation. All rights reserved.
# License: RGXU4 License Agreement
# This software is provided "as-is" without warranty.
# ============================================================================

from PyQt5.QtWidgets import QMessageBox

class MessageBoxHelper:
    def ask_save_confirmation(self):
        reply = QMessageBox.question(
            None,
            'Unsaved Changes',
            'Do you want to save before creating a new file?',
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
        )
        if reply == QMessageBox.Yes:
            return 'yes'
        elif reply == QMessageBox.No:
            return 'no'
        else:
            return 'cancel'

    def show_about(self):
        QMessageBox.information(
            None,
            'About',
            'SuperText is a text editor software for writing documents and office papers.\n'
            'Supports markdown and clean documents.\nRelease v0.1\n(c) SuperText RGXU4 Corporation'
        )

    def show_license(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle('License Agreement')
        msg_box.setText("""<h2>RGXU4 License Agreement</h2>
<p>By using this software, you agree to the following terms:</p>
<h3>1. License to Use</h3>
<p>You may use this software for personal purposes according to these terms.</p>
<h3>2. Restrictions</h3>
<ul>
<li>You may <b>not</b> sell, redistribute, or sublicense copies of this software.</li>
<li>You may modify the software only if it is open-source, for <b>personal use only</b>.</li>
</ul>
<h3>3. Ownership of Content</h3>
<p>Any content you create using this software belongs to you. The software itself remains property of RGXU4.</p>
<h3>4. Prohibited Uses</h3>
<p>You may not use this software to create illegal content.</p>
<h3>5. Disclaimer</h3>
<p>The software is provided <b>"as-is"</b> without warranty.</p>""")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
