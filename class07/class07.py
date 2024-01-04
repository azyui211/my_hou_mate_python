'''
    PySide2
        QtWidgets : 위젯 UI 관련된 부분
        QtCore : Qt 고유의 속성, 동작과 관련된 부분
        QtGui : Font, 마우스 커서, 글자 크기 등 GUI 요소에 대한 부분
        QtUiTools : Designer로 만든 .ui 파일과 관련된 부분
'''

import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtUiTools import uic

form_class = uic.loadUiType("UI파일이름.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass()        # 인스턴스 생성
    myWindow.show()
    sys.exit(app.exec_())
