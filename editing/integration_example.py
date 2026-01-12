"""
Example integration of diff-based editing into text_editor.py

This file shows how to integrate the DiffManager and DiffViewerWidget
into the main text editor application.
"""

from PySide6.QtWidgets import QFileDialog, QDialog, QVBoxLayout, QMessageBox
from PySide6.QtCore import Qt
from diff_viewer import DiffViewerWidget

class DiffDialog(QDialog):
    """Dialog for viewing and applying diffs."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diff Viewer")
        self.setGeometry(100, 100, 900, 600)
        
        layout = QVBoxLayout(self)
        
        self.diff_viewer = DiffViewerWidget(self)
        layout.addWidget(self.diff_viewer)
        
        # Connect signals
        self.diff_viewer.diff_applied.connect(self.accept)
        self.diff_viewer.diff_rejected.connect(self.reject)
    
    def load_diff(self, original, modified, original_name="current", modified_name="other"):
        """Load a diff into the viewer."""
        self.diff_viewer.load_diff(original, modified, original_name, modified_name)
    
    def get_modified_text(self):
        """Get the modified text after applying diff."""
        return self.diff_viewer.get_modified_text()


# Integration methods to add to TextEditor class:

def _create_diff_menu(self):
    """Create diff menu in the menubar."""
    diff_menu = self.menuBar().addMenu("Diff")
    
    # Compare with file action
    compare_file_action = QAction("Compare with File...", self)
    compare_file_action.setShortcut("Ctrl+D")
    compare_file_action.triggered.connect(self._compare_with_file)
    diff_menu.addAction(compare_file_action)
    
    # Compare with clipboard action
    compare_clipboard_action = QAction("Compare with Clipboard", self)
    compare_clipboard_action.setShortcut("Ctrl+Shift+D")
    compare_clipboard_action.triggered.connect(self._compare_with_clipboard)
    diff_menu.addAction(compare_clipboard_action)
    
    diff_menu.addSeparator()
    
    # Show diff history action
    diff_history_action = QAction("Diff History", self)
    diff_history_action.triggered.connect(self._show_diff_history)
    diff_menu.addAction(diff_history_action)


def _compare_with_file(self):
    """Compare current text with another file."""
    # Get current text
    current_text = self.editor.toPlainText()
    
    if not current_text:
        QMessageBox.warning(self, "No Content", "Current editor is empty.")
        return
    
    # Select file to compare
    path, _ = QFileDialog.getOpenFileName(
        self, "Select File to Compare", "", "Text Files (*.txt);;All Files (*)"
    )
    
    if not path:
        return
    
    try:
        # Read the file
        with open(path, 'r', encoding='utf-8') as f:
            other_text = f.read()
        
        # Create and show diff dialog
        dialog = DiffDialog(self)
        
        current_name = self.current_file if self.current_file else "current"
        dialog.load_diff(current_text, other_text, current_name, path)
        
        # If user applies the diff, update the editor
        if dialog.exec() == QDialog.Accepted:
            modified_text = dialog.get_modified_text()
            if modified_text:
                self.editor.setPlainText(modified_text)
                self.statusBar().showMessage("Diff applied successfully", 3000)
    
    except Exception as e:
        QMessageBox.critical(self, "Error", f"Failed to compare files: {e}")


def _compare_with_clipboard(self):
    """Compare current text with clipboard content."""
    from PySide6.QtWidgets import QApplication
    
    # Get current text
    current_text = self.editor.toPlainText()
    
    if not current_text:
        QMessageBox.warning(self, "No Content", "Current editor is empty.")
        return
    
    # Get clipboard text
    clipboard = QApplication.clipboard()
    clipboard_text = clipboard.text()
    
    if not clipboard_text:
        QMessageBox.warning(self, "Empty Clipboard", "Clipboard is empty.")
        return
    
    # Create and show diff dialog
    dialog = DiffDialog(self)
    
    current_name = self.current_file if self.current_file else "current"
    dialog.load_diff(current_text, clipboard_text, current_name, "clipboard")
    
    # If user applies the diff, update the editor
    if dialog.exec() == QDialog.Accepted:
        modified_text = dialog.get_modified_text()
        if modified_text:
            self.editor.setPlainText(modified_text)
            self.statusBar().showMessage("Diff applied successfully", 3000)


def _show_diff_history(self):
    """Show diff history dialog."""
    # This would show a history of diffs applied
    # For now, just show a placeholder message
    QMessageBox.information(
        self, "Diff History",
        "Diff history feature coming soon!\n\n"
        "This will show a list of all diffs that have been applied,\n"
        "allowing you to review and revert changes."
    )


# To integrate into text_editor.py:
# 1. Add these methods to the TextEditor class
# 2. Call _create_diff_menu() in the __init__ method after creating other menus
# 3. Import the necessary classes at the top of text_editor.py:
#    from editing.diff_viewer import DiffViewerWidget
#    from PySide6.QtWidgets import QDialog
