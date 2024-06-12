import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.btn1 = QPushButton("add")
        self.btn2 = QPushButton("clear")
        self.text_editor = QTextEdit()

    def main_window(self):
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.text_editor)
        main_layout.addWidget(self.btn1)
        main_layout.addWidget(self.btn2)
        self.btn1.clicked.connect(self.add_text)
        self.btn2.clicked.connect(self.clear_text)

    def add_text(self):
        self.text_editor.append("add data")

    def clear_text(self):
        self.text_editor.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.main_window()
    window.show()
    sys.exit(app.exec_())
