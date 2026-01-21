from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton, QGroupBox
)
from PySide6.QtCore import Qt


class LLMSettingsDialog(QDialog):
    """
    A dialog to configure LLM sampling parameters (temperature and top-p).
    """
    
    def __init__(self, temperature=0.9, top_p=0.9, parent=None):
        super().__init__(parent)
        self.setWindowTitle("LLM Parameter Settings")
        self.setFixedWidth(350)
        
        self.temp_value = temperature
        self.top_p_value = top_p
        
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Temperature Group
        temp_group = QGroupBox("Temperature")
        temp_layout = QVBoxLayout()
        
        self.temp_label = QLabel(f"Value: {self.temp_value:.1f}")
        self.temp_slider = QSlider(Qt.Horizontal)
        self.temp_slider.setMinimum(0)
        self.temp_slider.setMaximum(10)
        self.temp_slider.setValue(int(self.temp_value * 10))
        self.temp_slider.setTickPosition(QSlider.TicksBelow)
        self.temp_slider.setTickInterval(1)
        self.temp_slider.valueChanged.connect(self._on_temp_changed)
        
        temp_layout.addWidget(self.temp_label)
        temp_layout.addWidget(self.temp_slider)
        temp_group.setLayout(temp_layout)
        layout.addWidget(temp_group)
        
        # Top-P Group
        top_p_group = QGroupBox("Top-P")
        top_p_layout = QVBoxLayout()
        
        self.top_p_label = QLabel(f"Value: {self.top_p_value:.1f}")
        self.top_p_slider = QSlider(Qt.Horizontal)
        self.top_p_slider.setMinimum(0)
        self.top_p_slider.setMaximum(10)
        self.top_p_slider.setValue(int(self.top_p_value * 10))
        self.top_p_slider.setTickPosition(QSlider.TicksBelow)
        self.top_p_slider.setTickInterval(1)
        self.top_p_slider.valueChanged.connect(self._on_top_p_changed)
        
        top_p_layout.addWidget(self.top_p_label)
        top_p_layout.addWidget(self.top_p_slider)
        top_p_group.setLayout(top_p_layout)
        layout.addWidget(top_p_group)
        
        layout.addSpacing(20)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("Apply")
        self.cancel_button = QPushButton("Cancel")
        
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addStretch()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        # Style
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #555;
                margin-top: 10px;
                padding-top: 10px;
                color: #ddd;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }
            QLabel {
                color: #bbb;
            }
            QPushButton {
                padding: 6px 15px;
            }
        """)

    def _on_temp_changed(self, value):
        self.temp_value = value / 10.0
        self.temp_label.setText(f"Value: {self.temp_value:.1f}")

    def _on_top_p_changed(self, value):
        self.top_p_value = value / 10.0
        self.top_p_label.setText(f"Value: {self.top_p_value:.1f}")

    def get_values(self):
        """Returns (temperature, top_p)"""
        return self.temp_value, self.top_p_value
