from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import sys
import time
from PyQt5.QtCore import *

class Main(QMainWindow):
    def __init__(self): #method for creating widgets

        super(Main, self).__init__()
        loadUi("main.ui", self)
        todos = ["4P84 Review paper", "4P82 1st Assign", "3P94 first stage", "1P06 assign 1", "4P02 start up backend research"]
        for todo in todos:
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.todo_listWidget.addItem(item)
        self.pushButton.clicked.connect(self.toggle_all)
        self.current_value = 0

        self.pbar = QProgressBar(self) 
  
        # setting its geometry 
        self.pbar.setGeometry(30, 530, 300, 25) 
  
        # creating push button 
        self.btn = QPushButton('Progress in %', self) 
        
        # changing its position 
        self.btn.move(20, 565)

        self.btn.setGeometry(27, 561, 100, 40 )
  
        # adding action to push button 
        self.btn.clicked.connect(self.doAction) 
  
        # showing all the widgets 
        self.show() 

        extractAction = Qt.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openEditor = Qt.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = Qt.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = Qt.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)

        self.home()

    def toggle_all(self):
        for i in range (self.todo_listWidget.count()):
            item = self.todo_listWidget.item(i)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)


    # when button is pressed this method is being called 
    def doAction(self): 
  
        # setting for loop to set value of progress bar 
        for i in range(50): 
  
            # slowing down the loop 
            time.sleep(0.03) 
  
            # setting value to progress bar 
            self.pbar.setValue(i)             
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
