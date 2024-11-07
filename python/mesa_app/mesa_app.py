"""
Mesa gui
https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_Working_with_PySide_in_Maya_html
https://www.sidefx.com/docs/houdini/ref/windows/pythonpaneleditor.html

"""
import sys
import os
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))) # Try to make this less hardcoded
import mesa_api

# import the Qt framework
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QLabel, QComboBox, QLineEdit, QTabWidget, QVBoxLayout
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




        # Setup shot asset update ui
        """
        shot_update_asset = QWidget()
        shot_update_asset_layout = QHBoxLayout()
        shot_update_asset_layout.addWidget(shot_update_asset_type_label)
        shot_update_asset_layout.addWidget(self.shot_update_asset_types)
        shot_update_asset_layout.addWidget(shot_update_asset_name)
        shot_update_asset_layout.addWidget(shot_update_asset_create)
        shot_update_asset.setLayout(shot_update_asset_layout)
        """

        # Setup update tabs
        update_tabs = QTabWidget()
        update_tabs.setTabPosition(QTabWidget.North)
        update_tabs.setTabShape(QTabWidget.TabShape.Rounded)
        update_tabs.setMovable(False)

        # Add tabs to update tabs
        update_tabs.addTab(QPushButton("Update Show Asset"), "Show") # Replace with show update setup
        update_tabs.addTab(QPushButton("Update Shot Asset"), "Shot") # Replace with shot update setup


        # _________________ Asset Creation Tabs _________________


        # Show asset creation elements       
        self.show_create_asset_types = QComboBox()
        show_create_asset_type_options = ["prop", "set", "char"]
        self.show_create_asset_types.addItems(show_create_asset_type_options)
        show_create_asset_type_label = QLabel("Show Asset Type:")
        show_create_asset_name = QLineEdit("Show Asset Name")
        show_create_asset_name.setFixedWidth(200)
        show_create_asset_create = QPushButton("Create Show Asset")

        # Shot asset creation elements
        self.shot_create_asset_types = QComboBox()
        shot_create_asset_type_options = ["fx", "charfx", "lgt", "crowd"]
        self.shot_create_asset_types.addItems(shot_create_asset_type_options)
        shot_create_asset_type_label = QLabel("Shot Asset Type:")
        shot_create_asset_name = QLineEdit("Shot Asset Name")
        shot_create_asset_name.setFixedWidth(200)
        shot_create_asset_create = QPushButton("Create Shot Asset")


        # Setup show asset creation ui
        show_create_asset = QWidget()
        show_create_asset_layout = QHBoxLayout()
        show_create_asset_layout.addWidget(show_create_asset_type_label)
        show_create_asset_layout.addWidget(self.show_create_asset_types)
        show_create_asset_layout.addWidget(show_create_asset_name)
        show_create_asset_layout.addWidget(show_create_asset_create)
        show_create_asset.setLayout(show_create_asset_layout)

        # Setup shot asset creation ui
        shot_create_asset = QWidget()
        shot_create_asset_layout = QHBoxLayout()
        shot_create_asset_layout.addWidget(shot_create_asset_type_label)
        shot_create_asset_layout.addWidget(self.shot_create_asset_types)
        shot_create_asset_layout.addWidget(shot_create_asset_name)
        shot_create_asset_layout.addWidget(shot_create_asset_create)
        shot_create_asset.setLayout(shot_create_asset_layout)


        # Setup create asset tabs
        create_tabs = QTabWidget()
        create_tabs.setTabPosition(QTabWidget.North)
        create_tabs.setTabShape(QTabWidget.TabShape.Rounded)
        create_tabs.setMovable(False)

        # Add tabs to create tabs
        create_tabs.addTab(show_create_asset, "Show") # Replace with show asset creation setup
        create_tabs.addTab(shot_create_asset, "Shot") # Replace with shot asset creation setup


        # _________________ Core Tabs _________________

        # Setup core tabs
        core_tabs = QTabWidget()
        core_tabs.setTabPosition(QTabWidget.North)
        core_tabs.setTabShape(QTabWidget.TabShape.Rounded)
        core_tabs.setMovable(False)

        # Add tabs to core tabs
        core_tabs.addTab(create_tabs, "Create Asset")
        core_tabs.addTab(QLabel("Fetch latest"), "Sync")
        core_tabs.addTab(QLabel("Open Shot File"), "Open Shot")
        core_tabs.addTab(QLabel("Render Shot"), "Render")
        core_tabs.addTab(QLabel("View Shot"), "View")

        # Set opening tab
        core_tabs.setCurrentIndex(1)

        # core_tabs is central widget
        self.setCentralWidget(core_tabs)



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

    def test_sys(self):
        subprocess.run(["pip", "list"])
        #print("hello")
        






# create app object
app = QApplication(["Mesa"]) # App name in list, maybe add the show name
window = MainWindow()
window.show()

app.exec()

