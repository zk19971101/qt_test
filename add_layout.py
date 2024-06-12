from PyQt5.QtWidgets import QWidget


from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from PyQt5.QtWidgets import QPushButton, QRadioButton


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.btn1 = QPushButton(text="button1")
        self.btn2 = QPushButton(text="button2")

        self.btn3 = QPushButton(text="button3")
        self.btn4 = QPushButton(text="button4")

    def main_window(self):
        self.setWindowTitle("添加布局")
        self.resize(1440, 720)
        main_layout = QHBoxLayout(self)
        v_layout1 = QVBoxLayout()
        v_layout1.addWidget(self.btn1)
        v_layout1.addWidget(self.btn2)

        v_layout2 = QVBoxLayout()
        v_layout2.addWidget(self.btn3)
        v_layout2.addWidget(self.btn4)

        main_layout.addLayout(v_layout1)
        main_layout.addLayout(v_layout2)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    main = Windows()
    main.main_window()
    main.show()
    sys.exit(app.exec_())