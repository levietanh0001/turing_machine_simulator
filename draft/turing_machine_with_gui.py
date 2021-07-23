import sys
import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6 import QtCore, QtGui, QtWidgets

    
    # custom theme
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('turing.ui', self)
        self.setWindowTitle('Turing Machine Simulator - Adding Two Binary Numbers')
        # self.button.clicked.connect(self.sayHello)
        
    def sayHello(self):
        inputText = self.input.text()
        self.output.setText('Hello {0}'.format(inputText))       
    
     
    # main 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }               
        
    ''')
    
    myApp = MyApp()
    myApp.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
