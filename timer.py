from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AttachedTimerWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Timer window")
        self.setGeometry(parent.x() + parent.width(), parent.y(), 300, 400)  # Attach next to parent window
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.5)

        # Layout for the attached window
        layout = QVBoxLayout(self)

        # Example content
        self.label = QLabel("This is the attached window", self)
        self.label.setStyleSheet("color: white; font-size: 20px;")

        layout.addWidget(self.label)
        self.setLayout(layout)
