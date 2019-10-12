# python自带库
import sys
# 第三方库
import cv2 as cv
from PySide2.QtWidgets import QWidget, QApplication
# 自己的包
from UI2PY.set_calibration_line import Ui_Form
from config import Config


class SetCalibrationLine(QWidget, Ui_Form):
    def __init__(self):
        super(SetCalibrationLine, self).__init__()
        self.setupUi(self)
        self.conf = Config()
        self.marble_number = int(self.conf.read_config('product', 'marble_number'))
        self.setup()

    def setup(self):
        ptStart_bottom_x, ptStart_bottom_y = eval(self.conf.read_config('line', 'ptStart_bottom'))
        ptEnd_bottom_x, ptEnd_bottom_y = eval(self.conf.read_config('line', 'ptEnd_bottom'))
        ptStart_top_x, ptStart_top_y = eval(self.conf.read_config('line', 'ptStart_top'))
        ptEnd_top_x, ptEnd_top_y = eval(self.conf.read_config('line', 'ptEnd_top'))

        pts_vertical = eval(self.conf.read_config('line', 'pts_vertical'))
        pts_vertical1, pts_vertical2 = pts_vertical
        pts_vertical1_start, pts_vertical1_end = pts_vertical1
        pts_vertical2_start, pts_vertical2_end = pts_vertical2
        pts_vertical1_start_x, pts_vertical1_start_y = pts_vertical1_start
        pts_vertical1_end_x, pts_vertical1_end_y = pts_vertical1_end
        pts_vertical2_start_x, pts_vertical2_start_y = pts_vertical2_start
        pts_vertical2_end_x, pts_vertical2_end_y = pts_vertical2_end

        min_threshold = int(self.conf.read_config('canny', 'min_threshold'))
        max_threshold = int(self.conf.read_config('canny', 'max_threshold'))

        self.spinBox_ptStart_bottom_x.setValue(ptStart_bottom_x)
        self.spinBox_ptStart_bottom_y.setValue(ptStart_bottom_y)
        self.spinBox_ptEnd_bottom_x.setValue(ptEnd_bottom_x)
        self.spinBox_ptEnd_bottom_y.setValue(ptEnd_bottom_y)

        self.spinBox_ptStart_top_x.setValue(ptStart_top_x)
        self.spinBox_ptStart_top_y.setValue(ptStart_top_y)
        self.spinBox_ptEnd_top_x.setValue(ptEnd_top_x)
        self.spinBox_ptEnd_top_y.setValue(ptEnd_top_y)

        self.spinBox_pts_vertical1_start_x.setValue(pts_vertical1_start_x)
        self.spinBox_pts_vertical1_start_y.setValue(pts_vertical1_start_y)
        self.spinBox_pts_vertical1_end_x.setValue(pts_vertical1_end_x)
        self.spinBox_pts_vertical1_end_y.setValue(pts_vertical1_end_y)

        self.spinBox_pts_vertical2_start_x.setValue(pts_vertical2_start_x)
        self.spinBox_pts_vertical2_start_y.setValue(pts_vertical2_start_y)
        self.spinBox_pts_vertical2_end_x.setValue(pts_vertical2_end_x)
        self.spinBox_pts_vertical2_end_y.setValue(pts_vertical2_end_y)

        self.spinBox_min_threshold.setValue(min_threshold)
        self.spinBox_max_threshold.setValue(max_threshold)

    def check(self):
        print('点击了查看')
        original_img = cv.imread("key.jpg", 0)
        # cap = cv.VideoCapture(0)
        # res, original_img = cap.read()
        # 画线的粗细和类型
        thickness = int(self.conf.read_config('line', 'thickness'))
        lineType = int(self.conf.read_config('line', 'lineType'))
        # 底线起点和终点的坐标
        ptStart_bottom = (self.spinBox_ptStart_bottom_x.value(), self.spinBox_ptStart_bottom_y.value())
        ptEnd_bottom = (self.spinBox_ptEnd_bottom_x.value(), self.spinBox_ptEnd_bottom_y.value())
        point_color_bottom = eval(self.conf.read_config('line', 'point_color_bottom'))  # BGR
        cv.line(original_img, ptStart_bottom, ptEnd_bottom, point_color_bottom, thickness, lineType)

        # 顶线起点和终点的坐标
        ptStart_top = (self.spinBox_ptStart_top_x.value(), self.spinBox_ptStart_top_y.value())
        ptEnd_top = (self.spinBox_ptEnd_top_x.value(), self.spinBox_ptEnd_top_y.value())
        point_color_top = eval(self.conf.read_config('line', 'point_color_top'))  # BGR
        cv.line(original_img, ptStart_top, ptEnd_top, point_color_top, thickness, lineType)

        # 竖线（对准弹子）
        pts_vertical = [[(self.spinBox_pts_vertical1_start_x.value(), self.spinBox_pts_vertical1_start_y.value()),
                         (self.spinBox_pts_vertical1_end_x.value(), self.spinBox_pts_vertical1_end_y.value())],
                        [(self.spinBox_pts_vertical2_start_x.value(), self.spinBox_pts_vertical2_start_y.value()),
                         (self.spinBox_pts_vertical2_end_x.value(), self.spinBox_pts_vertical2_end_y.value())]]
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
        canny = cv.Canny(img1, self.spinBox_min_threshold.value(), self.spinBox_max_threshold.value())
        # cap.release()
        cv.imshow('Canny', canny)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def submit(self):
        ptStart_bottom = (self.spinBox_ptStart_bottom_x.value(), self.spinBox_ptStart_bottom_y.value())
        ptEnd_bottom = (self.spinBox_ptEnd_bottom_x.value(), self.spinBox_ptEnd_bottom_y.value())
        ptStart_top = (self.spinBox_ptStart_top_x.value(), self.spinBox_ptStart_top_y.value())
        ptEnd_top = (self.spinBox_ptEnd_top_x.value(), self.spinBox_ptEnd_top_y.value())
        pts_vertical = [[(self.spinBox_pts_vertical1_start_x.value(), self.spinBox_pts_vertical1_start_y.value()),
                         (self.spinBox_pts_vertical1_end_x.value(), self.spinBox_pts_vertical1_end_y.value())],
                        [(self.spinBox_pts_vertical2_start_x.value(), self.spinBox_pts_vertical2_start_y.value()),
                         (self.spinBox_pts_vertical2_end_x.value(), self.spinBox_pts_vertical2_end_y.value())]]
        min_threshold = self.spinBox_min_threshold.value()
        max_threshold = self.spinBox_max_threshold.value()

        self.conf.update_config(section='line', name='ptStart_bottom', value=str(ptStart_bottom))
        self.conf.update_config(section='line', name='ptEnd_bottom', value=str(ptEnd_bottom))
        self.conf.update_config(section='line', name='ptStart_top', value=str(ptStart_top))
        self.conf.update_config(section='line', name='ptEnd_top', value=str(ptEnd_top))
        self.conf.update_config(section='line', name='pts_vertical', value=str(pts_vertical))
        self.conf.update_config(section='canny', name='min_threshold', value=str(min_threshold))
        self.conf.update_config(section='canny', name='max_threshold', value=str(max_threshold))
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SetCalibrationLine()
    demo.show()
    sys.exit(app.exec_())
