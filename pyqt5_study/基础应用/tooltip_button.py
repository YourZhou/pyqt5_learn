import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这个静态方法设置了用于提示框的字体。
        # 我们使用10px大小的SansSerif字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        # 为了创建提示框，我们调用了setTooltip()方法。
        # 我们可以在提示框中使用富文本格式。
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 我们创建了一个按钮组件并且为它设置一个提示框。
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # setHint()方法给了按钮一个推荐的大小。
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
