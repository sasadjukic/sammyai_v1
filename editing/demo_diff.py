"""
Example script demonstrating the diff-based editing functionality.

This script shows how to use the DiffManager and DiffViewerWidget
to generate, view, and apply diffs.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QHBoxLayout
from diff_manager import DiffManager, DiffFormat
from diff_viewer import DiffViewerWidget


class DiffDemo(QMainWindow):
    """Demo application for diff-based editing."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diff-Based Editing Demo")
        self.setGeometry(100, 100, 1000, 700)
        
        # Create central widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        # Create input areas
        input_layout = QHBoxLayout()
        
        # Original text
        original_container = QVBoxLayout()
        original_container.addWidget(QPushButton("Original Text"))
        self.original_edit = QTextEdit()
        self.original_edit.setPlainText("""def hello_world():
    print("Hello, World!")
    return True

def goodbye():
    print("Goodbye!")
""")
        original_container.addWidget(self.original_edit)
        input_layout.addLayout(original_container)
        
        # Modified text
        modified_container = QVBoxLayout()
        modified_container.addWidget(QPushButton("Modified Text"))
        self.modified_edit = QTextEdit()
        self.modified_edit.setPlainText("""def hello_world(name="World"):
    print(f"Hello, {name}!")
    return True

def goodbye(name="Friend"):
    print(f"Goodbye, {name}!")
    return False

def new_function():
    print("This is new!")
""")
        modified_container.addWidget(self.modified_edit)
        input_layout.addLayout(modified_container)
        
        layout.addLayout(input_layout)
        
        # Generate diff button
        generate_btn = QPushButton("Generate Diff")
        generate_btn.clicked.connect(self.generate_diff)
        layout.addWidget(generate_btn)
        
        # Diff viewer
        self.diff_viewer = DiffViewerWidget()
        self.diff_viewer.diff_applied.connect(self.on_diff_applied)
        layout.addWidget(self.diff_viewer)
    
    def generate_diff(self):
        """Generate and display diff."""
        original = self.original_edit.toPlainText()
        modified = self.modified_edit.toPlainText()
        
        self.diff_viewer.load_diff(
            original, modified,
            "original.py", "modified.py"
        )
    
    def on_diff_applied(self):
        """Handle diff application."""
        result = self.diff_viewer.get_modified_text()
        if result:
            self.original_edit.setPlainText(result)
            print("Diff applied successfully!")


def demo_command_line():
    """Demonstrate diff functionality from command line."""
    print("=" * 60)
    print("Diff-Based Editing Demo (Command Line)")
    print("=" * 60)
    
    manager = DiffManager()
    
    # Example texts
    original = """Line 1
Line 2
Line 3
Line 4
Line 5
"""
    
    modified = """Line 1
Line 2 modified
Line 3
New Line 3.5
Line 4
Line 5
"""
    
    print("\n1. Generating unified diff...")
    diff = manager.generate_diff(
        original, modified,
        "original.txt", "modified.txt",
        format=DiffFormat.UNIFIED
    )
    
    print("\nGenerated Diff:")
    print("-" * 60)
    print(diff)
    print("-" * 60)
    
    print("\n2. Getting diff statistics...")
    stats = manager.get_diff_stats(diff)
    print(f"Additions: {stats['additions']}")
    print(f"Deletions: {stats['deletions']}")
    print(f"Hunks: {stats['hunks']}")
    print(f"Total changes: {stats['changes']}")
    
    print("\n3. Applying diff to original text...")
    result = manager.apply_diff(original, diff)
    
    print("\nResult after applying diff:")
    print("-" * 60)
    print(result)
    print("-" * 60)
    
    print("\n4. Verifying result matches modified text...")
    if result == modified:
        print("✓ SUCCESS: Result matches modified text!")
    else:
        print("✗ FAILURE: Result does not match!")
    
    print("\n5. Testing history (undo/redo)...")
    manager.add_to_history(original, modified)
    manager.add_to_history(modified, result)
    
    print(f"Can undo: {manager.can_undo()}")
    print(f"Can redo: {manager.can_redo()}")
    
    if manager.can_undo():
        undone = manager.undo()
        print(f"After undo, text is: {undone[:20]}...")
    
    print("\n" + "=" * 60)
    print("Demo completed!")
    print("=" * 60)


if __name__ == "__main__":
    # Run command line demo
    demo_command_line()
    
    print("\n\nLaunching GUI demo...")
    print("(Close the window to exit)")
    
    # Run GUI demo
    app = QApplication(sys.argv)
    demo = DiffDemo()
    demo.show()
    sys.exit(app.exec())
