import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

#Example类继承自QWidget类。
# 这意味着我们调用了两个构造方法：
# 第一个是Example类的构造方法，
# 第二个是被继承类的构造方法。
# super()方法返回了Example类的父类对象，
# 并且我们调用了父类的构造方法。
# _init__()方法是Python语言中的构造方法。
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。
        # 第三个参数是定义窗口的宽度，
        # 第四个参数是定义窗口的高度。
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())