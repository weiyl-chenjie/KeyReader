# python自带库
import sys
from time import sleep
import sqlite3
# 第三方库
import cv2 as cv
import numpy as np
from PySide2.QtWidgets import QMainWindow, QWidget, QApplication
from PySide2.QtGui import Qt, QImage, QPixmap
from PySide2.QtCore import QTimer, QThread, Signal
# 自己的包
from UI2PY.MainWindow import Ui_MainWindow
from set_calibration_line import SetCalibrationLine
from config import Config


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.set_calibration_line_pane = SetCalibrationLine()
        self.set_calibration_line_pane.setWindowModality(Qt.ApplicationModal)  # 设置为模态窗口

        self._thread = VideoThread()
        self._thread.signal.connect(self.show_video)
        self.conf = Config()

        self.plant = ''
        self.product = ''
        self.marble_number = 0
        self.row_number = 0
        self.setup()

    def setup(self):
        # 获取厂家名
        self.plant = self.conf.read_config('product', 'plant')
        # 获取产品名
        self.product = self.conf.read_config('product', 'product')
        # 获取弹子数
        self.marble_number = int(self.conf.read_config('product', 'marble_number'))
        # 单排齿还是多排齿
        self.row_number = int(self.conf.read_config('product', 'row_number'))
        # 设置控件值
        self.lineEdit_plant.setText(self.plant)
        self.lineEdit_product.setText(self.product)
        self.lineEdit_marble_number.setText(str(self.marble_number))
        if self.row_number == 1:
            self.radioButton_single_row.setCheckable(True)
            self.radioButton_single_row.setChecked(True)
            self.radioButton_double_row.setCheckable(False)
        elif self.row_number == 2:
            self.radioButton_double_row.setCheckable(True)
            self.radioButton_double_row.setChecked(True)
            self.radioButton_single_row.setCheckable(False)

        self.comboBox_change_product.addItem('')
        with sqlite3.connect('keyid.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT plant, product, marble_number, rows FROM products")
            rows = cur.fetchall()
            for row in rows:
                plant = row[0]
                product = row[1]
                item = plant + ":" + product
                self.comboBox_change_product.addItem(item)

    def start(self):
        self._thread.working = True
        if not self._thread.cap.isOpened():
            self._thread.cap.open(0)
        self._thread.start()

    def change_product(self, item):
        if item:  # 若果选择了非空项目
            product = item.split(":")[1]
            print(product)
            with sqlite3.connect('keyid.db') as conn:
                cur = conn.cursor()
                cur.execute("SELECT plant, product, marble_number, rows FROM products WHERE product ='%s'" % product)
                rows = cur.fetchall()
                row = rows[0]  # 应该只有一条数据
                self.plant = row[0]
                self.product = row[1]
                self.marble_number = row[2]
                self.row_number = row[3]

            self.lineEdit_plant.setText(self.plant)
            self.lineEdit_product.setText(self.product)
            self.lineEdit_marble_number.setText(str(self.marble_number))
            if self.row_number == 1:
                self.radioButton_single_row.setCheckable(True)
                self.radioButton_single_row.setChecked(True)
                self.radioButton_double_row.setCheckable(False)
            elif self.row_number == 2:
                self.radioButton_double_row.setCheckable(True)
                self.radioButton_double_row.setChecked(True)
                self.radioButton_single_row.setCheckable(False)

            # 修改config.ini文件
            self.conf.update_config(section='product', name='plant', value=self.plant)
            self.conf.update_config(section='product', name='product', value=self.product)
            self.conf.update_config(section='product', name='marble_number', value=str(self.marble_number))
            self.conf.update_config(section='product', name='row_number', value=str(self.row_number))

    def manual_adjustment_parameters(self):
        pass

    def self_calibration(self):
        step = 1
        while step < 5:
            cv.waitKey()
            if step == 1:
                pass

        print(self._thread.cap.isOpened())
        cap = cv.VideoCapture(0)
        res, frame = cap.read()
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.label_show_image.setPixmap(QPixmap.fromImage(img))
        cap.release()
        print(res, frame)

    def set_calibration_line(self):
        # 暂停读取摄像头进程，并释放摄像头，然后调用设置校准线的窗口
        self._thread.__del__()

        self.set_calibration_line_pane.show()

    def show_video(self):
        img = QImage(self._thread.img, self._thread.img.shape[1], self._thread.img.shape[0], QImage.Format_RGB888)
        self.label_show_image.setPixmap(QPixmap.fromImage(img))
        # print("发送信号了")

    def get_keyid(self, key):
        one = int(self.conf.read_config('key', 'one'))
        two = int(self.conf.read_config('key', 'two'))
        three = int(self.conf.read_config('key', 'three'))
        four = int(self.conf.read_config('key', 'four'))
        tolerance = int(self.conf.read_config('key', 'tolerance'))
        if one - tolerance < key < one + tolerance:
            return '1'
        elif two - tolerance < key < two + tolerance:
            return '2'
        elif three - tolerance < key < three + tolerance:
            return '3'
        elif four - tolerance < key < four + tolerance:
            return '4'
        else:
            return 'X'

    def get_keycode(self, keyid):
        with sqlite3.connect('keyid.db') as conn:
            c = conn.cursor()
            rows = c.execute("SELECT keycode from %s WHERE keyid='%s'" % (self.product, keyid)).fetchall()
            keycode = rows[0][0]
            return keycode

    def capture(self):
        print('点击了查看图像')
        original_img = cv.imread("key.jpg", 0)
        # original_img = self._thread.img
        # 画线的粗细和类型
        thickness = int(self.conf.read_config('line', 'thickness'))
        lineType = int(self.conf.read_config('line', 'lineType'))
        # 底线起点和终点的坐标
        ptStart_bottom = eval(self.conf.read_config('line', 'ptStart_bottom'))
        ptEnd_bottom = eval(self.conf.read_config('line', 'ptEnd_bottom'))
        point_color_bottom = eval(self.conf.read_config('line', 'point_color_bottom'))  # BGR
        cv.line(original_img, ptStart_bottom, ptEnd_bottom, point_color_bottom, thickness, lineType)

        # 顶线起点和终点的坐标
        ptStart_top = eval(self.conf.read_config('line', 'ptStart_top'))
        ptEnd_top = eval(self.conf.read_config('line', 'ptEnd_top'))
        point_color_top = eval(self.conf.read_config('line', 'point_color_top'))  # BGR
        cv.line(original_img, ptStart_top, ptEnd_top, point_color_top, thickness, lineType)

        # 竖线（对准弹子）
        pts_vertical = eval(self.conf.read_config('line', 'pts_vertical'))
        # marble_number = int(self.conf.read_config('product', 'marble_number'))
        for i in range(self.marble_number):
            if i < 2:
                continue
            pts_vertical.append(
                [(pts_vertical[0][0][0] + (pts_vertical[1][0][0] - pts_vertical[0][0][0]) * i, pts_vertical[0][0][1]),
                 (pts_vertical[0][0][0] + (pts_vertical[1][0][0] - pts_vertical[0][0][0]) * i, pts_vertical[0][1][1])])
        point_color_vertical = (255, 0, 0)  # BGR
        for pt in pts_vertical:
            cv.line(original_img, pt[0], pt[1], point_color_vertical, thickness, lineType)

        # canny(): 边缘检测
        img1 = cv.GaussianBlur(original_img, (3, 3), 0)
        canny = cv.Canny(img1, 200, 255)

        # 形态学：边缘检测
        # _, Thr_img = cv.threshold(original_img, 210, 255, cv.THRESH_BINARY)  # 设定红色通道阈值210（阈值影响梯度运算效果）
        # kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 定义矩形结构元素
        # gradient = cv.morphologyEx(Thr_img, cv.MORPH_GRADIENT, kernel)  # 梯度
        # cv.imshow("original_img", original_img)
        # cv.imshow("gradient", gradient)
        # cv.imshow('Canny', canny)

        keyid = ''
        for pt in pts_vertical:
            for i in range(ptStart_top[1] + 2, ptStart_bottom[1]):
                if canny[i][pt[0][0]] == 255:
                    keyid += self.get_keyid(i)
                    print(i)
                    break
        print(keyid)
        keycode = self.get_keycode(keyid)
        print(keycode)
        self.lineEdit_key_code.setText(keycode)
        self.lineEdit_key_id.setText(keyid)
        cv.waitKey(0)
        cv.destroyAllWindows()


class VideoThread(QThread):
    signal = Signal()

    def __init__(self):
        super(VideoThread, self).__init__()
        self.working = True  # 工作状态
        self.cap = cv.VideoCapture(0)

        if not self.cap.isOpened():
            print('无法打开摄像机')
            exit()

        self.img = np.array([])

    def __del__(self):
        self.working = False  # 工作状态
        # When everything done, release the capture
        self.cap.release()
        cv.destroyAllWindows()
        self.wait()

    def run(self):
        # 进行线程任务
        while self.working:
            sleep(0.1)
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # RGB转BGR
            frame_bgr = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            self.img = frame_bgr
            # Display the resulting frame
            # cv.imshow('frame', gray)
            # if cv.waitKey(1) == ord('q'):
            #     break
            self.signal.emit()  # 发射信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())

