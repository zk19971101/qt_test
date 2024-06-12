import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QHBoxLayout, QRadioButton


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.radio_btn1 = QRadioButton(text="选择1")
        self.radio_btn1.setObjectName("xuanze1")
        self.radio_btn1.setChecked(True)
        print("选择了1！")

        self.radio_btn2 = QRadioButton(text="选择2")
        self.radio_btn2.setChecked(False)
        self.radio_btn2.setObjectName("xuanze2")

    def main_window(self):
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.radio_btn1)
        main_layout.addWidget(self.radio_btn2)
        self.radio_btn1.toggled.connect(lambda: self.echo_information(self.radio_btn1))
        self.radio_btn2.toggled.connect(lambda: self.echo_information(self.radio_btn2))

    def echo_information(self, btn: QRadioButton):
        if btn.isChecked() and btn.objectName() == "xuanze1":
            print("选择了1！")
        elif btn.isChecked() and btn.objectName() == "xuanze2":
            print("选择了2！")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Windows()
    main.main_window()
    main.show()
    sys.exit(app.exec_())