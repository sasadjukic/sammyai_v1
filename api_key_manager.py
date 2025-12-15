"""
API Key Manager for LLM integration.
Handles secure storage and retrieval of API keys using QSettings.
"""

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class APIKeyManager:
    """Manages API key storage and retrieval using QSettings."""
    
    ORGANIZATION = "SammyAI"
    APPLICATION = "TextEditor"
    
    @staticmethod
    def save_api_key(api_key: str) -> None:
        """
        Save the API key to persistent storage.
        
        Args:
            api_key: The API key to save
        """
        settings = QSettings(APIKeyManager.ORGANIZATION, APIKeyManager.APPLICATION)
        settings.setValue("llm/api_key", api_key)
    
    @staticmethod
    def load_api_key() -> str:
        """
        Load the API key from persistent storage.
        
        Returns:
            The stored API key, or empty string if not set
        """
        settings = QSettings(APIKeyManager.ORGANIZATION, APIKeyManager.APPLICATION)
        return settings.value("llm/api_key", "")
    
    @staticmethod
    def clear_api_key() -> None:
        """Clear the stored API key."""
        settings = QSettings(APIKeyManager.ORGANIZATION, APIKeyManager.APPLICATION)
        settings.remove("llm/api_key")
    
    @staticmethod
    def has_api_key() -> bool:
        """
        Check if an API key is currently stored.
        
        Returns:
            True if an API key exists, False otherwise
        """
        return bool(APIKeyManager.load_api_key())


class APIKeyDialog(QDialog):
    """Dialog for entering and managing API keys."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("API Key Configuration")
        self.setModal(True)
        self.setMinimumWidth(500)
        self.setup_ui()
        self.load_existing_key()
    
    def setup_ui(self):
        """Set up the dialog UI."""
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Title and description
        title_label = QLabel("Cloud Model API Key")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title_label)
        
        description = QLabel(
            "Enter your API key for cloud-based LLM models (e.g., Kimi K2:1T).\n"
            "This key will be stored securely on your local machine.\n"
            "Leave empty if you only use local models."
        )
        description.setWordWrap(True)
        description.setStyleSheet("color: #888888;")
        layout.addWidget(description)
        
        # API Key input
        key_layout = QHBoxLayout()
        key_label = QLabel("API Key:")
        key_label.setMinimumWidth(80)
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter your API key here...")
        self.key_input.setEchoMode(QLineEdit.Password)
        
        # Toggle visibility button
        self.toggle_visibility_btn = QPushButton("👁")
        self.toggle_visibility_btn.setMaximumWidth(40)
        self.toggle_visibility_btn.setToolTip("Show/Hide API key")
        self.toggle_visibility_btn.clicked.connect(self._toggle_key_visibility)
        
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        key_layout.addWidget(self.toggle_visibility_btn)
        layout.addLayout(key_layout)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: #4CAF50; font-style: italic;")
        layout.addWidget(self.status_label)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setToolTip("Remove stored API key")
        self.clear_btn.clicked.connect(self._clear_key)
        
        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.reject)
        
        self.save_btn = QPushButton("Save")
        self.save_btn.setDefault(True)
        self.save_btn.clicked.connect(self._save_key)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addWidget(self.cancel_btn)
        button_layout.addWidget(self.save_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def load_existing_key(self):
        """Load and display existing API key if available."""
        existing_key = APIKeyManager.load_api_key()
        if existing_key:
            self.key_input.setText(existing_key)
            self.status_label.setText("✓ API key is currently configured")
            self.status_label.setStyleSheet("color: #4CAF50; font-style: italic;")
        else:
            self.status_label.setText("⚠ No API key configured")
            self.status_label.setStyleSheet("color: #FFA500; font-style: italic;")
    
    def _toggle_key_visibility(self):
        """Toggle between showing and hiding the API key."""
        if self.key_input.echoMode() == QLineEdit.Password:
            self.key_input.setEchoMode(QLineEdit.Normal)
            self.toggle_visibility_btn.setText("🔒")
        else:
            self.key_input.setEchoMode(QLineEdit.Password)
            self.toggle_visibility_btn.setText("👁")
    
    def _save_key(self):
        """Save the API key and close the dialog."""
        api_key = self.key_input.text().strip()
        
        if api_key:
            APIKeyManager.save_api_key(api_key)
            QMessageBox.information(
                self,
                "Success",
                "API key has been saved successfully!"
            )
            self.accept()
        else:
            # Allow saving empty key (clears it)
            APIKeyManager.clear_api_key()
            QMessageBox.information(
                self,
                "Cleared",
                "API key has been cleared."
            )
            self.accept()
    
    def _clear_key(self):
        """Clear the API key after confirmation."""
        reply = QMessageBox.question(
            self,
            "Confirm Clear",
            "Are you sure you want to clear the stored API key?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            APIKeyManager.clear_api_key()
            self.key_input.clear()
            self.status_label.setText("⚠ No API key configured")
            self.status_label.setStyleSheet("color: #FFA500; font-style: italic;")
            QMessageBox.information(
                self,
                "Cleared",
                "API key has been cleared successfully."
            )
