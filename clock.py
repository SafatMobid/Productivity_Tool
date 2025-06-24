from PySide6.QtCore import QTime, QTimer, Slot
from PySide6.QtWidgets import QLCDNumber

"""CLOCK Functionality"""
class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.setDigitCount(8)

        # Timer to update every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.show_time()
        self.setFixedSize(276, 222)


    @Slot()
    def show_time(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm:ss AP")

        self.setDigitCount(11)

        # Blinking colon effect
        if (time.second() % 2) == 0:
            text = text.replace(":", " ")

        self.display(text)
