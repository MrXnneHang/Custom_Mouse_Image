import sys
import pyautogui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口无边框、透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

        # 创建 QLabel 用于显示图片
        self.label = QLabel(self)
        pixmap = QPixmap('.\\fig\\mayi.jpg')  # 加载你的图片
        self.label.setPixmap(pixmap.scaled(40, 40, Qt.KeepAspectRatio))  # 缩放图片

        # 调整窗口大小为图片大小
        self.resize(pixmap.width(), pixmap.height())

        # 设置定时器，定期更新鼠标位置
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.followMouse)
        self.timer.start(10)  # 每10ms更新一次位置

    def followMouse(self):
        # 使用pyautogui获取鼠标位置并移动窗口
        mouse_pos = pyautogui.position()
        # 修正的x和y
        x = 450
        y = 450
        self.move(x + mouse_pos.x - self.width() // 2,y + mouse_pos.y - self.height() // 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    transWindow = TransparentWindow()
    transWindow.show()
    sys.exit(app.exec_())
