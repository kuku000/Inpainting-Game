import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QFileDialog
from PyQt5.QtCore import QTimer, QDir,Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import io 
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化變數
        self.setFixedSize(1024, 640)
        self.time_left = 20
        self.difficulty = 'easy'
        self.open_pic = './open.png'
        self.background_pic = './show2.png'

        # 初始化主頁面佈局
        self.layout = QVBoxLayout()
        
        # 創建 QStackedWidget 來存放不同的頁面
        self.stack = QStackedWidget()

        
        
        # 創建頁面
        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.create_page4()
        self.create_page5()
        self.create_page6()
        self.create_page7()
        
        # 將頁面添加到 QStackedWidget
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)
        self.stack.addWidget(self.page4)
        self.stack.addWidget(self.page5)
        self.stack.addWidget(self.page6)
        self.stack.addWidget(self.page7)
        
        # 設定初始頁面
        self.stack.setCurrentWidget(self.page1)
        
        # 將 QStackedWidget 添加到主頁面佈局
        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)
        
    ######################
        self.image_folder = "./question"  # 替換為你的圖片資料夾路徑
        # self.image_paths = self.load_images_from_folder(self.image_folder)
        self.current_index = 0
        self.path=''
    
    def load_images_from_folder(self, folder):
        self.path=folder+f"/{self.difficulty}"
        image_files = []
        for filename in os.listdir(self.path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_files.append(os.path.join(self.path, filename))
        return image_files   

    def load_images(self):
        if self.image_paths:
            pixmap1 = QPixmap(self.image_paths[self.current_index]).scaled(512, 512, Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap1)
    ######################   
    def create_page1(self):
        self.page1 = QWidget()
        layout = QVBoxLayout()
        
        

        label = QLabel("遊戲名稱")
        label.setAlignment(Qt.AlignCenter)
        button = QPushButton("開始")
        button.clicked.connect(self.show_page2)
        
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(button, alignment=Qt.AlignRight | Qt.AlignBottom)
        self.page1.setLayout(layout)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(self.open_pic)))
        self.page1.setAutoFillBackground(True)
        self.page1.setPalette(palette)

    def create_page2(self):
        self.page2 = QWidget()
        layout = QVBoxLayout()



        instructions = QLabel(
            "遊戲說明:\n這是一個考驗記憶力與運氣的遊戲，首先你會被給予一張照片，和一個拿掉某些東西後的照片，"
            "你可以在30秒內觀察兩者的差別。\n\n之後，你會被給予一張原圖，你將在上面塗畫記號，這些記號代表你要去除的部分，"
            "你覺得完成之後，就按繳交查看分數。"
        )
        next_button = QPushButton("下一頁")
        next_button.clicked.connect(self.show_page3)
        
        layout.addWidget(instructions)
        layout.addStretch()
        layout.addWidget(next_button, alignment=Qt.AlignRight | Qt.AlignBottom)
        self.page2.setLayout(layout)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(self.background_pic)))
        self.setPalette(palette)
        

    def create_page3(self):
        self.page3 = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel("選擇難度")
        label.setAlignment(Qt.AlignCenter)
        
        easy_button = QPushButton("簡單")
        medium_button = QPushButton("中等")
        hard_button = QPushButton("高難度")
        
        easy_button.clicked.connect(lambda: self.set_difficulty('easy'))
        medium_button.clicked.connect(lambda: self.set_difficulty('medium'))
        hard_button.clicked.connect(lambda: self.set_difficulty('hard'))
        layout.addWidget(label)
        layout.addWidget(easy_button)
        layout.addWidget(medium_button)
        layout.addWidget(hard_button)
        layout.addStretch()
        
        self.page3.setLayout(layout)
    
    def create_page4(self):
        self.page4 = QWidget()
        layout = QVBoxLayout()
        
        self.image_label = QLabel("顯示圖片的方框")
        self.image_label.setAlignment(Qt.AlignCenter)
        
        prev_button = QPushButton("上一張")
        next_button = QPushButton("下一張")
        confirm_button = QPushButton("確定")
        
        prev_button.clicked.connect(self.show_previous_image)
        next_button.clicked.connect(self.show_next_image)
        confirm_button.clicked.connect(self.show_page5)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(prev_button)
        button_layout.addWidget(next_button)
        button_layout.addWidget(confirm_button)
        
        layout.addWidget(self.image_label)
        layout.addLayout(button_layout)
        
        self.page4.setLayout(layout)
    
    def create_page5(self):
        self.page5 = QWidget()
        layout = QVBoxLayout()
        img_layout = QHBoxLayout()
        
        self.timer_label = QLabel(f"倒數計時: {self.time_left} 秒")
        self.timer_label.setAlignment(Qt.AlignHCenter)
        
        self.image_label1 = QLabel()
        self.image_label1.setFixedSize(512, 512)
        self.image_label1.setAlignment(Qt.AlignLeft)
    
        self.image_label2 = QLabel()
        self.image_label2.setFixedSize(512, 512)
        self.image_label2.setAlignment(Qt.AlignRight)

        pixmap1 = QPixmap("open.png").scaled(512, 512, Qt.KeepAspectRatio)
        self.image_label1.setPixmap(pixmap1)
    
        pixmap2 = QPixmap("show2.png").scaled(512, 512, Qt.KeepAspectRatio)
        self.image_label2.setPixmap(pixmap2)
        
        layout.addWidget(self.timer_label)
        img_layout.addWidget(self.image_label1)
        img_layout.addWidget(self.image_label2)

        layout.addLayout(img_layout)
        self.page5.setLayout(layout)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
    
    def create_page6(self):
        self.page6 = QWidget()
        layout = QVBoxLayout()
        
        self.drawing_area = QLabel("在這裡畫記號")
        confirm_button = QPushButton("確認完成作答，看答案")
        confirm_button.clicked.connect(self.show_page7)
        
        layout.addWidget(self.drawing_area)
        layout.addWidget(confirm_button, alignment=Qt.AlignCenter)
        
        self.page6.setLayout(layout)
    
    def create_page7(self):
        self.page7 = QWidget()
        layout = QVBoxLayout()
        
        self.result_label = QLabel("顯示結果")
        self.result_label.setAlignment(Qt.AlignCenter)
        
        play_again_button = QPushButton("再玩一次")
        quit_button = QPushButton("結束遊戲")
        
        play_again_button.clicked.connect(self.show_page3)
        quit_button.clicked.connect(self.close)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(play_again_button)
        button_layout.addWidget(quit_button)
        
        layout.addWidget(self.result_label)
        layout.addLayout(button_layout)
        
        self.page7.setLayout(layout)
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.image_paths = self.load_images_from_folder(self.image_folder)
        self.current_index = 0
        self.load_images()
        self.show_page4()
    
    def show_previous_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_paths)
        self.load_images()
    
    def show_next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.load_images()
    
    def update_timer(self):
        self.time_left -= 1
        self.timer_label.setText(f"倒數計時: {self.time_left} 秒")
        if self.time_left == 0:
            self.timer.stop()
            self.show_page6()
    
    def show_page2(self):
        self.stack.setCurrentWidget(self.page2)
        
    def show_page3(self):
        self.stack.setCurrentWidget(self.page3)
    
    def show_page4(self):
        self.stack.setCurrentWidget(self.page4)
    
    def show_page5(self):
        self.stack.setCurrentWidget(self.page5)
        self.time_left = 20
        self.timer.start(1000)
    
    def show_page6(self):
        self.stack.setCurrentWidget(self.page6)
    
    def show_page7(self):
        self.stack.setCurrentWidget(self.page7)

# 主程序
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
