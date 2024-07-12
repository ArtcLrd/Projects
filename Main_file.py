
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import urllib.request
import firebase_admin
from firebase_admin import credentials
import numpy as np
import imutils
from PyQt5.QtGui import QImage , QPixmap
import sys
import Main_class
from PyQt5.QtCore import QThread , pyqtSignal
import datetime
import time
import working
import text_extraction
import firebase_check
from firebase_admin import firestore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_back = QtWidgets.QFrame(self.centralwidget)
        self.main_back.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.main_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_back.setObjectName("main_back")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_back)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.app_bar = QtWidgets.QFrame(self.main_back)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_bar.sizePolicy().hasHeightForWidth())
        self.app_bar.setSizePolicy(sizePolicy)
        self.app_bar.setMinimumSize(QtCore.QSize(100, 100))
        self.app_bar.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"border: 1px solid black;\n"
"border-radius:10px;\n"
"")
        self.app_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_bar.setObjectName("app_bar")
        self.gridLayout = QtWidgets.QGridLayout(self.app_bar)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.app_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(450, 50))
        self.frame_3.setStyleSheet(u"background-color: rgb(173, 173, 173);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_title = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_title.setStyleSheet(u"border:0px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout_3.addWidget(self.lbl_title)
        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(245, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.icon_frame = QtWidgets.QFrame(self.app_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_frame.sizePolicy().hasHeightForWidth())
        self.icon_frame.setSizePolicy(sizePolicy)
        self.icon_frame.setMinimumSize(QtCore.QSize(100, 100))
        self.icon_frame.setStyleSheet(u"background-color: rgb(173, 173, 173);\n"
"border:0px;\n"
"border-radius:10px;\n"
"")
        self.icon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.icon_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.icon_frame.setObjectName("icon_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.icon_frame)
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_web = QtWidgets.QPushButton(self.icon_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_web.sizePolicy().hasHeightForWidth())
        self.btn_web.setSizePolicy(sizePolicy)
        self.btn_web.setMinimumSize(QtCore.QSize(90, 90))
        self.btn_web.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/OM/Downloads/logobg1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_web.setIcon(icon)
        self.btn_web.setIconSize(QtCore.QSize(90, 100))
        self.btn_web.setObjectName("btn_web")
        self.btn_web.clicked.connect(self.clear)
        self.verticalLayout_7.addWidget(self.btn_web)
        self.gridLayout.addWidget(self.icon_frame, 0, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.app_bar)
        self.frame_8.setEnabled(False)
        self.frame_8.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_8.setStyleSheet("border:0px;\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout.addWidget(self.frame_8, 0, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.app_bar)
        self.frame_body = QtWidgets.QFrame(self.main_back)
        self.frame_body.setEnabled(True)
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_body)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_body)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMaximumSize(500,500)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_img = QtWidgets.QLabel(self.frame_2)
        self.lbl_img.setStyleSheet(u"background-color: rgb(173, 173, 173);\n"
"border-radius:10px;\n"
"")
        self.lbl_img.setText("")
        self.lbl_img.setObjectName("lbl_img")
        self.verticalLayout_4.addWidget(self.lbl_img)
        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_body)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_body)
        self.frame_6.setStyleSheet(u"background-color: rgb(173, 173, 173);\n"
"border-radius:5px;\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setContentsMargins(28, 28, 28, 28)
        self.gridLayout_3.setSpacing(28)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_cardetected = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cardetected.sizePolicy().hasHeightForWidth())
        self.lbl_cardetected.setSizePolicy(sizePolicy)
        self.lbl_cardetected.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        font.setBold(True)
        self.lbl_cardetected.setFont(font)
        self.lbl_cardetected.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")
        self.lbl_cardetected.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_cardetected.setObjectName("lbl_cardetected")
        self.gridLayout_3.addWidget(self.lbl_cardetected, 0, 0, 1, 1)
        self.lbl_nodetect = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_nodetect.sizePolicy().hasHeightForWidth())
        self.lbl_nodetect.setSizePolicy(sizePolicy)
        self.lbl_nodetect.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nodetect.setFont(font)
        self.lbl_nodetect.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"")
        self.lbl_nodetect.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nodetect.setObjectName("lbl_nodetect")
        self.gridLayout_3.addWidget(self.lbl_nodetect, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_body)
        self.frame_5.setStyleSheet(u"background-color: rgb(173, 173, 173);\n"
"border:1px;\n"
"border-radius:5px;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_stream = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stream.sizePolicy().hasHeightForWidth())
        self.btn_stream.setSizePolicy(sizePolicy)
        self.btn_stream.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_stream.setFont(font)
        self.btn_stream.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stream.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")
        self.btn_stream.setCheckable(True)
        self.btn_stream.setObjectName("btn_stream")
        self.btn_stream.clicked.connect(self.deploy_stream)
        self.verticalLayout_5.addWidget(self.btn_stream)
        self.btn_start = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"")
        self.btn_start.setCheckable(True)
        self.btn_start.setChecked(False)
        self.btn_start.setObjectName("btn_start")
        self.btn_start.toggled.connect(self.deploy_prediction)
        self.verticalLayout_5.addWidget(self.btn_start)
        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_body)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2.addWidget(self.frame_4, 0, 2, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_body)
        self.frame_7.setStyleSheet(u"background-color: rgb(173, 173, 173);\n"
"border-radius:5px;\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_6.addWidget(self.textBrowser)
        self.gridLayout_2.addWidget(self.frame_7, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_body)
        self.verticalLayout.addWidget(self.main_back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        """self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)"""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "Py-Application"))
        self.lbl_cardetected.setText(_translate("MainWindow", "CAR DETECTED"))
        self.lbl_nodetect.setText(_translate("MainWindow", "NO DETECTIONS"))
        self.btn_stream.setText(_translate("MainWindow", "STREAM"))
        self.btn_stream.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.btn_start.setText(_translate("MainWindow", "Start Process"))
        self.btn_start.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Car Number..."))
    #clear  text in the textbox when button is clicked and reset label colors
    def clear(self):
      
        print("Worker 3 started...")
        self.textBrowser.setText("")
        self.lbl_cardetected.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")
        self.lbl_nodetect.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")
        #Start streaming
    def deploy_stream(self):
        if self.btn_stream.isChecked():
           self.btn_stream.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n") 
           self.worker1= WorkerThread2(parent=None)
           self.worker1.imgUpdate.connect(self.imgupdateslot)
           self.worker1.car_str.connect(self.detection)
           self.worker1.start()
           #self.worker1.start()
           print("Streaming started...")
        elif not self.btn_stream.isChecked():
            time.sleep(0.1)
            self.worker1.imgUpdate.disconnect(self.imgupdateslot)
            self.worker1.stop()
            self.lbl_img.setText(" ")
            self.btn_stream.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n") 
            self.lbl_img.setStyleSheet("background-color: rgb(173,173,173);\n"
"border-radius:10px;\n"
"")
            self.lbl_cardetected.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")
            self.lbl_nodetect.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")         
            self.textBrowser.setText("")
            self.textBrowser.append("\nStreaming Stopped...")
            self.lbl_img.setStyleSheet("background-color: rgb(173,173,173);\n"
"border-radius:10px;\n"
"")

    #Deploy prediction...
    def deploy_prediction(self):
        if self.btn_start.isChecked():
            self.lbl_title.setText("Prediction in Progress...")
            self.worker = WorkerThread(parent=None)
            self.worker.start()
            self.btn_start.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n")
            
        else:
            self.lbl_title.setText("Py-Application") 
            self.worker.terminate()
            print(working.DETECT_WINDOW.str_ret(working.DETECT_WINDOW))
            self.textBrowser.setText("")
            self.btn_start.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n")
            self.lbl_cardetected.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")
            self.lbl_nodetect.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"")
            print("Worker Stopped...")

#Worker Thread2....
            
    
    def imgupdateslot(self, Image):
        self.lbl_img.setPixmap(QPixmap.fromImage(Image))


#checking...
    def detection(self,car_str):
        db = firestore.client()
        str = firebase_check.Db_update.get_document(firebase_check.Db_update,'Car_test', 'eADQjHTyfmzTkkRIIduT', db)[0]
        try:
            if "NULL" in car_str:
                self.lbl_cardetected.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:20px;\n"
    "\n"
    "")
                self.lbl_nodetect.setStyleSheet(u"background-color: rgb(136, 181, 127);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:20px;\n"
    "") 
                self.textBrowser.setText("Number: "+"\t...")
            elif car_str == str:
                self.lbl_cardetected.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:20px;\n"
    "\n"
    "")
                self.lbl_nodetect.setStyleSheet(u"background-color: rgb(136, 181, 127);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:20px;\n"
    "") 
                self.textBrowser.setText("Number: "+"\tAlready registered..")
            else:
                    self.lbl_cardetected.setStyleSheet(u"background-color: rgb(136, 181, 127);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:20px;\n"
    "")
                    self.lbl_nodetect.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:20px;\n"
    "\n"
    "")
                    #num_str = text_extraction.image_mod.ret_str(text_extraction.image_mod)
                    self.textBrowser.setText("")
                    self.textBrowser.setText("\n\nNumber: \t"+car_str)
                    #Worker #3 called...
                    worker3 = WorkerThread3(parent = None, in_str=car_str)
                    worker3.out_str.connect(self.firebase_change)
                    worker3.start()
                    time.sleep(1)
                    worker3.terminate()
        except Exception as exp:
            print(exp)

    def firebase_change(self,out_str):
        if out_str == "true":
            self.textBrowser.append("\n\tRegistered...")
        elif out_str == "false":
            self.textBrowser.append("\n\tMatched..")
        else:
            self.textBrowser.append("\n\tError Occured!")


#Prediction Class...            

class WorkerThread(QThread):
    result=""
    def __init__(self, parent: None, index = 1 ):
        super().__init__(parent)
        self.index = index
    def run(self):   
        m= Main_class.Main('http://192.168.29.47/cam-hi.jpg')
        result = m.string_ret()
        print("Worker finish..."+result)


#Stream thread...

class WorkerThread2(QThread):
    imgUpdate = pyqtSignal(QImage)
    car_str = pyqtSignal(str)
    def __init__(self, parent: None, index = 2 ):
        super().__init__(parent)
        self.index = index
    def run(self):
        self.ThreadActive = True
        url = 'http://192.168.29.47/cam-hi.jpg'
        while self.ThreadActive:
            img_resp = urllib.request.urlopen(url)
            imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            im = cv2.imdecode(imgnp, -1)
            im = imutils.resize(im,width=500,height=400)
            frame = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            self.imgUpdate.emit(img)
            str = working.DETECT_WINDOW.str_ret(working.DETECT_WINDOW)
            if "Car" in str:
                num_str = text_extraction.image_mod.ret_str(text_extraction.image_mod)
                #number emitted...
                if "NULL" in num_str:
                    self.car_str.emit("NULL")
                else:
                    self.car_str.emit(num_str)
            elif "NULL" in str:
                self.car_str.emit("NULL")                
            else:
                self.car_str.emit("NULL")
            
    def stop(self):
        self.ThreadActive = False
        self.quit()


#Firebase....

class WorkerThread3(QThread):
    out_str = pyqtSignal(str)
    def __init__(self, parent: None ,in_str):
        self.in_str = in_str
        super().__init__(parent)
    def run(self):
        db = firestore.client()
        #xy = text_extraction.image_mod.ret_str(text_extraction.image_mod)
        if not "NULL" in self.in_str:
            fb_check = firebase_check.Db_update()
            doc = ()
            doc = fb_check.get_document('Car_test','eADQjHTyfmzTkkRIIduT',db)

            if self.in_str == doc[0]:
                print("done")
                self.out_str.emit("false")

            else:
                now = datetime.datetime.now().time()
                fb_check.update_exixting_doc('Car_test','eADQjHTyfmzTkkRIIduT',db,self.in_str,str(now))
                self.out_str.emit("true")
                print("done")
                self.in_str=""




if __name__=="__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     MainWindow = QtWidgets.QMainWindow()
     ui = Ui_MainWindow()
     ui.setupUi(MainWindow)
     MainWindow.show()
     cred = credentials.Certificate("E:/Programs/numberplatetest-a72be-firebase-adminsdk-8lh3t-c11bbc87d1.json")
     firebase_admin.initialize_app(cred,{"databaseURL":"https://numberplatetest-a72be-default-rtdb.firebaseio.com"})
     sys.exit(app.exec_())
