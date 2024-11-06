"""
Mesa gui
https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_Working_with_PySide_in_Maya_html
https://www.sidefx.com/docs/houdini/ref/windows/pythonpaneleditor.html

"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))) # Try to make this less hardcoded
import mesa_api

# import the Qt framework
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI setup
        self.setWindowTitle("Mesa")
        self.setMinimumSize(QSize(200, 200))
        self.setMaximumSize(QSize(500, 500))


        # Create show button
        show_button = QPushButton("Create Show")
        show_button.clicked.connect(self.create_show)


        # Placement
        self.setCentralWidget(show_button)



    # Button functionality
    def create_show(self):
        current_show = mesa_api.Create()
        current_show.show()

    def create_sequence(self, seq_number):
        current_show = mesa_api.Create()
        current_show.sequence(seq_number)

    def create_shot(self, seq_number, shot_number):
        current_show = mesa_api.Create()
        current_show.shot(seq_number, shot_number)






# create app object
app = QApplication(["Mesa"]) # App name in list

window = MainWindow()
window.show()

app.exec()

