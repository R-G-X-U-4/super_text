# SuperText

A lightweight, feature-rich text editor built with PyQt5, designed for writing documents, office papers, and quick note-taking with integrated markdown support and live formatting.

---

###  Screenshots

<img width="606" alt="SuperText UI" src="https://github.com/user-attachments/assets/3d26ef02-b6e9-4efd-a161-42664f18f2cd" />

<img width="1271" alt="SuperText Hello World Example" src="https://github.com/user-attachments/assets/23f95e6e-6f9f-456e-a3aa-c47896df4b4e" />


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Architecture](#architecture)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

**SuperText** is a modern text editor that combines essential writing features with smart markdown parsing. Whether you're drafting documents, taking notes, or composing office papers, SuperText provides an intuitive interface with powerful editing capabilities.

The editor supports real-time markdown parsing, text formatting (bold, italic, underline), font resizing, and a live character counter. Files are saved in a lightweight format (`.srt`) optimized for document preservation.

---

## Features

**Core Features:**
- **Markdown Support** — Type markdown syntax (e.g., `# Heading`, `**bold**`, `*italic*`) and press Enter to auto-format
- **Text Formatting** — Bold, italic, underline, text color, and background color via toolbar
- **Font Resizing** — Adjust font size with `Ctrl+=` / `Ctrl+-` (or use the resize dialog)
- **Live Character Counter** — Real-time character count displayed in the status bar
- **File Operations** — Open and save documents in `.srt` format
- **Auto-Save Toggle** — Optional automatic saving while you work

---

## Installation

### Requirements
- **Python 3.8+** (tested with Python 3.14)
- **PyQt5**

### Setup

#### Option 1: Quick Install (with pip)
```powershell
python -m pip install PyQt5
```

#### Option 2: Virtual Environment (Recommended)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install PyQt5
```

---

## Getting Started

> **Note** This Guide is for developers who want to contribute to this project  or want to test the source code for users conside download and install the setup for easy installetion from [Releases](https://github.com/R-G-X-U-4/super_text/releases)

### Running the Application

```powershell
cd path/to/your_dir/super-text
python main.py
```

Or, with your Python executable:
```powershell
& C:user/your_dir/AppData/Local/Programs/Python/Python314/python.exe main.py
```

The SuperText window will open, ready for editing.

---

## Usage

### Markdown Formatting

When you type markdown syntax and press **Enter**, the line is automatically formatted:

| Syntax | Result | Example |
|--------|--------|---------|
| `# text` | Heading 1 (18pt bold) | `# My Title` |
| `## text` | Heading 2 (16pt bold) | `## Section` |
| `### text` | Heading 3 (14pt bold) | `### Subsection` |
| `**text**` | Bold | `**important**` |
| `*text*` | Italic | `*emphasis*` |
| `` `text` `` | Code (monospace) | `` `code snippet` `` |
| `- item` | Bullet point | `- List item` |

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| New Document | `Ctrl+N` |
| Open File | `Ctrl+O` |
| Save File | `Ctrl+S` |
| Increase Font | `Ctrl+=` |
| Decrease Font | `Ctrl+-` |
| Reset Font | `Ctrl+0` |

### Text Formatting

- **Bold:** Click the Bold button or use `Ctrl+B` equivalent
- **Italic:** Click the Italic button
- **Underline:** Click the Underline button
- **Color:** Use the color picker to change text color
- **Background:** Apply background color to highlighted text

### File Management

- **New:** Create a blank document (will prompt to save if current document has unsaved changes)
- **Open:** Browse and open existing `.srt` files
- **Save:** Save your document (prompts for filename on first save)
- **Auto-Save:** Toggle automatic saving via the checkbox in the toolbar

---

## Architecture

### Project Structure

```
superText/
├── main.py                    # Application entry point
├── windows/
│   ├── __init__.py
│   └── main_window.py         # Main UI logic & event handling
├── core/
│   ├── __init__.py
│   └── file_manager.py        # File I/O operations
├── utils/
│   ├── __init__.py
│   ├── markdown_parser.py     # Markdown parsing engine
│   └── message_helper.py      # Dialog & notification helpers
├── ui/
│   └── windows.ui             # Qt Designer UI definition
└── README.md                  # This file
```

### Key Modules

- **`main_window.py`** — Core application logic, event handling, and UI state management
- **`markdown_parser.py`** — Parses markdown syntax and applies formatting
- **`file_manager.py`** — Handles file dialogs, reading, and writing
- **`message_helper.py`** — User-facing dialogs (about, license, confirmations)

---

## Contributing

We appreciate your interest in contributing to SuperText! 

### How to Contribute

1. **Report Issues** — Found a bug? Create an issue with details and steps to reproduce
2. **Suggest Features** — Have an idea? Open a feature request discussion
3. **Code Contributions** — Fork the repo, make changes, and submit a pull request

### Development Guidelines

- Follow PEP 8 style conventions
- Add docstrings to new functions and classes
- Test your changes before submitting a PR
- Include a clear commit message and PR description

### Feature Ideas for Contributors

- Word count and reading-time estimation
- Settings persistence (theme, font preferences, recent files)
- Export to HTML, PDF, or Markdown
- Syntax highlighting for code blocks
- Find & Replace functionality
- Dark Mode / Light Mode themes

---

## License

**Code:** This project's source code is provided under the **MIT License** read [License file](https://github.com/R-G-X-U-4/super_text/blob/main/LICENSE).

**Software:** SuperText and its branding are provided under the [RGXU4 Software License Agreement](https://github.com/R-G-X-U-4/Super_text_releases/blob/main/License.md).

For full license text, see the full license file above For software's  license checkout [RGXU4 SOFTWARE LICENSE TERMS](https://github.com/R-G-X-U-4/Super_text_releases/blob/main/License.md)

---

## Copyright

© RGXU4 Corporation. All rights reserved.


The logo and name of RGXU4 are the exclusive property of the RGXU4 team. Use of the RGXU4 name or logo for commercial purposes is strictly prohibited without prior written permission.
---

## Support & Contact

For questions, feedback, or support, please reach out through:
- GitHub Issues
- Project repository discussions

---

**Last Updated:** November 2025  
**Version:** 0.1 (Beta)
