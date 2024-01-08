
'''
# 크기 조절
    QMainWindow, QWidgets - .resize(가로크기, 세로크기)
    나머지 widget - .setGeometry(QtCore.QRect(x좌표, y좌표, 가로크기, 세로크기))

# 버튼 연결
    버튼.clicked.connect(self.함수이름)
    
# Text 읽기, 쓰기
    읽기 - 위젯.text()
    쓰기 - 위젯.setText()

# 기본 꾸미기
    위젯.setStyleSheet("위젯타입이름{스타일시트 내용}")
    
    컬러표현 : 16진수 형태 - #FFA435 또는
             RGB 형태 - rgb(255,134,82)
             RGBA 형태 - rgba(223,150,31,102)

    스타일시트 내용 기본
        color: #FFAA44;                # 글자색
        background-color: #54FD1A;     # 위젯 배경색
        border-radius: 10px;           # 위젯 테두리 각진 정도
'''

import sys
from PySide2 import QtWidgets, QtCore

class myWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)

app = QtWidgets.QApplication(sys.argv)
widgetUI = myWindow()
widgetUI.show()
sys.exit(app.exec_())