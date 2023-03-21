from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os



class Window(QMainWindow):
    POWER_GADGET_PATH = None
    LOG_FILE = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EHCI")
        self.setGeometry(50, 50, 200, 300)
        self.show()

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        power_gadget_path_button = QPushButton("Set PowerLog3.0 path", self)
        power_gadget_path_button.clicked.connect(self.set_power_gadget_path)
        main_layout.addWidget(power_gadget_path_button)

        log_file_button = QPushButton("Chose log file", self)
        log_file_button.clicked.connect(self.create_log)
        main_layout.addWidget(log_file_button)

        monitor_app_button = QPushButton("Monitor Application", self)
        monitor_app_button.clicked.connect(self.monitor_app)
        main_layout.addWidget(monitor_app_button)

        exit_button = QPushButton("Exit", self)
        exit_button.clicked.connect(self.exit_app)
        main_layout.addWidget(exit_button)


    def set_power_gadget_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select directory")

        if folder_path:
            self.POWER_GADGET_PATH = folder_path
            print(f"PowerLog3.0 path set to {self.POWER_GADGET_PATH}")


    def create_log(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save file", "log.csv", "csv files (*.csv);;All Files (*)")

        if file_name:
            if (os.path.exists(file_name)):
                os.remove(file_name)
            
            f = open(file_name, "x")
            f.close()
            self.LOG_FILE = file_name


    def monitor_app(self):
        app_path, _ = QFileDialog.getOpenFileName(self, "Choose exe", "", "exe files (*.exe)")

        if app_path:
            print(f"Monitoring {app_path}")
            os.system(f'powerlog.bat "{self.POWER_GADGET_PATH}" "{self.LOG_FILE}" "{app_path}"')


    def exit_app(self):
        sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
