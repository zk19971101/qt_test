import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QPushButton, QHBoxLayout


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.push_btn = QPushButton(text="push button")
        self.push_btn.setObjectName("btn1")

    def main_window(self):
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.push_btn)

        self.push_btn.clicked.connect(lambda: self.push_btn_function(self.push_btn))

    def push_btn_function(self, btn: QPushButton):
        if btn.objectName() == "btn1" and btn.clicked:
            print("push btn is clicked!")
            btn.toggle()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Windows()
    main.main_window()
    main.show()
    sys.exit(app.exec_())