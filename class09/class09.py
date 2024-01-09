#

import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QSizePolicy
from PySide2.QtCore import Qt, QRect
from PySide2.QtGui import QCursor, QFont

class myWindow(QWidget):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        self.resize(580,260)
        self.x_pos = QCursor.pos().x()
        self.y_pos = QCursor.pos().y()
        self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        
        self.buttonA = self.mk_button("Open/Save", 5,10,180,40)
        self.buttonB = self.mk_button("Nuke Panels", 200,10,180,40)
        self.buttonC = self.mk_button("Load/Upload", 395,10,180,40)
        self.leaveEvent = self.MainLeaveEvent
        self.move(self.x_pos, self.y_pos)
        self.show()
    
    def mk_button(self, text, x, y, wd, ht):
        button = QPushButton(self)
        button.setFont(QFont("Dejavu Sans", 13, QFont.Bold))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(text)
        button.setGeometry(QRect(x, y, wd, ht))
        button.setStyleSheet("QPushButton{color:#ABABAB; background-color:#565656; border-radius:10px} QPushButton:hover{color:#DEDEDE; background-color:#16B2EC; border-radius:10px}")
        
        
        return button
    
    def MainLeaveEvent(self, event):
        self.close()

app = QApplication(sys.argv)      # 후디니에서 띄울 경우 필요없는 줄 1
widgetUI = myWindow()
sys.exit(app.exec_())             # 후디니에서 띄울 경우 필요없는 줄 2