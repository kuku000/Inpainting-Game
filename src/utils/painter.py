import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QFileDialog
from PyQt5.QtCore import QTimer, QDir, Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QImage

class Sketcher:
    def __init__(self, windowname, dests, colors_func, thick, type,drawing_area_from_qt):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        
        self.thick = thick
        #從qt傳過來要更改的drwaing area
        self.drawing_area_from_qt = drawing_area_from_qt
        # 將原始圖像轉換為 QImage 或 QPixmap
        self.qt_image = self.cvimg_to_qimage(self.dests[0])
        self.qt_pixmap = QPixmap.fromImage(self.qt_image)
        self.show()
        if type == "bbox":
            cv2.setMouseCallback(self.windowname, self.on_bbox)
        else:
            cv2.setMouseCallback(self.windowname, self.on_mouse)


    def large_thick(
        self,
    ):
        self.thick = min(48, self.thick + 1)

    def small_thick(
        self,
    ):
        self.thick = max(3, self.thick - 1)

    # def show(self):
    #     cv2.imshow(self.windowname, self.dests[0])
    def show(self):
        # 更新 QImage 或 QPixmap
        cv2.imshow(self.windowname, self.dests[0])
        self.qt_image = self.cvimg_to_qimage(self.dests[0])
        self.qt_pixmap = QPixmap.fromImage(self.qt_image)

        # # 將更新後的圖像顯示在 PyQt5 界面的 QLabel 中
        print(type(self.drawing_area_from_qt))
        self.drawing_area_from_qt.setPixmap(self.qt_pixmap)
        # return self.qt_pixmap

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv2.EVENT_LBUTTONUP:
            self.prev_pt = None

        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv2.line(dst, self.prev_pt, pt, color, self.thick)
            self.dirty = True
            self.prev_pt = pt
            self.show()

    def on_bbox(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv2.EVENT_LBUTTONUP:
            for dst, color in zip(self.dests, self.colors_func()):
                cv2.rectangle(dst, self.prev_pt, pt, color, -1)
            self.dirty = True
            self.prev_pt = None
            self.show(self.drawing_area_from_qt)
    #by chat
    def cvimg_to_qimage(self, cvimg):
        """Convert OpenCV image format to QImage."""
        height, width, channel = cvimg.shape
        bytes_per_line = 3 * width
        qimg = QImage(cvimg.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        return qimg