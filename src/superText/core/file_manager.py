# ============================================================================
# SuperText - File Manager Module
# Copyright (c) RGXU4 Corporation. All rights reserved.
# License: RGXU4 License Agreement
# This software is provided "as-is" without warranty.
# ============================================================================

from PyQt5.QtWidgets import QFileDialog

class FileManager:
    def save(self, content, file_path=None, parent=None):
        if file_path is None:
            file_path, _ = QFileDialog.getSaveFileName(
                parent,
                "Save SuperText File",
                "",
                "SuperText File (*.srt);;All Files (*)"
            )
            if not file_path:
                return None

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path

    def open(self, parent=None):
        file_name, _ = QFileDialog.getOpenFileName(
            parent,
            "Open SuperText File",
            "",
            "SuperText File (*.srt);;All Files (*)"
        )
        if not file_name:
            return None

        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        return content, file_name
