import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtWidgets import QApplication, QWidget

class BorderlessWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Control Window
        self.setWindowTitle("Borderless_Window")
        self.setGeometry(10, 100, 600, 800)  # (initial location Left_space, initial location Up_space, Window_length, Window_Height) 
        self.setWindowFlags(Qt.FramelessWindowHint)  # No borders
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make window background transparent
        self.setWindowOpacity(0.9)  # Set window opacity
        
        # Store position for dragging
        self._drag_position = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Create a semi-transparent black color (alpha 0.5 means 50% transparent)
        semi_transparent_black = QColor(0, 0, 0, 208)  # (R, G, B, 0-255)
        
        # Set the brush and pen for painting
        painter.setBrush(QBrush(semi_transparent_black))
        painter.setPen(Qt.transparent)  # Remove border around the surface
        
        # Fill the entire window with semi-transparent black color
        painter.drawRect(self.rect())  # This fills the whole window area

        painter.end()

    """ Allows dragging of Window"""
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = event.globalPosition().toPoint() - self._drag_position
            self.move(self.pos() + delta)
            self._drag_position = event.globalPosition().toPoint()


def main():
    app = QApplication(sys.argv)
    # Create and display the window
    window = BorderlessWindow()
    window.show()
    # Run the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__": 
    main() #Called to run the application