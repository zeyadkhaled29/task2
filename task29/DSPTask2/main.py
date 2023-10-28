import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Task2ui import Ui_MainWindow  # Replace 'ui_file' with your actual module name

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main window and UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    #zeyad
