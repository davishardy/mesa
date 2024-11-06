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
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QLabel, QComboBox, QLineEdit, QTabWidget
from PySide6.QtGui import QPalette, QColor



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI setup
        self.setWindowTitle("Mesa")
        #self.setMinimumSize(QSize(200, 200))
        #self.setMaximumSize(QSize(700, 500))
        self.setFixedSize(QSize(700, 500)) # Set window size

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(38, 38, 38)) # Set bg color to grey
        self.setPalette(palette)

        """
        # Create show button
        show_button = QPushButton("Create Show")
        show_button.clicked.connect(self.create_show)

        # Placement
        self.setCentralWidget(show_button)
        """
        """
        asset_type_label = QLabel("Asset Type:")
        self.asset_type = QComboBox()
        asset_types = ["prop", "set", "char", "fx"]
        self.asset_type.addItems(asset_types)
        asset_name = QLineEdit("Asset Name")
        asset_name.setFixedWidth(200)
        asset_create = QPushButton("Create")

        layout = QHBoxLayout()
        layout.addWidget(asset_type_label)
        layout.addWidget(self.asset_type)
        layout.addWidget(asset_name)
        layout.addWidget(asset_create)
        """

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setTabShape(QTabWidget.TabShape.Triangular)
        tabs.setMovable(True)

        tabs.addTab(QPushButton("hi"), "Setup")
        tabs.addTab(QPushButton("Hi There"), "Create")
        tabs.addTab(QPushButton("Hi There"), "Update")
        tabs.addTab(QPushButton("Hi There"), "Render")
        tabs.addTab(QPushButton("Hi There"), "Open")
        tabs.setCurrentIndex(2)

        self.setCentralWidget(tabs)

        #widget = QWidget()
        #widget.setLayout(layout)
        #self.setCentralWidget(widget)

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
window.setWindowIconText("Hi")
window.show()

app.exec()

