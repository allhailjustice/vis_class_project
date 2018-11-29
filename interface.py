import sys
from graphlet import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from utilities import test, training, clear

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Final Project'
        self.width = 1400
        self.height = 550
        self.initUI()
    
    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button1 = QPushButton('Training', self)
        button1.move(0,0)
        button1.resize(140,100)
        button1.clicked.connect(self.prepare)
        
        button2 = QPushButton('Test', self)
        button2.move(0,110)
        button2.resize(140,100)
        button2.clicked.connect(self.test)
        
        button3 = QPushButton('Clear', self)
        button3.move(0,220)
        button3.resize(140,100)
        button3.clicked.connect(self.clear)
        
        
        title1 = QLabel(self)
        title1.setText('estimated_layout')
        title1.adjustSize()
        title1.move(400,10)
        
        self.m1 = QLabel(self)
        self.m1.setPixmap(QPixmap(''))
        self.m1.adjustSize()
        self.m1.move(140,50)
        
        title2 = QLabel(self)
        title2.setText('real_layout')
        title2.adjustSize()
        title2.move(1100,10)
        
        self.m2 = QLabel(self)
        self.m2.setPixmap(QPixmap(''))
        self.m2.adjustSize()
        self.m2.move(760,50)
        
        self.show()
    
    @pyqtSlot()
    def prepare(self):
        training()
    
    @pyqtSlot()
    def test(self):
        self.m1.hide()
        self.m2.hide()
        test()
        m3 = QLabel(self)
        m3.setPixmap(QPixmap('estimated_layout.png'))
        m3.adjustSize()
        m3.move(140,50)
        m4 = QLabel(self)
        m4.setPixmap(QPixmap('real_layout.png'))
        m4.adjustSize()
        m4.move(760,50)
        self.m1 = m3
        self.m2 = m4
        self.m1.show()
        self.m2.show()

    @pyqtSlot()
    def clear(self):
        self.m1.hide()
        self.m2.hide()
        clear()
        self.m1.setPixmap(QPixmap('estimated_layout.png'))
        self.m2.setPixmap(QPixmap('real_layout.png'))
        self.m1.show()
        self.m2.show()
        QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
