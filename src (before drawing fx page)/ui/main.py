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
        

        self.path_to_Qfolder = "./question"  # 替換為你的圖片資料夾路徑
        self.path_to_Afolder = "./answer"
        self.imageQ_path_list=[] #image files名稱改為imageQ_path_list
        self.imageA_path_list=[] #image_files_ans名稱改為imageA_path_list
        
        self.current_index = 0
        self.path=''#難度的全路徑會由func填
        self.path_ans = ''

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
        


        
        
    
    def load_all_image_path_to_two_list(self):
        self.path= self.path_to_Qfolder+f"/{self.difficulty}"
        self.path_ans=self.path_to_Afolder + f"/{self.difficulty}"
        self.imageA_path_list = []
        self.imageQ_path_list = []
        for filename in os.listdir(self.path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.imageQ_path_list.append(os.path.join(self.path, filename))
                self.imageA_path_list.append(os.path.join(self.path_ans, filename))
        return self.imageQ_path_list, self.imageA_path_list

    def load_images(self):
        #目前只在page 4用到
        if self.imageQ_path_list and self.imageA_path_list:
            pixmap1 = QPixmap(self.imageQ_path_list[self.current_index]).scaled(512, 512, Qt.KeepAspectRatio)
            # self.imageA_path_list[self.current_index]

            self.image_label_p4_Q.setPixmap(pixmap1)
    ######################   
    def create_page1(self):
        self.page1 = QWidget()
        layout = QVBoxLayout()
        
        

        label = QLabel("")#之後可以再用
        label.setAlignment(Qt.AlignCenter)
        button = QPushButton("Start!!")
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
            "Game Instructions:\nThis is a game that tests memory and luck.\nFirst, you will be shown a photograph and\nanother one from which some things have been removed.\n"
            "You have 30 seconds to observe the differences between the two.\nAfterward, you will be given the original image,\nwhere you will mark areas to be removed.\n"
            "When you feel you're done, submit to check your score."
        )
        font = instructions.font()  # 獲取現有的字體設置
        font.setPointSize(16)  # 設置字體大小
        instructions.setFont(font)  # 設置新的字體設置
    
        next_button = QPushButton("Next")
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
        
        label = QLabel("Level")
        label.setAlignment(Qt.AlignCenter)
        
        easy_button = QPushButton("Easy")
        medium_button = QPushButton("Medium")
        hard_button = QPushButton("Hard")
        
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
        
        self.image_label_p4_Q = QLabel("")
        self.image_label_p4_Q.setAlignment(Qt.AlignCenter)
        
        prev_button = QPushButton("Previous")
        next_button = QPushButton("Next")
        confirm_button = QPushButton("Confirm")
        
        prev_button.clicked.connect(self.show_previous_image)
        next_button.clicked.connect(self.show_next_image)
        confirm_button.clicked.connect(self.show_page5)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(prev_button)
        button_layout.addWidget(next_button)
        button_layout.addWidget(confirm_button)
        
        layout.addWidget(self.image_label_p4_Q)
        layout.addLayout(button_layout)
        
        self.page4.setLayout(layout)
    
    def create_page5(self):
        self.page5 = QWidget()
        layout = QVBoxLayout()
        img_layout = QHBoxLayout()
        
        self.timer_label = QLabel(f"Time remaining: {self.time_left} secs")
        self.timer_label.setAlignment(Qt.AlignHCenter)
        
        self.image_label_p5_Q = QLabel()
        self.image_label_p5_Q.setFixedSize(512, 512)
        self.image_label_p5_Q.setAlignment(Qt.AlignLeft)
    
        self.image_label_p5_A = QLabel()
        self.image_label_p5_A.setFixedSize(512, 512)
        self.image_label_p5_A.setAlignment(Qt.AlignRight)

       
        # pixmap1 = QPixmap(self.image_files[self.current_index]).scaled(512, 512, Qt.KeepAspectRatio)
        # self.image_label_p5_Q.setPixmap(pixmap1)
    
        # pixmap2 = QPixmap(self.image_file_ans[self.current_index]).scaled(512, 512, Qt.KeepAspectRatio)
        # self.image_label_p5_A.setPixmap(pixmap2)
        
        layout.addWidget(self.timer_label)
        img_layout.addWidget(self.image_label_p5_Q)
        img_layout.addWidget(self.image_label_p5_A)

        layout.addLayout(img_layout)
        self.page5.setLayout(layout)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
    
    def create_page6(self):
        self.page6 = QWidget()
        layout = QVBoxLayout()
        
        self.drawing_area = QLabel("Draw where you want to delete")
        confirm_button = QPushButton("I'm finished, show result")
        confirm_button.clicked.connect(self.show_page7)
        
        layout.addWidget(self.drawing_area)
        layout.addWidget(confirm_button, alignment=Qt.AlignCenter)
        
        self.page6.setLayout(layout)
    
    def create_page7(self):
        self.page7 = QWidget()
        layout = QVBoxLayout()
        
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        
        play_again_button = QPushButton("Play again")
        quit_button = QPushButton("End Game")
        
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
        self.load_all_image_path_to_two_list()
        self.current_index = 0
        self.load_images()
        self.show_page4()
    
    def show_previous_image(self):
        #page 4用而已
        self.current_index = (self.current_index - 1) % len(self.imageQ_path_list)
        self.load_images()
    
    def show_next_image(self):
        #page 4而已
        self.current_index = (self.current_index + 1) % len(self.imageQ_path_list)
        self.load_images()

    
    def update_timer(self):
        self.time_left -= 1
        self.timer_label.setText(f"Time remaining: {self.time_left} secs")
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
        pixmap1 = QPixmap(self.imageQ_path_list[self.current_index]).scaled(512, 512, Qt.KeepAspectRatio)
        self.image_label_p5_Q.setPixmap(pixmap1)
    
        pixmap2 = QPixmap(self.imageA_path_list[self.current_index]).scaled(512, 512, Qt.KeepAspectRatio)
        self.image_label_p5_A.setPixmap(pixmap2)

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
