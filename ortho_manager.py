try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *

except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()

from ui.design_ortho_manager import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.left_model = QFileSystemModel()
        self.left_model.setRootPath("/")

        self.left_tree.setModel(self.left_model)
        self.left_tree.setSortingEnabled(True)
        self.left_tree.setAnimated(False)
        self.left_tree.expandAll()
        self.left_tree.sortByColumn(0, Qt.AscendingOrder)

        self.right_model = QFileSystemModel()
        self.right_model.setRootPath("/")

        self.right_tree.setModel(self.right_model)
        self.right_tree.setSortingEnabled(True)
        self.right_tree.setAnimated(False)
        self.right_tree.expandAll()
        self.right_tree.sortByColumn(0, Qt.AscendingOrder)

        self.tab_shortcut = QShortcut(QKeySequence("Tab"), self)
        self.tab_shortcut.activated.connect(self.on_tab)
        self.left_tree.setFocus()

    @pyqtSlot()
    def on_tab(self):
        if self.left_tree.hasFocus():
            print("Tab pressed. Left tree in focus. Switching to right tree.")
            self.right_tree.setFocus()
        else:
            print("Tab pressed. Right tree in focus. Switching to left tree.")
            self.left_tree.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())