"""
Mesa gui
https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_Working_with_PySide_in_Maya_html
https://www.sidefx.com/docs/houdini/ref/windows/pythonpaneleditor.html

"""

# import the Qt framework
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mesa")

        self.button_checked = True

        button = QPushButton("First Button")
        button.setCheckable(True)
        button.clicked.connect(self.click_action)

        self.setMinimumSize(QSize(200, 200))
        self.setMaximumSize(QSize(500, 500))

        self.setCentralWidget(button)

    def click_action(self):
        print("hi")


# create app object
app = QApplication(["Mesa"]) # App name in list

window = MainWindow()
window.show()

app.exec()

