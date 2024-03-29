import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    #如果我们关闭一个QWidget，QCloseEvent类事件将被生成。
    # 要修改组件动作我们需要重新实现closeEvent()事件处理方法。
    def closeEvent(self, event):
        # 代码中第一个字符串的内容被显示在标题栏上。
        # 第二个字符串是对话框上显示的文本。
        # 第三个参数指定了显示在对话框上的按钮集合。
        # 最后一个参数是默认选中的按钮。
        # 这个按钮一开始就获得焦点。返回值被储存在reply变量中。
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        # 测试一下返回值。
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
