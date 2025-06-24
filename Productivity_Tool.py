import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

from clock import DigitalClock

class BorderlessWindow(QWidget):
    def __init__(self):
        super().__init__()

        """ Program Window Setting"""
        self.setWindowTitle("Borderless_Window")
        self.setGeometry(1700, 200, 600, 800)  # (initial location Left_space, initial location Up_space, Window_length, Window_Height) 
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground) 
        self.setWindowOpacity(0.4)  
        self._drag_position = QPoint()

        """ Clock """
        self.clock = DigitalClock(self)
        self.clock.setStyleSheet("background-color: transparent; color: White")


        """ Exit Button """
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setStyleSheet("background-color: transparent; color: white; font-size: 20px;") 
        self.exit_button.clicked.connect(self.close) 

        # Exit Button and Clock layout
        clock_layout = QVBoxLayout()
        clock_layout.addWidget(self.clock, alignment=Qt.AlignCenter)  
  
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.exit_button, alignment=Qt.AlignRight | Qt.AlignBottom)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(clock_layout) 
        main_layout.addStretch(1) 
        main_layout.addLayout(button_layout)  

        self.setLayout(main_layout)


    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(QBrush( QColor(0, 0, 0, 85)))  # (R, G, B, 0-255)
        painter.setPen(Qt.transparent) 

        painter.drawRect(self.rect())  # This fills the whole window area
        painter.end()

    """ Allows dragging of Window """
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

    window = BorderlessWindow()
    window.show()


    sys.exit(app.exec())

if __name__ == "__main__": 
    main() 