import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #QAction是一个用于菜单栏、工具栏或自定义快捷键的抽象动作行为。
        #我们创建了一个有指定图标和文本为'Exit'的标签。
        # 另外，还为这个动作定义了一个快捷键。
        # 第三行创建一个当我们鼠标浮于菜单项之上就会显示的一个状态提示。
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        #信号连接到QApplication组件的quit()方法。这样就中断了应用。
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())