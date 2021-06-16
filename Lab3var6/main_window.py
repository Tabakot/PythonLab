import logging
import os

import cv2
from PyQt5 import QtCore, QtWidgets

from find_mouth import FindMouth


class MainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(400, 260)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 80, 200, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 120, 200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label.setMaximumSize(QtCore.QSize(640, 480))
        self.label.setText("")
        self.label.setObjectName("label")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Табачинский Михаил ПРИ-18"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить изображение"))
        self.pushButton_2.setText(_translate("MainWindow", "В реальном времени"))
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton2_handler)

    def pushButton_handler(self):
        logging.info("Button 'Загрузить изображение' pressed")
        self.file_browse()

    def pushButton2_handler(self):
        logging.info("Button 'В реальном времени' pressed")
        self.find_camera()

    @staticmethod
    def file_browse():
        cv2.destroyAllWindows()
        logging.info('csv windows destroyed')
        file_path = QtWidgets.QFileDialog.getOpenFileName()
        extension = os.path.splitext(file_path[0])[1]
        if file_path[0] and extension in ['.jpg', '.png']:
            FindMouth.image_find_mouth(file_path[0])
        else:
            logging.error('Файл не выбран!')

    @staticmethod
    def find_camera():
        cv2.destroyAllWindows()
        logging.info('csv windows destroyed')
        FindMouth.video_find_mouth()