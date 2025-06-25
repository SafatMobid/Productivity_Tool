import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtWidgets import * 

from clock import DigitalClock

class BorderlessWindow(QWidget):
    def __init__(self):
        super().__init__()

        """ Program Window Setting"""
        self.setWindowTitle("Borderless_Window")
        self.setGeometry(1700, 200, 460, 800)  # (initial location Left_space, initial location Up_space, Window_length, Window_Height) 
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground) 
        self.setWindowOpacity(0.4)
        
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowTitle("Always on Top Window") 
        self._drag_position = QPoint()

        #Doesnt work, may be some use
        # self.setAttribute(Qt.WA_TransparentForMouseEvents)
        # self.setWindowFlag(Qt.FramelessWindowHint, True)

        #Works but if window is click through it none draggable or exitable(Exploring options)
        # self.setWindowFlags(Qt.FramelessWindowHint |Qt.WindowStaysOnTopHint |Qt.WindowTransparentForInput)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush( QColor(0, 0, 0, 85)))  # (R, G, B, 0-255)
        painter.setPen(Qt.transparent) 
        painter.drawRect(self.rect())
        painter.end()

        """ Clock Style"""
        self.clock = DigitalClock(self)
        self.clock.setStyleSheet("background-color: transparent; color: White;")

        # opacity_effect = QGraphicsOpacityEffect(self.clock)
        # opacity_effect.setOpacity(1)
        # self.clock.setGraphicsEffect(opacity_effect)

        """ Exit Button """
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setStyleSheet("background-color: transparent; color: white; font-size: 20px;") 
        self.exit_button.clicked.connect(self.close) 

        """ Exit Button and Clock layout """
        clock_layout = QVBoxLayout()
        clock_layout.addWidget(self.clock, alignment=Qt.AlignCenter)  
  
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.exit_button, alignment=Qt.AlignRight | Qt.AlignBottom)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(clock_layout) 
        main_layout.addStretch(1) 
        main_layout.addLayout(button_layout)  

        self.setLayout(main_layout)

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