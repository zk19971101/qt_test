import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication, QHBoxLayout, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.comb_btn = QComboBox(self)
        self.item_list = [f'item {i}' for i in range(5)]
        self.comb_btn.addItems(self.item_list)
        self.comb_btn.currentIndexChanged.connect(lambda: self.get_comb_text())

    def get_comb_text(self):
        print(self.comb_btn.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())