# ============================================================================
# SuperText - Markdown Parser Module
# Copyright (c) RGXU4 Corporation. All rights reserved.
# License: RGXU4 License Agreement
# This software is provided "as-is" without warranty.
# ============================================================================

import re
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QFont, QColor

class MarkdownParser:
    """Parse and apply markdown formatting to text"""
    
    def __init__(self, text_edit):
        self.text_edit = text_edit
    
    def parse_line(self, line):
        """
        Parse a line of markdown and return formatting info
        Returns: (processed_text, formatting_dict)
        """
        
        # Heading levels: # = H1, ## = H2, etc.
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2)
            return text, {'type': 'heading', 'level': level}
        
        # Bold: **text** or __text__
        bold_match = re.match(r'^[\*_]{2}(.+?)[\*_]{2}', line)
        if bold_match:
            text = bold_match.group(1)
            return text, {'type': 'bold'}
        
        # Italic: *text* or _text_
        italic_match = re.match(r'^[\*_]([^\*_]+)[\*_]', line)
        if italic_match:
            text = italic_match.group(1)
            return text, {'type': 'italic'}
        
        # Code: `text`
        code_match = re.match(r'^`(.+?)`', line)
        if code_match:
            text = code_match.group(1)
            return text, {'type': 'code'}
        
        # Unordered list: - item or * item
        list_match = re.match(r'^[\-\*]\s+(.+)$', line)
        if list_match:
            text = list_match.group(1)
            return '• ' + text, {'type': 'list'}
        
        return line, {'type': 'normal'}
    
    def apply_formatting(self, cursor, text, formatting):
        """Apply formatting to text at cursor position"""
        fmt = QTextCharFormat()
        
        if formatting['type'] == 'heading':
            level = formatting['level']
            size = 18 - (level * 2)  # H1=18, H2=16, H3=14, etc.
            fmt.setFontPointSize(max(size, 10))
            fmt.setFontWeight(QFont.Bold)
        
        elif formatting['type'] == 'bold':
            fmt.setFontWeight(QFont.Bold)
        
        elif formatting['type'] == 'italic':
            fmt.setFontItalic(True)
        
        elif formatting['type'] == 'code':
            fmt.setFontFamily("Courier New")
            fmt.setBackground(QColor(240, 240, 240))
        
        elif formatting['type'] == 'list':
            fmt.setFontPointSize(12)
        
        cursor.insertText(text, fmt)
    
    def process_markdown_line(self):
        """Process the current line when Enter is pressed"""
        cursor = self.text_edit.textCursor()
        block = cursor.block()
        text = block.text().strip()
        
        if not text:
            # If empty line, just insert newline normally
            cursor.insertText('\n')
            return True
        
        # Parse the line
        processed_text, formatting = self.parse_line(text)
        
        # Check if we found markdown
        if formatting['type'] == 'normal':
            # No markdown found, insert newline normally
            cursor.insertText('\n')
            return True
        
        # Select and replace the entire line
        cursor.select(cursor.LineUnderCursor)
        cursor.removeSelectedText()
        
        # Move to beginning of line
        cursor.movePosition(cursor.StartOfLine)
        
        # Apply formatting
        self.apply_formatting(cursor, processed_text, formatting)
        
        # Add newline after formatted text
        cursor.insertText('\n')
        
        self.text_edit.setTextCursor(cursor)
        return True
