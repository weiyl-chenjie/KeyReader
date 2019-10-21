# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Wed Oct 16 08:16:37 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1594, 1012)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_show_image = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_show_image.setGeometry(QtCore.QRect(290, 190, 1281, 661))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox_show_image.setFont(font)
        self.groupBox_show_image.setObjectName("groupBox_show_image")
        self.label_show_image = QtWidgets.QLabel(self.groupBox_show_image)
        self.label_show_image.setGeometry(QtCore.QRect(9, 29, 1261, 621))
        self.label_show_image.setObjectName("label_show_image")
        self.groupBox_result = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_result.setGeometry(QtCore.QRect(290, 10, 901, 181))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox_result.setFont(font)
        self.groupBox_result.setObjectName("groupBox_result")
        self.lineEdit_key_id = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_key_id.setGeometry(QtCore.QRect(40, 120, 220, 51))
        self.lineEdit_key_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_key_id.setReadOnly(True)
        self.lineEdit_key_id.setObjectName("lineEdit_key_id")
        self.lineEdit_key_code = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_key_code.setGeometry(QtCore.QRect(290, 20, 580, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit_key_code.setFont(font)
        self.lineEdit_key_code.setText("")
        self.lineEdit_key_code.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_key_code.setReadOnly(True)
        self.lineEdit_key_code.setObjectName("lineEdit_key_code")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 251, 281))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 41, 231, 225))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_plant = QtWidgets.QLabel(self.widget)
        self.label_plant.setObjectName("label_plant")
        self.horizontalLayout_4.addWidget(self.label_plant)
        self.lineEdit_plant = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_plant.setMinimumSize(QtCore.QSize(139, 39))
        self.lineEdit_plant.setMaximumSize(QtCore.QSize(139, 16777215))
        self.lineEdit_plant.setText("")
        self.lineEdit_plant.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_plant.setReadOnly(True)
        self.lineEdit_plant.setObjectName("lineEdit_plant")
        self.horizontalLayout_4.addWidget(self.lineEdit_plant)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_product = QtWidgets.QLabel(self.widget)
        self.label_product.setObjectName("label_product")
        self.horizontalLayout.addWidget(self.label_product)
        self.lineEdit_product = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_product.setMaximumSize(QtCore.QSize(139, 16777215))
        self.lineEdit_product.setText("")
        self.lineEdit_product.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_product.setReadOnly(True)
        self.lineEdit_product.setObjectName("lineEdit_product")
        self.horizontalLayout.addWidget(self.lineEdit_product)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_marble_number = QtWidgets.QLabel(self.widget)
        self.label_marble_number.setObjectName("label_marble_number")
        self.horizontalLayout_2.addWidget(self.label_marble_number)
        self.lineEdit_marble_number = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_marble_number.setText("")
        self.lineEdit_marble_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_marble_number.setReadOnly(True)
        self.lineEdit_marble_number.setObjectName("lineEdit_marble_number")
        self.horizontalLayout_2.addWidget(self.lineEdit_marble_number)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_single_row = QtWidgets.QRadioButton(self.widget)
        self.radioButton_single_row.setCheckable(False)
        self.radioButton_single_row.setObjectName("radioButton_single_row")
        self.horizontalLayout_3.addWidget(self.radioButton_single_row)
        self.radioButton_double_row = QtWidgets.QRadioButton(self.widget)
        self.radioButton_double_row.setCheckable(False)
        self.radioButton_double_row.setObjectName("radioButton_double_row")
        self.horizontalLayout_3.addWidget(self.radioButton_double_row)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_key_sensor = QtWidgets.QLabel(self.widget)
        self.label_key_sensor.setObjectName("label_key_sensor")
        self.horizontalLayout_5.addWidget(self.label_key_sensor)
        self.checkBox_key_sensor = QtWidgets.QCheckBox(self.widget)
        self.checkBox_key_sensor.setObjectName("checkBox_key_sensor")
        self.horizontalLayout_5.addWidget(self.checkBox_key_sensor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.comboBox_change_product = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_change_product.setGeometry(QtCore.QRect(10, 340, 187, 39))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.comboBox_change_product.setFont(font)
        self.comboBox_change_product.setObjectName("comboBox_change_product")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(290, 860, 1281, 101))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_status.setText("")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 390, 189, 225))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_set_calibration_line = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton_set_calibration_line.setFont(font)
        self.pushButton_set_calibration_line.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.pushButton_set_calibration_line.setObjectName("pushButton_set_calibration_line")
        self.verticalLayout.addWidget(self.pushButton_set_calibration_line)
        self.pushButton_self_calibrate = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton_self_calibrate.setFont(font)
        self.pushButton_self_calibrate.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.pushButton_self_calibrate.setObjectName("pushButton_self_calibrate")
        self.verticalLayout.addWidget(self.pushButton_self_calibrate)
        self.pushButton_manual_calibrate = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton_manual_calibrate.setFont(font)
        self.pushButton_manual_calibrate.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.pushButton_manual_calibrate.setObjectName("pushButton_manual_calibrate")
        self.verticalLayout.addWidget(self.pushButton_manual_calibrate)
        self.pushButton_check_image = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton_check_image.setFont(font)
        self.pushButton_check_image.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.pushButton_check_image.setObjectName("pushButton_check_image")
        self.verticalLayout.addWidget(self.pushButton_check_image)
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1594, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_start, QtCore.SIGNAL("clicked()"), MainWindow.start)
        QtCore.QObject.connect(self.pushButton_check_image, QtCore.SIGNAL("clicked()"), MainWindow.manual_capture)
        QtCore.QObject.connect(self.pushButton_manual_calibrate, QtCore.SIGNAL("clicked()"), MainWindow.manual_adjustment_parameters)
        QtCore.QObject.connect(self.pushButton_self_calibrate, QtCore.SIGNAL("clicked()"), MainWindow.self_calibration)
        QtCore.QObject.connect(self.pushButton_set_calibration_line, QtCore.SIGNAL("clicked()"), MainWindow.set_calibration_line)
        QtCore.QObject.connect(self.comboBox_change_product, QtCore.SIGNAL("currentTextChanged(QString)"), MainWindow.change_product)
        QtCore.QObject.connect(self.checkBox_key_sensor, QtCore.SIGNAL("toggled(bool)"), MainWindow.key_sensor_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "KeyReader", None, -1))
        self.groupBox_show_image.setTitle(QtWidgets.QApplication.translate("MainWindow", "实时影像", None, -1))
        self.label_show_image.setText(QtWidgets.QApplication.translate("MainWindow", "实时影像", None, -1))
        self.groupBox_result.setTitle(QtWidgets.QApplication.translate("MainWindow", "结果展示区", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "产品信息", None, -1))
        self.label_plant.setText(QtWidgets.QApplication.translate("MainWindow", "厂家:", None, -1))
        self.label_product.setText(QtWidgets.QApplication.translate("MainWindow", "产品：", None, -1))
        self.label_marble_number.setText(QtWidgets.QApplication.translate("MainWindow", "弹子数：", None, -1))
        self.radioButton_single_row.setText(QtWidgets.QApplication.translate("MainWindow", "单排齿", None, -1))
        self.radioButton_double_row.setText(QtWidgets.QApplication.translate("MainWindow", "双排齿", None, -1))
        self.label_key_sensor.setText(QtWidgets.QApplication.translate("MainWindow", "到位传感器:", None, -1))
        self.checkBox_key_sensor.setText(QtWidgets.QApplication.translate("MainWindow", "有", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "选择产品：", None, -1))
        self.pushButton_set_calibration_line.setText(QtWidgets.QApplication.translate("MainWindow", "设定标定线", None, -1))
        self.pushButton_self_calibrate.setText(QtWidgets.QApplication.translate("MainWindow", "校准(自动调参)", None, -1))
        self.pushButton_manual_calibrate.setText(QtWidgets.QApplication.translate("MainWindow", "手动调参", None, -1))
        self.pushButton_check_image.setText(QtWidgets.QApplication.translate("MainWindow", "查看图像", None, -1))
        self.pushButton_start.setText(QtWidgets.QApplication.translate("MainWindow", "开始", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

