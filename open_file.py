import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("open", self)
        self.file_path = None

    def main_window(self):
        self.btn.clicked.connect(lambda: self.get_file_path())

    def get_file_path(self):
        # parent，caption为弹出框名字，directory为弹出框路径，filter为选区的文件格数
        # 同一个类型的不同格式如xlsx和xls 用空格隔开
        filename, filetype = QFileDialog.getOpenFileName(self, "对话框名字", "./", "text Files (*.txt)")
        print('name:', filename)
        print('type:', filetype)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.main_window()
    window.show()
    sys.exit(app.exec_())