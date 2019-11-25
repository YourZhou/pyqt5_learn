import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
#我们需要一个来自QtCore的对象模块。

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 按钮是一个QPushButton类的实例。
        # 构造方法的第一个参数是显示在button上的标签文本。
        # 第二个参数是父组件。
        qbtn = QPushButton('Quit', self)
        # 事件处理系统由信号&槽机制建立,
        # 如果我们点击了按钮，信号clicked被发送。
        # QCoreApplication类包含了主事件循环；
        # 它处理和转发所有事件。
        # instance()方法给我们返回一个实例化对象。
        # 点击信号连接到quit()方法，
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())