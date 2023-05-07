import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from main import MainWindow
from unity.main_list_music import MainWindow


class MainWidget(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Khởi tạo các trang
        self.main = MainWindow()
        self.main_list_music = MainWindow()

        # Thêm các trang vào stack
        self.addWidget(self.main)
        self.addWidget(self.main_list_music)

        # Đặt trang hiển thị ban đầu
        self.setCurrentIndex(0)

        # Kết nối sự kiện để chuyển trang
        self.main.uic.tro_ve.clicked.connect(self.show_main_list_music)
        # print(dir(self.main.uic))

    def show_main_list_music(self):
        self.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    sys.exit(app.exec_())