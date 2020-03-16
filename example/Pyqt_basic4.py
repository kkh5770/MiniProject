import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic


#form_class=uic.loadUiType('D:/section6/example/basictest_1.ui')[0]

class TestForm(QMainWindow,Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__() #부모의 생성자 함수 호출
        self.setupUi(self) # 함수 선언



if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
