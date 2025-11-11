from PyQt5.QtWidgets import QFileDialog

class FileManager:
    def save(self, content, file_path=None):
        """Save content to file. Returns the file path."""
        if file_path is None:
            file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text Files (*.txt);; All Files (*)")
            if not file_path:
                return None
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path

    def open(self):
        """Open file and return content and path"""
        file_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text Files (*.txt);; All Files (*)")
        if not file_path:
            return None, None
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content, file_path
