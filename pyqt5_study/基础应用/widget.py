#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    #创建一个应用（Application）对象，
    # sys.argv参数是一个来自命令行的参数列表
    app = QApplication(sys.argv)
    #没有父类的widget组件将被作为窗口使用。
    # resize()方法调整了widget组件的大小
    # move()方法移动widget组件到一个位置
    # show()方法在屏幕上显示出widget调用
    # exit()方法或主widget组件被销毁，主循环将退出。
    # sys.exit()方法确保一个不留垃圾的退出
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('first_wid')
    w.show()

    sys.exit(app.exec_())