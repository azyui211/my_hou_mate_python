'''
    PySide2
        QtWidgets : 위젯 UI 관련된 부분
        QtCore : Qt 고유의 속성, 동작과 관련된 부분
        QtGui : Font, 마우스 커서, 글자 크기 등 GUI 요소에 대한 부분
        QtUiTools : Designer로 만든 .ui 파일과 관련된 부분
'''
import os
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtUiTools import loadUiType

# current_dir_path = os.path.dirname(os.path.abspath(__file__))
# ui_file_path = os.path.join(current_dir_path, "test.ui")        # .ui 파일 연결

ui_file_path = "ui파일 경로"

form_class = loadUiType(ui_file_path)[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showText)          # 버튼 누르면 showText 함수로 연결
        
    def showText(self):
        self.lineEdit.setText("Test Text!!")                    # LineEdit에 글자 표시

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass()        # 인스턴스 생성
    myWindow.show()
    sys.exit(app.exec_())
