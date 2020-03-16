import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import uic
from lib.you_viewer_layout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
from PyQt5 import QtWebEngineWidgets
import re
import datetime


#from_class=uic.loadUiType('D:/section6/ui/pro.ui')[0]
class TestForm(QMainWindow, Ui_MainWindow): #PyQt5.QtWidgets에서 상속됨
    #생성자
    def __init__(self):
        super().__init__() #부모의 생성자 호출
        #초기화
        self.setupUi(self) # 함수 선언
        #인증버튼 이벤트 전
        self.initAuthLock()
        #인증버튼 이벤트 후
        self.initAuthActive()
        #시그널 초기화
        self.initSignal()
        #로그인 관련 변수 선언
        self.user_id=None
        self.user_pw=None


    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
    @pyqtSlot() #명시적 표현
    def authCheck(self):
        pass    



if __name__ == "__main__":     # 클래스 전체 호출
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
