import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel
from PyQt5.QtCore import QTimer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 初始化主頁面佈局
        self.layout = QVBoxLayout()
        
        # 創建 QStackedWidget 來存放不同的頁面
        self.stack = QStackedWidget()
        
        # 創建兩個頁面
        self.page1 = QWidget()
        self.page2 = QWidget()
        
        # 設定頁面1
        self.page1_layout = QVBoxLayout()
        self.page1_label = QLabel("這是頁面 1")
        self.page1_button = QPushButton("切換到頁面 2")
        self.page1_button.clicked.connect(self.show_page2)
        self.page1_layout.addWidget(self.page1_label)
        self.page1_layout.addWidget(self.page1_button)
        self.page1.setLayout(self.page1_layout)
        
        # 設定頁面2
        self.page2_layout = QVBoxLayout()
        self.page2_label = QLabel("這是頁面 2")
        self.page2_button = QPushButton("切換到頁面 1")
        self.page2_button.clicked.connect(self.show_page1)
        
        # 添加倒數計時器標籤
        self.timer_label = QLabel("倒數計時: 10 秒")
        self.page2_layout.addWidget(self.page2_label)
        self.page2_layout.addWidget(self.timer_label)
        self.page2_layout.addWidget(self.page2_button)
        self.page2.setLayout(self.page2_layout)
        
        # 初始化倒數計時器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 10
        
        # 將頁面添加到 QStackedWidget
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        
        # 設定初始頁面
        self.stack.setCurrentWidget(self.page1)
        
        # 將 QStackedWidget 添加到主頁面佈局
        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)
        
    def show_page1(self):
        self.stack.setCurrentWidget(self.page1)
        self.timer.stop()  # 停止計時器
        
    def show_page2(self):
        self.stack.setCurrentWidget(self.page2)
        self.time_left = 10  # 重置倒數時間
        self.timer_label.setText(f"倒數計時: {self.time_left} 秒")
        self.timer.start(1000)  # 啟動計時器，每秒更新一次
        
    def update_timer(self):
        self.time_left -= 1
        self.timer_label.setText(f"倒數計時: {self.time_left} 秒")
        if self.time_left == 0:
            self.timer.stop()
            self.timer_label.setText("時間到！")

# 主程序
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

