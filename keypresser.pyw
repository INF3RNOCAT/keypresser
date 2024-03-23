import sys, pyautogui, time
from threading import Thread
from pynput import keyboard
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Keypresser(object):
    def setupUi(self, Keypresser):
        if not Keypresser.objectName():
            Keypresser.setObjectName(u"Keypresser")
        Keypresser.setFixedWidth(451)
        Keypresser.setFixedHeight(256)
        Keypresser.setWindowIcon(QIcon("keyboard.ico"))
        self.gridLayoutWidget = QWidget(Keypresser)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 431, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.seconds = QSpinBox(self.gridLayoutWidget)
        self.seconds.setObjectName(u"seconds")
        self.seconds.setMaximum(99999)

        self.gridLayout.addWidget(self.seconds, 1, 4, 1, 1)

        self.hours = QSpinBox(self.gridLayoutWidget)
        self.hours.setObjectName(u"hours")
        self.hours.setMaximum(99999)

        self.gridLayout.addWidget(self.hours, 1, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.milliseconds = QSpinBox(self.gridLayoutWidget)
        self.milliseconds.setObjectName(u"milliseconds")
        self.milliseconds.setMaximum(99999)

        self.gridLayout.addWidget(self.milliseconds, 1, 6, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 5, 1, 1)

        self.minutes = QSpinBox(self.gridLayoutWidget)
        self.minutes.setObjectName(u"minutes")
        self.minutes.setMaximum(99999)

        self.gridLayout.addWidget(self.minutes, 1, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 7, 1, 1)

        self.line = QFrame(Keypresser)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 70, 431, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_2 = QWidget(Keypresser)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 110, 431, 24))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(Keypresser)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 80, 45, 21))
        self.line_2 = QFrame(Keypresser)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 140, 431, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.start = QPushButton(Keypresser)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(10, 160, 211, 81))
        self.stop = QPushButton(Keypresser)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(230, 160, 211, 81))

        self.running = False
        Thread(target=self.input).start()
        

        self.retranslateUi(Keypresser)

        QMetaObject.connectSlotsByName(Keypresser)
    # setupUi

    def get_time(self):
        times = {
            "hours": self.hours.value() * 3600,
            "minutes": self.minutes.value() * 60,
            "seconds": self.seconds.value(),
            "milliseconds": self.milliseconds.value() * .001,
        }
        total = times["hours"] + times["minutes"] + times["seconds"] + times["milliseconds"]
        return total

    def get_options(self):
        return self.get_time(), self.lineEdit.text().split("=>")

    def thread(self):
        total, keys = self.get_options()

        while True:
            if (not self.running): break
            for key in keys:
                if (not self.running): break
                if (not key in pyautogui.KEYBOARD_KEYS): continue
                pyautogui.keyDown(str(key.lower()))
                if (not total == 0.0): time.sleep(total)
                pyautogui.keyUp(str(key.lower()))

    def begin(self):
        if (self.running): return
        self.running = True
        Thread(target=self.thread).start()

    def end(self):
        if (not self.running): return
        self.running = False

    def pressed(self, key):
        if (key == keyboard.Key.f5):
            self.begin()
        elif (key == keyboard.Key.f6):
            self.end()

    def input(self):
        with keyboard.Listener(on_press=self.pressed) as listener:
            listener.join()
        

    def retranslateUi(self, Keypresser):
        Keypresser.setWindowTitle(QCoreApplication.translate("Keypresser", u"Keypresser", None))
        self.label.setText(QCoreApplication.translate("Keypresser", u"Interval:", None))
        self.label_2.setText(QCoreApplication.translate("Keypresser", u"hours", None))
        self.label_4.setText(QCoreApplication.translate("Keypresser", u"seconds", None))
        self.label_3.setText(QCoreApplication.translate("Keypresser", u"minutes", None))
        self.label_5.setText(QCoreApplication.translate("Keypresser", u"millseconds", None))
        self.label_6.setText(QCoreApplication.translate("Keypresser", u"Key(s):   ", None))
        self.label_7.setText(QCoreApplication.translate("Keypresser", u"Options:", None))
        self.start.setText(QCoreApplication.translate("Keypresser", u"Start [F5]", None))
        self.stop.setText(QCoreApplication.translate("Keypresser", u"Stop [F6]", None))
    # retranslateUi

def main():
    app = QApplication(sys.argv)
    Keypresser = QWidget()
    ui = Ui_Keypresser()
    ui.setupUi(Keypresser)
    Keypresser.show()
    sys.exit(app.exec())

main()
