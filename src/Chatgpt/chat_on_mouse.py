import numpy as np

class Sketcher:
    # 初始化和其他代碼...

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv2.EVENT_LBUTTONUP:
            self.prev_pt = None

        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv2.line(dst, self.prev_pt, pt, color, self.thick)
                # 將畫出的線條更新到 QImage 或 QPixmap
                self.update_qt_image(dst)
            self.dirty = True
            self.prev_pt = pt
            self.show()

    def update_qt_image(self, dst):
        # 更新 QImage 或 QPixmap
        self.qt_image = self.cvimg_to_qimage(dst)
        self.qt_pixmap = QPixmap.fromImage(self.qt_image)
