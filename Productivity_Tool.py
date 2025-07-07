import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtWidgets import * 

from clock import DigitalClock
from timer import AttachedTimerWindow

class TransparentBackground(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(parent.rect())
        #self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(0, 0, 0, 85)))  # (R, G, B, 0-255)
        painter.setPen(Qt.transparent) 
        painter.drawRect(self.rect())
        painter.end()

class BorderlessWindow(QWidget):
    def __init__(self):
        super().__init__()

        """ Program Window Setting"""
        self.setWindowTitle("Borderless_Window")
        self.setGeometry(1700, 200, 460, 800)  # (Left_space, Up_space, Win_wid, Win_len) 
        self.setWindowFlags(Qt.FramelessWindowHint| Qt.WindowStaysOnTopHint| Qt.Tool)#| Qt.WindowTransparentForInput) 
        self.setAttribute(Qt.WA_TranslucentBackground) 
        self.setWindowOpacity(0.4)
        self._drag_position = QPoint()

        #self.setAttribute(Qt.WA_TransparentForMouseEvents)
        
        self.background = TransparentBackground(self)
        self.background.lower() 

        # self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.header = QWidget(self)
        self.header.setGeometry(0, 0, self.width(), 100)
        self.header.setStyleSheet("background-color: transparent;")

        """ Clock """
        self.clock = DigitalClock(self)
        self.clock.setStyleSheet("background-color: transparent; color: White;")

        """ Timer """
        self.timer_button = QPushButton("Timer", self)
        self.timer_button.clicked.connect(self.open_timer_window) 
        self.timer_button.setStyleSheet(" background-color: transparent; color: white; font-size: 20px;")

        """ Exit Button """
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        self.exit_button.setStyleSheet("background-color: transparent; color: white; font-size: 20px;") 
        
        # self.exit_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)

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

        self.timer_window = None # Need to initialize timer or else error
        
    """ Allows dragging of Window """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.position().y() < 100:
            self._drag_position = event.globalPosition().toPoint()
        else:
            event.ignore()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if event.position().y() < 100:
                delta = event.globalPosition().toPoint() - self._drag_position
                self.move(self.pos() + delta)
                self._drag_position = event.globalPosition().toPoint()
        else:
            event.ignore()

    def open_timer_window(self):  # Open Timer Window
        if self.timer_window is None:  # Check if window is already open
            print("Timer button clicked!")
            self.timer_window = AttachedTimerWindow(self)  # Create an instance of AttachedTimerWindow

            # Set the geometry of the timer window so it’s visible (ensure it's not off-screen)
            self.timer_window.move(self.x() + self.width(), self.y())  # Place it to the right of the parent window
            self.timer_window.resize(300, 400)  # Set the size of the timer window

            self.timer_window.show()  # Show the attached timer window
        else:
            print("Timer window is already open.")  # Prevent reopening if it's already opened


def main():
    app = QApplication(sys.argv)
    window = BorderlessWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__": 
    main() 