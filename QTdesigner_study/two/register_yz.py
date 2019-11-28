from PyQt5.Qt import *
from resource.register import Ui_Form
import sys


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_hide_menue(self):
        print("菜单显示和隐藏")

    def about_yz(self):
        print("about")

    def reset(self):
        print("reset")

    def exit_pane(self):
        print("exit")

    def check_register(self):
        print("check")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
